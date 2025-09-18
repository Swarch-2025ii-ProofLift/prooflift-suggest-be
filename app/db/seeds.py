from datetime import datetime
from ..main import db

# 50 ejercicios con su grupo muscular principal
BASE = [
  # 1–10
  {"slug":"press-banca","group":"pecho","name":"Press de banca con barra","muscles":["pecho","tríceps","hombros"],"goal_tags":["fuerza","hipertrofia"],"equipment":["barra","banco"],"synonyms":["bench press","press banca"],"cues":["escápulas retraídas","barra al esternón"],"level":"intermedio"},
  {"slug":"sentadilla-goblet","group":"piernas","name":"Sentadilla goblet","muscles":["piernas","glúteos","core"],"goal_tags":["hipertrofia","resistencia"],"equipment":["mancuerna","kettlebell"],"synonyms":["goblet squat"],"cues":["pecho alto","rodillas afuera"],"level":"principiante"},
  {"slug":"dominadas-pronas","group":"espalda","name":"Dominadas pronas","muscles":["espalda","bíceps","antebrazos"],"goal_tags":["fuerza","hipertrofia"],"equipment":["barra de dominadas"],"synonyms":["pull-up","dominadas agarre prono"],"cues":["pecho al frente","control en la bajada"],"level":"intermedio"},
  {"slug":"peso-muerto","group":"piernas","name":"Peso muerto convencional","muscles":["cadena posterior","glúteos","isquiotibiales","espalda"],"goal_tags":["fuerza"],"equipment":["barra","discos"],"synonyms":["deadlift"],"cues":["barra pegada","lumbares neutras"],"level":"intermedio"},
  {"slug":"press-militar","group":"hombros","name":"Press militar de pie","muscles":["hombros","tríceps","core"],"goal_tags":["fuerza","hipertrofia"],"equipment":["barra"],"synonyms":["overhead press","press estricto"],"cues":["glúteos activos","barra recta"],"level":"intermedio"},
  {"slug":"remo-mancuerna-una-mano","group":"espalda","name":"Remo con mancuerna a una mano","muscles":["espalda","bíceps"],"goal_tags":["hipertrofia"],"equipment":["mancuerna","banco"],"synonyms":["one-arm dumbbell row"],"cues":["espalda neutra","codo a la cadera"],"level":"principiante"},
  {"slug":"zancadas-mancuernas","group":"piernas","name":"Zancadas con mancuernas","muscles":["piernas","glúteos","core"],"goal_tags":["hipertrofia","resistencia"],"equipment":["mancuernas"],"synonyms":["lunges"],"cues":["paso largo","tronco erguido"],"level":"principiante"},
  {"slug":"jalon-pecho-supino","group":"espalda","name":"Jalón al pecho agarre supino","muscles":["espalda","bíceps"],"goal_tags":["hipertrofia","resistencia"],"equipment":["polea","barra"],"synonyms":["lat pulldown supinated","jalón supino"],"cues":["pecho alto","tira con codos"],"level":"principiante"},
  {"slug":"curl-biceps-barra","group":"brazos","name":"Curl de bíceps con barra","muscles":["bíceps","antebrazos"],"goal_tags":["hipertrofia"],"equipment":["barra"],"synonyms":["barbell curl"],"cues":["codos quietos","no balancear"],"level":"principiante"},
  {"slug":"extension-triceps-polea","group":"brazos","name":"Extensión de tríceps en polea","muscles":["tríceps"],"goal_tags":["hipertrofia","resistencia"],"equipment":["polea","cuerda"],"synonyms":["triceps pushdown"],"cues":["codos pegados","extiende completo"],"level":"principiante"},

  # 11–20
  {"slug":"sentadilla-barra-alta","group":"piernas","name":"Sentadilla con barra (high bar)","muscles":["cuádriceps","glúteos","core"],"goal_tags":["fuerza","hipertrofia"],"equipment":["barra","discos"],"synonyms":["back squat high bar","sentadilla trasera"],"cues":["profundidad segura","rodillas afuera"],"level":"intermedio"},
  {"slug":"sentadilla-frontal","group":"piernas","name":"Sentadilla frontal","muscles":["cuádriceps","glúteos","core"],"goal_tags":["fuerza","hipertrofia"],"equipment":["barra"],"synonyms":["front squat"],"cues":["codos altos","torso erguido"],"level":"intermedio"},
  {"slug":"hip-thrust-barra","group":"piernas","name":"Hip thrust con barra","muscles":["glúteos","isquiotibiales"],"goal_tags":["hipertrofia","fuerza"],"equipment":["barra","banco"],"synonyms":["empuje de cadera"],"cues":["mentón adentro","pélvis en retroversión"],"level":"principiante"},
  {"slug":"pm-rumano-mancuernas","group":"piernas","name":"Peso muerto rumano con mancuernas","muscles":["isquiotibiales","glúteos","espalda baja"],"goal_tags":["hipertrofia"],"equipment":["mancuernas"],"synonyms":["romanian deadlift"],"cues":["bisagra de cadera","recorrido controlado"],"level":"intermedio"},
  {"slug":"remo-barra","group":"espalda","name":"Remo con barra","muscles":["dorsales","romboides","bíceps"],"goal_tags":["fuerza","hipertrofia"],"equipment":["barra"],"synonyms":["barbell row","remo pendlay (var.)"],"cues":["espalda neutra","codo hacia atrás"],"level":"intermedio"},
  {"slug":"face-pull","group":"hombros","name":"Face pull en polea","muscles":["deltoides posteriores","romboides"],"goal_tags":["resistencia","hipertrofia"],"equipment":["polea","cuerda"],"synonyms":["tirón a la cara"],"cues":["pulgares arriba","separa la cuerda"],"level":"principiante"},
  {"slug":"elevaciones-laterales","group":"hombros","name":"Elevaciones laterales con mancuernas","muscles":["deltoides laterales"],"goal_tags":["hipertrofia"],"equipment":["mancuernas"],"synonyms":["lateral raises"],"cues":["codos suaves","hasta línea de hombro"],"level":"principiante"},
  {"slug":"aperturas-mancuernas","group":"pecho","name":"Aperturas con mancuernas en banco","muscles":["pecho"],"goal_tags":["hipertrofia"],"equipment":["mancuernas","banco"],"synonyms":["dumbbell flyes"],"cues":["arco controlado","escápulas fijas"],"level":"principiante"},
  {"slug":"press-inclinado-mancuernas","group":"pecho","name":"Press inclinado con mancuernas","muscles":["pecho superior","tríceps","hombros"],"goal_tags":["hipertrofia","fuerza"],"equipment":["mancuernas","banco"],"synonyms":["incline DB press"],"cues":["escápulas retraídas","trayectoria estable"],"level":"intermedio"},
  {"slug":"jalon-pecho-prono","group":"espalda","name":"Jalón al pecho agarre prono","muscles":["espalda","bíceps"],"goal_tags":["hipertrofia","resistencia"],"equipment":["polea","barra"],"synonyms":["lat pulldown pronated"],"cues":["hombros abajo","control negativo"],"level":"principiante"},

  # 21–30
  {"slug":"remo-polea-baja","group":"espalda","name":"Remo en polea baja","muscles":["dorsales","romboides","bíceps"],"goal_tags":["hipertrofia"],"equipment":["polea","agarre"],"synonyms":["seated cable row"],"cues":["espalda neutra","pecho al frente"],"level":"principiante"},
  {"slug":"dominadas-supinas","group":"espalda","name":"Dominadas supinas","muscles":["espalda","bíceps"],"goal_tags":["fuerza","hipertrofia"],"equipment":["barra de dominadas"],"synonyms":["chin-up"],"cues":["codos adelante","control de core"],"level":"intermedio"},
  {"slug":"fondos-paralelas","group":"brazos","name":"Fondos en paralelas","muscles":["tríceps","pecho","hombros"],"goal_tags":["fuerza","hipertrofia"],"equipment":["barras paralelas"],"synonyms":["dips"],"cues":["hombros abajo","rango cómodo"],"level":"intermedio"},
  {"slug":"curl-inclinado-mancuernas","group":"brazos","name":"Curl inclinado con mancuernas","muscles":["bíceps"],"goal_tags":["hipertrofia"],"equipment":["mancuernas","banco inclinado"],"synonyms":["incline DB curl"],"cues":["estiramiento completo","sin balanceo"],"level":"principiante"},
  {"slug":"martillo-mancuernas","group":"brazos","name":"Curl martillo con mancuernas","muscles":["bíceps","braquiorradial"],"goal_tags":["hipertrofia"],"equipment":["mancuernas"],"synonyms":["hammer curl"],"cues":["agarre neutro","recorrido controlado"],"level":"principiante"},
  {"slug":"extension-triceps-sobre-cabeza","group":"brazos","name":"Extensión de tríceps sobre cabeza (cuerda)","muscles":["tríceps"],"goal_tags":["hipertrofia"],"equipment":["polea","cuerda"],"synonyms":["overhead triceps extension"],"cues":["codos quietos","estira sin dolor"],"level":"principiante"},
  {"slug":"sentadilla-bulgara","group":"piernas","name":"Sentadilla búlgara","muscles":["cuádriceps","glúteos","core"],"goal_tags":["hipertrofia","resistencia"],"equipment":["banco","mancuernas (opcional)"],"synonyms":["bulgarian split squat"],"cues":["talón firme","rodilla estable"],"level":"intermedio"},
  {"slug":"prensa-45","group":"piernas","name":"Prensa 45°","muscles":["cuádriceps","glúteos","isquiotibiales"],"goal_tags":["fuerza","hipertrofia"],"equipment":["prensa 45"],"synonyms":["leg press"],"cues":["rango seguro","empuja con talones"],"level":"principiante"},
  {"slug":"abduccion-cadera-maquina","group":"piernas","name":"Abducción de cadera en máquina","muscles":["glúteos medios"],"goal_tags":["resistencia","hipertrofia"],"equipment":["máquina abductora"],"synonyms":["hip abduction"],"cues":["control al volver","espalda apoyada"],"level":"principiante"},
  {"slug":"aduccion-cadera-maquina","group":"piernas","name":"Aducción de cadera en máquina","muscles":["aductores"],"goal_tags":["resistencia","hipertrofia"],"equipment":["máquina aductora"],"synonyms":["hip adduction"],"cues":["sin rebote","rango cómodo"],"level":"principiante"},

  # 31–40
  {"slug":"curl-femoral-acostado","group":"piernas","name":"Curl femoral acostado","muscles":["isquiotibiales"],"goal_tags":["hipertrofia"],"equipment":["máquina femoral"],"synonyms":["lying leg curl"],"cues":["punta neutra","control excéntrico"],"level":"principiante"},
  {"slug":"extension-cuadriceps","group":"piernas","name":"Extensión de cuádriceps","muscles":["cuádriceps"],"goal_tags":["hipertrofia","resistencia"],"equipment":["máquina extensiones"],"synonyms":["leg extension"],"cues":["no bloquear rodilla","sube y pausa"],"level":"principiante"},
  {"slug":"gemelos-prensa","group":"piernas","name":"Elevación de gemelos en prensa","muscles":["gemelos"],"goal_tags":["hipertrofia","resistencia"],"equipment":["prensa 45"],"synonyms":["calf press"],"cues":["recorrido completo","sin rebote"],"level":"principiante"},
  {"slug":"gemelos-de-pie","group":"piernas","name":"Elevación de gemelos de pie","muscles":["gemelos"],"goal_tags":["hipertrofia","resistencia"],"equipment":["peso corporal","mancuernas (opcional)"],"synonyms":["standing calf raise"],"cues":["talón abajo","sube controlado"],"level":"principiante"},
  {"slug":"plancha","group":"core","name":"Plancha isométrica","muscles":["core"],"goal_tags":["resistencia"],"equipment":["colchoneta"],"synonyms":["plank"],"cues":["línea recta","glúteos activos"],"level":"principiante"},
  {"slug":"rueda-abdominal","group":"core","name":"Rueda abdominal","muscles":["core"],"goal_tags":["resistencia","hipertrofia"],"equipment":["ab wheel"],"synonyms":["ab rollout"],"cues":["no hiperextender","progresivo"],"level":"intermedio"},
  {"slug":"crunch-maquina","group":"core","name":"Crunch en máquina","muscles":["recto abdominal"],"goal_tags":["hipertrofia"],"equipment":["máquina abdominal"],"synonyms":["machine crunch"],"cues":["redondea controlado","exhala al subir"],"level":"principiante"},
  {"slug":"hollow-hold","group":"core","name":"Hollow hold","muscles":["core"],"goal_tags":["resistencia"],"equipment":["colchoneta"],"synonyms":["sostén hueco"],"cues":["zona lumbar pegada","brazos extendidos"],"level":"intermedio"},
  {"slug":"remo-anillas","group":"espalda","name":"Remo en anillas","muscles":["espalda","bíceps","core"],"goal_tags":["resistencia","hipertrofia"],"equipment":["anillas"],"synonyms":["ring row"],"cues":["cuerpo rígido","tirar con codos"],"level":"principiante"},
  {"slug":"peso-muerto-sumo","group":"piernas","name":"Peso muerto sumo","muscles":["glúteos","isquiotibiales","aductores","espalda"],"goal_tags":["fuerza","hipertrofia"],"equipment":["barra"],"synonyms":["sumo deadlift"],"cues":["pies abiertos","rodillas afuera"],"level":"intermedio"},

  # 41–50
  {"slug":"good-morning","group":"piernas","name":"Good morning con barra","muscles":["isquiotibiales","espalda baja"],"goal_tags":["hipertrofia","fuerza"],"equipment":["barra"],"synonyms":["buenos días"],"cues":["bisagra cadera","espalda neutra"],"level":"intermedio"},
  {"slug":"press-arnold","group":"hombros","name":"Press Arnold","muscles":["hombros","tríceps"],"goal_tags":["hipertrofia"],"equipment":["mancuernas"],"synonyms":["arnold press"],"cues":["giro controlado","no hiperextender"],"level":"intermedio"},
  {"slug":"remo-meadows","group":"espalda","name":"Remo Meadows","muscles":["dorsales","romboides","bíceps"],"goal_tags":["hipertrofia"],"equipment":["barra T o landmine","mancuerna"],"synonyms":["meadows row"],"cues":["cadera estable","codo a la cadera"],"level":"intermedio"},
  {"slug":"elevacion-piernas-colgado","group":"core","name":"Elevación de piernas colgado","muscles":["abdominales inferiores","flexores de cadera"],"goal_tags":["resistencia","hipertrofia"],"equipment":["barra"],"synonyms":["hanging leg raise"],"cues":["sin balanceo","sube controlado"],"level":"intermedio"},
  {"slug":"swing-kettlebell","group":"piernas","name":"Swing con kettlebell","muscles":["cadena posterior","glúteos","core"],"goal_tags":["resistencia","potencia técnica"],"equipment":["kettlebell"],"synonyms":["kb swing"],"cues":["bisagra de cadera","no elevar con brazos"],"level":"intermedio"},
  {"slug":"step-up-mancuernas","group":"piernas","name":"Step-up al banco con mancuernas","muscles":["cuádriceps","glúteos"],"goal_tags":["hipertrofia","resistencia"],"equipment":["banco","mancuernas"],"synonyms":["subida al banco"],"cues":["empuja con talón","control al bajar"],"level":"principiante"},
  {"slug":"farmer-walk","group":"core","name":"Farmer walk","muscles":["antebrazos","trapecio","core","piernas"],"goal_tags":["resistencia","fuerza de agarre"],"equipment":["mancuernas","kettlebells"],"synonyms":["paseo del granjero"],"cues":["pasos cortos","tronco firme"],"level":"principiante"},
  {"slug":"press-mancuernas-sentado","group":"hombros","name":"Press con mancuernas sentado","muscles":["hombros","tríceps"],"goal_tags":["hipertrofia","fuerza"],"equipment":["mancuernas","banco"],"synonyms":["seated DB press"],"cues":["recorrido vertical","control excéntrico"],"level":"principiante"},
  {"slug":"remo-pecho-apoyado","group":"espalda","name":"Remo con pecho apoyado","muscles":["espalda media","bíceps"],"goal_tags":["hipertrofia"],"equipment":["banco inclinado","mancuernas"],"synonyms":["chest-supported row"],"cues":["pecho fijo","codo atrás"],"level":"principiante"},
  {"slug":"pull-over-mancuerna","group":"pecho","name":"Pull-over con mancuerna","muscles":["pecho","dorsales","serrato"],"goal_tags":["hipertrofia"],"equipment":["mancuerna","banco"],"synonyms":["dumbbell pullover"],"cues":["codo semiflexionado","arco cómodo"],"level":"principiante"},
]

def _with_media(b):
    slug = b["slug"]
    return {
        **b,
        "media": {
            "type": "image",
            "url": f"/exercises/{slug}/main.webp",
            "thumbnail_url": f"/exercises/{slug}/thumb.webp",
        },
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow(),
    }

def run():
    col = db.exercises
    if col.estimated_document_count() == 0:
        col.create_index([("group", 1)])
        col.create_index([("muscles", 1)])
        col.create_index([("created_at", -1)])
        try:
            col.create_index([("name", "text"), ("synonyms", "text")],
                             name="ex_text", default_language="spanish")
        except Exception:
            pass
        docs = [_with_media(b) for b in BASE]
        col.insert_many(docs)
        print(f"Seed loaded: {len(docs)} exercises")
    else:
        print("Exercises already present; skipping seed")
