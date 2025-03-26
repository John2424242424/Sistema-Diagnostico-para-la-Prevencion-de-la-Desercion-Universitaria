import concurrent.futures
import time
from Login import loginUsuario
from unittest.mock import MagicMock, patch

# Función para simular un intento de login
def simular_login(usuario, contraseña):
    """Ejecuta loginUsuario() en un entorno simulado para pruebas de estrés."""
    try:
        with patch("Login.ConnexionBD") as mock_conexion, \
             patch("Login.usuarioEntry", MagicMock(get=lambda: usuario)), \
             patch("Login.password", MagicMock(get=lambda: contraseña)), \
             patch("Login.menu") as mock_menu, \
             patch("Login.errorLogin") as mock_error:

            # Simula la base de datos con un usuario válido
            mock_cursor = MagicMock()
            mock_cursor.fetchone.return_value = (usuario, contraseña)  # Usuario encontrado en la BD
            mock_conexion.return_value.cursor.return_value = mock_cursor

            # Ejecuta login
            loginUsuario()

            # Verifica si el login fue exitoso o fallido
            if mock_menu.called:
                return True  # Login exitoso
            elif mock_error.called:
                return False  # Login fallido
            return None  # No se detectó un resultado claro
    except Exception as e:
        print(f"Error durante el login de {usuario}: {e}")
        return None  # Error inesperado

# Prueba de estrés: Simular múltiples intentos de login
def prueba_estres(num_usuarios=100):
    """Ejecuta una prueba de estrés con múltiples logins simultáneos."""
    usuarios = [f"usuario{i}@example.com" for i in range(num_usuarios)]
    contraseñas = [f"contraseña{i}" for i in range(num_usuarios)]

    inicio = time.time()

    # Usar ThreadPoolExecutor para manejar concurrencia
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        resultados = list(executor.map(simular_login, usuarios, contraseñas))

    fin = time.time()

    # Mostrar resultados
    print(f"Prueba de estrés completada en {fin - inicio:.2f} segundos.")
    print(f"Logins exitosos: {resultados.count(True)}")
    print(f"Logins fallidos: {resultados.count(False)}")
    print(f"Resultados desconocidos: {resultados.count(None)}")  # Para detectar errores inesperados

# Ejecutar la prueba de estrés
if __name__ == "__main__":
    prueba_estres(50)  # Prueba con 50 usuarios