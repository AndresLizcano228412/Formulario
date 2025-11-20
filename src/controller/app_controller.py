from __future__ import annotations

from src.model.formulario import (
    ErrorFormulario,
    LetraInvalidaError,
    NumeroInvalidoError,
    Formulario
)
from src.view.app_view import AppView


class Controlador:
    def __init__(self):
        self.formulario = Formulario()

    def procesar_datos(self, datos: dict):
        try:
            self.formulario.nombre = self.formulario._nombre(datos['nombre'])
            self.formulario.apellido = self.formulario._apellido(datos['apellido'])
            self.formulario.numero_de_identificacion = self.formulario._numero_identificacion(datos['numero_de_dentificacion'])
            self.formulario.fecha_nacimiento = self.formulario._fecha_nacimiento(datos['fecha_nacimiento'])
            self.formulario.correo = self.formulario._correo_electronico(datos['correo'])
            self.formulario.direccion = self.formulario._direccion_correspondencia(datos['direccion'])
            self.formulario.numero_hijos = self.formulario._numero_hijos(datos['numero_hijos'])
            self.formulario.cargo = self.formulario._cargo(datos['cargo'])
            self.formulario.empresa = self.formulario._empresa(datos['empresa'])

            return self.formulario
        except (ErrorFormulario, LetraInvalidaError, NumeroInvalidoError, ValueError) as e:
            raise e
        except Exception as e:
            raise e
