import enum

class TipoBateria(str, enum.Enum):
    LITIO_ION = "Litio-ion"
    PLOMO_ACIDO = "Plomo-ácido"
    NIMH = "NiMH"
    SOLIDA = "Sólida"


class EstadoBateria(str, enum.Enum):
    DISPONIBLE = "Disponible"
    EN_USO = "En uso"
    EN_MANTENIMIENTO = "En mantenimiento"


class RolUsuario(str, enum.Enum):
    ADMIN = "admin"
    TECNICO = "tecnico"
    CLIENTE = "cliente"


class MarcaVehiculo(str, enum.Enum):
    TESLA = "Tesla"
    NISSAN = "Nissan"
    BMW = "BMW"
    RENAULT = "Renault"
    CHEVROLET = "Chevrolet"

class EstadoVehiculo(str, enum.Enum):
    DISPONIBLE = "Disponible"
    EN_TALLER = "En taller"
    EN_MANTENIMIENTO = "En mantenimiento"


class EstadoCita(str, enum.Enum):
    PENDIENTE = "Pendiente"
    EN_PROGRESO = "En progreso"
    COMPLETADA = "Completada"