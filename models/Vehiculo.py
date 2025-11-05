from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from sqlalchemy import Column, Boolean, Enum
from Enum import *

class Vehiculo(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    marca: MarcaVehiculo
    modelo: str
    año: int
    imagen_url: Optional[str] = Field(default=None, description="URL de la imagen del vehículo")
    estado: EstadoVehiculo = Field(
        sa_column=Column(Enum(EstadoVehiculo), default=EstadoVehiculo.DISPONIBLE)
    )
    eliminado: bool = Field(default=False, sa_column=Column(Boolean, default=False))

    bateria: Optional["Bateria"] = Relationship(
        back_populates="vehiculo",
        sa_relationship_kwargs={"uselist": False}
    )
    citas: List["Cita"] = Relationship(back_populates="vehiculo")


import Bateria
import Cita

