from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from pydantic import EmailStr, validator
from datetime import date
from sqlalchemy import Column, Boolean, Enum
from Enum import *


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

    # Relaciones con Cita
    citas_cliente: List["Cita"] = Relationship(
        back_populates="cliente",
        sa_relationship_kwargs={"foreign_keys": "[Cita.cliente_id]"}
    )
    citas_tecnico: List["Cita"] = Relationship(
        back_populates="tecnico",
        sa_relationship_kwargs={"foreign_keys": "[Cita.tecnico_id]"}
    )

    @validator("contraseña")
    def validar_contraseña(cls, v):
        if len(v) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres.")
        return v

    @validator("nombre")
    def validar_nombre(cls, v):
        if not all(c.isalpha() or c.isspace() for c in v):
            raise ValueError("El nombre solo puede contener letras y espacios.")
        return v

import Cita