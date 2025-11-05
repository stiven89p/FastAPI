<div align="center">
  <h1>Taller FastAPI</h1>
  <p><em>Autor: stiven89p</em></p>
  <p>
  Proyecto de ejemplo construido con FastAPI. Contiene una API sencilla (endpoints básicos) y estructura preparada para ampliar con modelos y routers.
  </p>

  [![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com/stiven89p/FastAPI/releases)
  [![FastAPI](https://img.shields.io/badge/FastAPI-v0.118.3-green.svg)](https://fastapi.tiangolo.com/)
  [![Python](https://img.shields.io/badge/Python-3.8%2B-yellow.svg)](https://www.python.org/)
</div>

## Descripción
Aplicación mínima en FastAPI con la intención de ser usada como taller o plantilla. Actualmente incluye un endpoint de ejemplo que devuelve "hola mundo" y la estructura base preparada para añadir modelos y routers.

## Estructura del Proyecto

El repositorio contiene al menos los siguientes archivos y carpetas:

```
.
├── main.py               # Aplicación principal FastAPI (ruta: ./main.py)
├── models/               # (Directorio) para modelos del proyecto
└── routers/              # (Directorio) para routers / endpoints
```

Nota: Las carpetas models/ y routers/ existen en el repositorio y están listas para agregar los archivos de modelo y rutas que necesites.

## Endpoints conocidos
- GET /Hola/  
  - Descripción: endpoint de ejemplo que responde con "hola mundo".
  - Ejemplo de respuesta: "hola mundo"

Además, cuando la aplicación está en ejecución, FastAPI genera documentación automática en:
- Swagger UI: /docs
- ReDoc: /redoc
- OpenAPI JSON: /openapi.json

## Modelos
Vehiculo
   ```bash
   class Vehiculo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    marca: MarcaVehiculo
    modelo: str
    año: int
    imagen_url: Optional[str]
    estado: EstadoVehiculo
    eliminado: bool = Field(default=False)
    bateria: Optional["Bateria"] 
    citas: List["Cita"]
   ```
Cita
   ```bash
   class Cita(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="usuario.id")
    tecnico_id: int = Field(foreign_key="usuario.id")
    vehiculo_id: int = Field(foreign_key="vehiculo.id")
    fecha: date
    hora: str
    costo: float
    estado: EstadoCita
    cliente: Optional["Usuario"]
    tecnico: Optional["Usuario"] 
    vehiculo: Optional["Vehiculo"]
   ```
Bateria
   ```bash
   class Bateria(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str = Field(index=True, unique=True, nullable=False)
    tipo: TipoBateria = Field(sa_column=Column(Enum(TipoBateria), nullable=False))
    capacidad_kWh: float
    estado_salud: float = Field(gt=0, le=100)
    ciclos_carga: Optional[int] = Field(default=0, ge=0)
    temperatura_operacion: Optional[float] = Field(default=None)
    estado: EstadoBateria 
    vehiculo_id: Optional[int] = Field(default=None, foreign_key="vehiculo.id")
    eliminado: bool = Field(default=False)
    vehiculo: Optional["Vehiculo"] = Relationship(back_populates="bateria")
   ```
Usuario
   ```bash
   class Usuario(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str = Field(index=True, min_length=2, max_length=50)
    apellido: str = Field(index=True, min_length=2, max_length=50)
    email: EmailStr = Field(unique=True, index=True)
    telefono: Optional[str] = Field(default=None)
    direccion: Optional[str] = Field(default=None)
    contraseña: str = Field(min_length=6)
    rol: RolUsuario = Field(sa_column=Column(Enum(RolUsuario), nullable=False))
    fecha_registro: date = Field(default_factory=date.today)
    activo: bool = Field(default=True, sa_column=Column(Boolean, default=True))
    eliminado: bool = Field(default=False, sa_column=Column(Boolean, default=False))

    citas_cliente: List["Cita"]
    citas_tecnico: List["Cita"]
    ```
    

## Requisitos Previos
- Git
- Python 3.8+
- pip

## Instalación y ejecución (entorno local)

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/stiven89p/FastAPI.git
   cd FastAPI
   ```

2. Crear y activar un entorno virtual:
   ```bash
   # macOS / Linux
   python3 -m venv .venv
   source .venv/bin/activate

   # Windows (PowerShell)
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Instalar dependencias mínimas (si no hay requirements.txt):
   ```bash
   pip install fastapi uvicorn
   ```
   - Si tienes un requirements.txt, ejecuta:
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecutar la aplicación:
   ```bash
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```
   (Reemplaza `main:app` si la instancia de FastAPI está en otro módulo/path.)

5. Abrir en el navegador:
   - Aplicación: http://127.0.0.1:8000/
   - Swagger UI: http://127.0.0.1:8000/docs

## Probar el endpoint de ejemplo

Usando curl:
```bash
curl -X GET "http://127.0.0.1:8000/Hola/" -H "accept: application/json"
```

Deberías recibir:
```
hola mundo
```

## Desarrollo y ampliación
- Añade modelos en el directorio models/ (p. ej. Pydantic o SQLModel).
- Añade routers en routers/ y regístralos en main.py con app.include_router(...).
- Crea un requirements.txt con:
  ```bash
  pip freeze > requirements.txt
  ```
