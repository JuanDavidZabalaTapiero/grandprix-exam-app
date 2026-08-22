class AppError(Exception):
    default_message = "Ocurrió un error inesperado."
    status_code = 400

    def __init__(self, message=None, **kwargs):
        base_message = message or self.default_message

        # Pasar argumentos al mensaje
        try:
            formatted_message = base_message.format(**kwargs)
        except KeyError:
            formatted_message = base_message

        super().__init__(formatted_message)
