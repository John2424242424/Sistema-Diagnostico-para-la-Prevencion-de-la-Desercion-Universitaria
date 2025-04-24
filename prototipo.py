class SistemaExpertoVocacional:
        reglas = {
            'Regla 1': {'condiciones': {1: 'Si', 2: 'No', 3: 'No', 4: 'No', 5: 'No', 6: 'No', 7: 'Si', 8: 'No', 9: 'No',
                                        10: 'No', 11: 'No', 12: 'Si'}, 'vocacion': 'Ingeniería de Sistemas'},
            'Regla 2': {'condiciones': {1: 'No', 2: 'Si', 3: 'No', 4: 'Si', 5: 'No', 6: 'No', 7: 'No', 8: 'No', 9: 'Si',
                                        10: 'No', 11: 'No', 12: 'No'}, 'vocacion': 'Ingeniería Ambiental'},
            'Regla 3': {'condiciones': {1: 'No', 2: 'No', 3: 'Si', 4: 'No', 5: 'No', 6: 'Si', 7: 'No', 8: 'No', 9: 'No',
                                        10: 'No', 11: 'Si', 12: 'No'}, 'vocacion': 'Arte y creatividad'},
            'Regla 4': {'condiciones': {1: 'No', 2: 'No', 3: 'No', 4: 'No', 5: 'Si', 6: 'No', 7: 'No', 8: 'Si', 9: 'No',
                                        10: 'Si', 11: 'No', 12: 'No'}, 'vocacion': 'Administración'}
        }

def orientar(respuestas):
    for regla, condiciones in reglas.items():
        coincidencia = True
        for materia, nivel in condiciones['condiciones'].items():
            if nivel != respuestas.get(materia, 'N/A'):
                 coincidencia = False
            break
        if coincidencia:
            return condiciones['vocacion']
    return 'No se encontró una vocación adecuada'

# Crear una instancia del sistema experto
sistema_vocacional = SistemaExpertoVocacional()
    
def enviar_datos(respuestas, preguntas):
    # Verifica si se han respondido todas las preguntas
    if len(respuestas) == len(preguntas):
        respuestas_estudiante = {}
        for i in range(1, 13):
            response = respuestas.get(i, 'N/A')
            respuestas_estudiante[i] = response 
        vocacion_recomendada = sistema_vocacional.orientar(respuestas_estudiante)
        print(vocacion_recomendada)
    else:
        print("Por favor, responde todas las preguntas antes de enviar.")