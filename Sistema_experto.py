reglas = {
            'Regla 1': {'condiciones': {1: 'Si', 2: 'No', 3: 'No', 4: 'No', 5: 'No', 6: 'No', 7: 'Si', 8: 'No', 9: 'No',
                                        10: 'No', 11: 'No', 12: 'Si'}, 'vocacion': 'Ingeniería de Sistemas'},
            'Regla 2': {'condiciones': {1: 'No', 2: 'Si', 3: 'No', 4: 'Si', 5: 'No', 6: 'No', 7: 'No', 8: 'No', 9: 'Si',
                                        10: 'No', 11: 'No', 12: 'No'}, 'vocacion': 'Ingeniería Ambiental'},
            'Regla 3': {'condiciones': {1: 'No', 2: 'No', 3: 'Si', 4: 'No', 5: 'No', 6: 'Si', 7: 'No', 8: 'No', 9: 'No',
                                        10: 'No', 11: 'Si', 12: 'No'}, 'vocacion': 'Arte y creatividad'},
            'Regla 4': {'condiciones': {1: 'No', 2: 'No', 3: 'No', 4: 'No', 5: 'Si', 6: 'No', 7: 'No', 8: 'Si', 9: 'No',
                                        10: 'Si', 11: 'No', 12: 'No'}, 'vocacion': 'Administración'},
            'Regla 5': {'condiciones': {1: 'Si', 2: 'Si', 3: 'No', 4: 'No', 5: 'No', 6: 'No', 7: 'Si', 8: 'No', 9: 'No',
                                        10: 'No', 11: 'No', 12: 'Si'}, 'vocacion': 'Ingeniería de Sistemas'},
            'Regla 6': {'condiciones': {1: 'Si', 2: 'Si', 3: 'No', 4: 'Si', 5: 'No', 6: 'No', 7: 'No', 8: 'No', 9: 'Si',
                                        10: 'No', 11: 'No', 12: 'No'}, 'vocacion': 'Ingeniería Ambiental'},
            'Regla 7': {'condiciones': {1: 'Si', 2: 'No', 3: 'Si', 4: 'No', 5: 'No', 6: 'Si', 7: 'No', 8: 'No', 9: 'No',
                                        10: 'No', 11: 'Si', 12: 'No'}, 'vocacion': 'Arte y creatividad'},
            'Regla 8': {'condiciones': {1: 'Si', 2: 'Si', 3: 'Si', 4: 'No', 5: 'Si', 6: 'No', 7: 'No', 8: 'Si', 9: 'No',
                                        10: 'Si', 11: 'No', 12: 'Si'}, 'vocacion': 'Administración'}
        }



def orientar(respuestas):
    for regla, condiciones in reglas.items():
        coincidencia = True
        for materia, nivel in condiciones['condiciones'].items():
            if nivel.lower() != respuestas[materia].lower():
                coincidencia = False
                break
        if coincidencia:
            return condiciones['vocacion']
    return 'No se encontró una vocación adecuada'