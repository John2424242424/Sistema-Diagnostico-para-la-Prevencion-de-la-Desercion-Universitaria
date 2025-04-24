#import random
from conexion import db

def obtener_preguntas():
    # Supongo que cada documento en la colección "preguntas" tiene campos "texto" y "categoria"
    preguntas_ref = db.collection('preguntas').stream()
    
    preguntas = {}  # índice: {"texto": ..., "categoria": ...}
    for i, doc in enumerate(preguntas_ref):
        data = doc.to_dict()
        preguntas[i] = {
            "texto": data.get("texto", ""),
            "categoria": data.get("categoria", "Sin categoría")
        }
    return preguntas

    
#preguntas = {
 #      1: "1. Diseñar programas de computación y explorar nuevas aplicaciones tecnológicas para uso del internet",
   #    2: "2. Criar, cuidar y tratar animales domésticos y de campo",
  #     3: "3. Ilustrar, dibujar y animar digitalmente",
   #    4: "4. Investigar sobre áreas verdes, medioambiente y cambios climáticos",
   #    5: "5. Seleccionar, capacitar y motivar al personal de una organización o empresa",
   #    6: "6. Diseñar logotipos y portadas de una revista",
   #    7: "7. Revisar y dar mantenimiento a artefactos eléctricos, electrónicos y computadoras",
   #    8: "8. Aconsejar a las personas sobre planes de ahorro e inversiones",
    #   9: "9. Estudiar la influencia entre las corrientes marinas y el clima y sus consecuencias ecológicas",
   #    10: "10. Controlar ingresos y egresos de fondos y presentar el balance final de una institución",
    #   11: "11. Pintar, hacer esculturas, ilustrar libros de arte, etcétera",
    #   12: "12. Diseñar juegos interactivos electrónicos para computadora"
#}


#def obtener_todas():
   #  return preguntas

#def agregar(self, pregunta):
   # nueva_clave = max(self.preguntas.keys()) + 1
   # self.preguntas[nueva_clave] = pregunta
    
#def eliminar(self, pregunta_id):
   # if pregunta_id in self.preguntas:
   #     del self.preguntas[pregunta_id]