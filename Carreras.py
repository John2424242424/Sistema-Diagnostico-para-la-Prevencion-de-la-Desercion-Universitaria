from conexion import db

def obtener_carreras():
    carreras_ref = db.collection('carreras').stream()
    carreras = {}
    for doc in carreras_ref:
        data = doc.to_dict()
        nombre = data.get("nombreC", "Sin nombre")
        carreras[nombre] = {
            "campo_laboral": data.get("campo_laboral", "Sin información"),
            "descripcion": data.get("descripcion", "Sin descripción")
        }
    return carreras
