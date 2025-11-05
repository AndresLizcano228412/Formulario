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
        self.vista = None

    def set_vista(self, vista: AppView):
        self.vista = vista

    def procesar_datos(self, datos: dict):
        try:
            self.formulario.nombre = self.formulario._nombre(datos["nombre"])
            self.formulario.apellido = self.formulario._apellido(datos["apellido"])
            self.formulario.numero_id = self.formulario._numero_identificacion(datos["numero_id"])
            self.formulario.fecha_nacimiento = self.formulario._fecha_nacimiento(datos["fecha_nacimiento"])
            self.formulario.correo = self.formulario._correo_electronico(datos["correo"])
            self.formulario.direccion = self.formulario._direccion_correspondencia(datos["direccion"])
            self.formulario.numero_hijos = self.formulario._numero_hijos(datos["numero_hijos"])
            self.formulario.cargo = self.formulario._cargo(datos["cargo"])
            self.formulario.empresa = self.formulario._empresa(datos["empresa"])

            if self.vista:
                self.vista.mostrar_formulario_procesado(self.formulario)
            else:
                print("Formulario procesado:", vars(self.formulario))

        except (ErrorFormulario, LetraInvalidaError, NumeroInvalidoError, ValueError) as e:
            if self.vista:
                self.vista.mostrar_error(f"Error en el formulario: {str(e)}")
        except Exception as e:
            if self.vista:
                self.vista.mostrar_error(f"Error inesperado: {str(e)}")
