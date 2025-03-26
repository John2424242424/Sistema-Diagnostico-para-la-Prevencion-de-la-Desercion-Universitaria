from Sistema_experto import orientar

def test_ingenieria_sistemas():
    # Respuestas que coinciden con Ingeniería de Sistemas
    respuestas = {1: 'Si', 2: 'No', 3: 'No', 4: 'No', 5: 'No', 6: 'No', 7: 'Si', 8: 'No', 9: 'No', 10: 'No', 11: 'No', 12: 'Si'}
    resultado = orientar(respuestas)
    assert resultado == 'Ingeniería de Sistemas'

def test_ingenieria_ambiental():
    # Respuestas que coinciden con Ingeniería Ambiental
    respuestas = {1: 'No', 2: 'Si', 3: 'No', 4: 'Si', 5: 'No', 6: 'No', 7: 'No', 8: 'No', 9: 'Si', 10: 'No', 11: 'No', 12: 'No'}
    resultado = orientar(respuestas)
    assert resultado == 'Ingeniería Ambiental'

def test_arte_y_creatividad():
    # Respuestas que coinciden con Arte y creatividad
    respuestas = {1: 'No', 2: 'No', 3: 'Si', 4: 'No', 5: 'No', 6: 'Si', 7: 'No', 8: 'No', 9: 'No', 10: 'No', 11: 'Si', 12: 'No'}
    resultado = orientar(respuestas)
    assert resultado == 'Arte y creatividad'

def test_administracion():
    # Respuestas que coinciden con Administración
    respuestas = {1: 'No', 2: 'No', 3: 'No', 4: 'No', 5: 'Si', 6: 'No', 7: 'No', 8: 'Si', 9: 'No', 10: 'Si', 11: 'No', 12: 'No'}
    resultado = orientar(respuestas)
    assert resultado == 'Administración'

def test_sin_coincidencia():
    # Respuestas que no coinciden con ninguna regla
    respuestas = {1: 'No', 2: 'No', 3: 'No', 4: 'No', 5: 'No', 6: 'No', 7: 'No', 8: 'No', 9: 'No', 10: 'No', 11: 'No', 12: 'No'}
    resultado = orientar(respuestas)
    assert resultado == 'No se encontró una vocación adecuada'