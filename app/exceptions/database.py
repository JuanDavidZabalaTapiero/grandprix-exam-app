class DatabaseError(Exception):
    default_message = "Ocurrió un error al procesar la operación en la base de datos."
    status_code = 500
