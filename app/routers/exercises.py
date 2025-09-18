from fastapi import APIRouter, HTTPException, Query
from typing import Optional, Dict, Any, List
from bson import ObjectId

from ..db.mongo import get_db
from ..models.exercise import (
    ExerciseListItem,
    ExerciseDetail,
    ExerciseListResponse,
    PageMeta,
)

db = get_db()
router = APIRouter(prefix="/exercises", tags=["exercises"])

ALLOWED_GROUPS = {"pecho", "espalda", "piernas", "hombros", "brazos", "core"}


@router.get("", response_model=ExerciseListResponse)
def search_exercises(
    group: Optional[str] = Query(
        None,
        description="Grupo muscular principal: pecho|espalda|piernas|hombros|brazos|core",
    ),
    # opcional: filtro fino por un músculo concreto dentro del array "muscles"
    muscle: Optional[str] = Query(
        None, description="Músculo específico (opcional), p. ej. tríceps"
    ),
    q: Optional[str] = Query(
        None, min_length=2, max_length=80, description="Búsqueda por nombre/sinónimos"
    ),
    limit: int = Query(20, ge=1, le=50),
    cursor: Optional[str] = Query(
        None, description="Cursor basado en _id para paginación ascendente"
    ),
) -> ExerciseListResponse:
    """
    Lista ejercicios para pintar cards.
    Devuelve: id, name, group, muscles, media.thumbnail_url
    Filtros: group (principal), muscle (fino), q (texto).
    Paginación: cursor por _id ascendente.
    """
    filt: Dict[str, Any] = {}

    if group:
        g = group.strip().lower()
        if g not in ALLOWED_GROUPS:
            raise HTTPException(status_code=400, detail="invalid_group")
        filt["group"] = g

    if muscle:
        # coincide si el músculo está en el array "muscles"
        filt["muscles"] = muscle.strip().lower()

    if q:
        filt["$text"] = {"$search": q}

    if cursor:
        try:
            filt["_id"] = {"$gt": ObjectId(cursor)}
        except Exception:
            raise HTTPException(status_code=400, detail="invalid_cursor")

    cur = (
        db.exercises.find(
            filt,
            projection={
                "name": 1,
                "group": 1,
                "muscles": 1,
                "media.thumbnail_url": 1,
            },
        )
        .sort("_id", 1)
        .limit(limit)
    )

    raw_items: List[Dict[str, Any]] = list(cur)
    next_cursor = str(raw_items[-1]["_id"]) if len(raw_items) == limit else None

    items: List[ExerciseListItem] = []
    for it in raw_items:
        _id = str(it.pop("_id"))
        thumb = None
        if isinstance(it.get("media"), dict):
            thumb = it["media"].get("thumbnail_url")
        items.append(
            ExerciseListItem(
                id=_id,
                name=it.get("name"),
                group=it.get("group"),
                muscles=it.get("muscles", []),
                media={"thumbnail_url": thumb} if thumb else None,
            )
        )

    return ExerciseListResponse(
        items=items, page=PageMeta(next_cursor=next_cursor, limit=limit)
    )


@router.get("/{id}", response_model=ExerciseDetail)
def get_exercise(id: str) -> ExerciseDetail:
    """
    Detalle completo del ejercicio (incluye media.url para la vista grande).
    """
    try:
        _id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=400, detail="invalid_id")

    doc = db.exercises.find_one({"_id": _id})
    if not doc:
        raise HTTPException(status_code=404, detail="exercise_not_found")

    doc["id"] = str(doc.pop("_id"))
    return ExerciseDetail(**doc)
