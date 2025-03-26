import pytest
from ConexionBD import ConnexionBD

def test_conexion_bd():
    conexion = ConnexionBD()
    assert conexion is not None  # Verifica que la conexión se establezca correctamente

def test_insertar_usuario():
    conexion = ConnexionBD()
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO usuario (nombre, apellido, correo, contraseña, direccion, estrato, celular) VALUES ('Test', 'User', 'test@example.com', '1234', 'Calle 123', 3, '123456789')")
    conexion.commit()
    cursor.execute("SELECT * FROM usuario WHERE correo = 'test@example.com'")
    resultado = cursor.fetchone()
    assert resultado is not None  # Verifica que el usuario se haya insertado correctamente