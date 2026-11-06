"""mermaid
classDiagram
    direction topDown

    class ServicioEmail {
        +enviar_correo(mensaje: str, destino: str)
    }

    class NotificadorUsuario {
        +emisor: ServicioEmail
        +_init_()
        +notificar(mensaje: str, destino: str)
    }

    NotificadorUsuario --> ServicioEmail : depende de
mermaid
classDiagram
    direction topDown

    class ServicioEmail {
        +enviar_correo(mensaje: str, destino: str)
    }

    class NotificadorUsuario {
        +emisor: ServicioEmail
        +_init_()
        +notificar(mensaje: str, destino: str)
    }

    NotificadorUsuario --> ServicioEmail : depende de """