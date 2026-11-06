class CanalNotificacion {
    <<abstract>>
    +enviar(mensaje: str, destino: str)*
}

class ServicioEmail {
    +enviar(mensaje: str, destino: str)
}

class ServicioSMS {
    +enviar(mensaje: str, destino: str)
}

class ServicioWhatsApp {
    +enviar(mensaje: str, destino: str)
}

class NotificadorUsuario {
    +canal: CanalNotificacion
    +enviar_alerta(mensaje: str, destino: str)
}

CanalNotificacion <|-- ServicioEmail
CanalNotificacion <|-- ServicioSMS
CanalNotificacion <|-- ServicioWhatsApp

NotificadorUsuario --> CanalNotificacion : usa / inyecta
"""
