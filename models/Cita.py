from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from datetime import date
from sqlalchemy import Column, Boolean, Enum
from Enum import *

class Cita(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    cliente_id: int = Field(foreign_key="usuario.id")
    tecnico_id: int = Field(foreign_key="usuario.id")
    vehiculo_id: int = Field(foreign_key="vehiculo.id")
    fecha: date
    hora: str
    costo: float
    estado: EstadoCita = Field(sa_column=Column(Enum(EstadoCita), default=EstadoCita.PENDIENTE))

    cliente: Optional["Usuario"] = Relationship(
        back_populates="citas_cliente",
        sa_relationship_kwargs={"foreign_keys": "[Cita.cliente_id]"}
    )
    tecnico: Optional["Usuario"] = Relationship(
        back_populates="citas_tecnico",
        sa_relationship_kwargs={"foreign_keys": "[Cita.tecnico_id]"}
    )
    vehiculo: Optional["Vehiculo"] = Relationship(back_populates="citas")

import Usuario
import Vehiculo