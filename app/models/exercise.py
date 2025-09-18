from typing import List, Optional, Literal
from pydantic import BaseModel, Field

Group = Literal["pecho","espalda","piernas","hombros","brazos","core"]

class Media(BaseModel):
    type: Optional[Literal["image","gif","video"]] = "image"
    url: Optional[str] = None
    thumbnail_url: Optional[str] = None

class ExerciseListItem(BaseModel):
    id: str = Field(alias="id")
    name: str
    group: Group
    muscles: List[str]
    media: Optional[Media] = None

class ExerciseDetail(ExerciseListItem):
    # campos extra del detalle
    goal_tags: List[str] = []
    equipment: List[str] = []
    synonyms: List[str] = []
    cues: List[str] = []
    level: Optional[str] = None

class PageMeta(BaseModel):
    next_cursor: Optional[str] = None
    limit: int

class ExerciseListResponse(BaseModel):
    items: List[ExerciseListItem]
    page: PageMeta
