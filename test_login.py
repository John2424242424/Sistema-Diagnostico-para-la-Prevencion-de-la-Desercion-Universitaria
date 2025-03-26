import pytest
from unittest.mock import MagicMock, patch
from Login import loginUsuario

# Prueba: Login exitoso
@patch("Login.usuarioEntry")
@patch("Login.password")
@patch("Login.ConnexionBD")
@patch("Login.menu")  # Intercepta la función que se llama en un login exitoso
def test_login_exitoso(mock_menu, mock_conexion, mock_password, mock_usuarioEntry):
    mock_usuarioEntry.get.return_value = "usuario_existente@example.com"
    mock_password.get.return_value = "contraseña_correcta"

    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = ("usuario_existente@example.com", "contraseña_correcta")
    mock_conexion.return_value.cursor.return_value = mock_cursor

    loginUsuario()

    # Verifica que se llamó `menu()`, lo que indica un login exitoso
    mock_menu.assert_called_once()

# Prueba: Credenciales incorrectas
@patch("Login.usuarioEntry")
@patch("Login.password")
@patch("Login.ConnexionBD")
@patch("Login.errorLogin")  # Intercepta la función de error
def test_login_credenciales_incorrectas(mock_errorLogin, mock_conexion, mock_password, mock_usuarioEntry):
    mock_usuarioEntry.get.return_value = "usuario_existente@example.com"
    mock_password.get.return_value = "contraseña_incorrecta"

    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = ("usuario_existente@example.com", "contraseña_correcta")
    mock_conexion.return_value.cursor.return_value = mock_cursor

    loginUsuario()

    # Verifica que `errorLogin()` se llamó con el mensaje correcto
    mock_errorLogin.assert_called_once_with("Contraseña incorrecta")

# Prueba: Usuario no registrado
@patch("Login.usuarioEntry")
@patch("Login.password")
@patch("Login.ConnexionBD")
@patch("Login.errorLogin")
def test_login_usuario_no_registrado(mock_errorLogin, mock_conexion, mock_password, mock_usuarioEntry):
    mock_usuarioEntry.get.return_value = "usuario_inexistente@example.com"
    mock_password.get.return_value = "contraseña_cualquiera"

    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = None  # Simula usuario inexistente
    mock_conexion.return_value.cursor.return_value = mock_cursor

    loginUsuario()

    # Verifica que `errorLogin()` se llamó con el mensaje correcto
    mock_errorLogin.assert_called_once_with("El correo no está registrado")

# Prueba: Campos vacíos
@patch("Login.usuarioEntry")
@patch("Login.password")
@patch("Login.ConnexionBD")
@patch("Login.errorLogin")
def test_login_campos_vacios(mock_errorLogin, mock_conexion, mock_password, mock_usuarioEntry):
    mock_usuarioEntry.get.return_value = ""
    mock_password.get.return_value = ""

    loginUsuario()

    # Verifica que `errorLogin()` se llamó con el mensaje correcto
    mock_errorLogin.assert_called_once_with("Tiene que llenar los datos solicitados...")
