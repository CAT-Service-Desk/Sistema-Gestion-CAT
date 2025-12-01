# Servicio de Autenticación para Estudiantes
import database_connection

def login(email, password):
    """
    Valida las credenciales contra la base de datos institucional
    """
    if not email.endswith("@universidad.edu.co"):
        return "Error: Dominio no permitido"

    user = database_connection.find_user(email)

    if user and user.verify_password(password):
        return "Login Exitoso: Token generado"
    else:
        return "Error: Credenciales inválidas"
