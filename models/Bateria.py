from sqlmodel import SQLModel, Field, Relationship
from typing import Optional
from pydantic import validator
from sqlalchemy import Column, Boolean, Enum
from Enum import *

class Bateria(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    codigo: str = Field(index=True, unique=True, nullable=False)
    tipo: TipoBateria = Field(sa_column=Column(Enum(TipoBateria), nullable=False))
    capacidad_kWh: float
    estado_salud: float = Field(gt=0, le=100)
    ciclos_carga: Optional[int] = Field(default=0, ge=0)
    temperatura_operacion: Optional[float] = Field(default=None)
    estado: EstadoBateria = Field(
        sa_column=Column(Enum(EstadoBateria), default=EstadoBateria.DISPONIBLE)
    )
    vehiculo_id: Optional[int] = Field(default=None, foreign_key="vehiculo.id")
    eliminado: bool = Field(default=False)

    vehiculo: Optional["Vehiculo"] = Relationship(back_populates="bateria")

    @validator("estado_salud")
    def validar_estado_salud(cls, v):
        if not 0 <= v <= 100:
            raise ValueError("El estado de salud debe estar entre 0 y 100.")
        return v

import Vehiculo