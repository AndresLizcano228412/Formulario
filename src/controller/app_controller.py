from __future__ import annotations  # Para compatibilidad con anotaciones futuras

# Importamos las excepciones y la clase Formulario
from src.model.formulario import (
    ErrorFormulario,
    LetraInvalidaError,
    NumeroInvalidoError,
    Formulario
)


# ----------Creamos la clase Controlador-------
class Controlador:
    def __init__(self):
        self.formulario = Formulario()  # creamos una instancia de la clase Formulario

    def procesar_datos(self, datos: dict):
        # procesamos y asignamos cada campo usando los metodos de la clase Formulario
        try:
            self.formulario.nombre = self.formulario._nombre(datos['nombre'])
            self.formulario.apellido = self.formulario._apellido(datos['apellido'])
            # clave corregida: 'numero_de_identificacion' (antes tenía un typo)
            self.formulario.numero_de_identificacion = self.formulario._numero_identificacion(datos['numero_de_identificacion'])
            self.formulario.fecha_nacimiento = self.formulario._fecha_nacimiento(datos['fecha_nacimiento'])
            self.formulario.correo = self.formulario._correo_electronico(datos['correo'])
            self.formulario.direccion = self.formulario._direccion_correspondencia(datos['direccion'])
            self.formulario.numero_hijos = self.formulario._numero_hijos(datos['numero_hijos'])
            self.formulario.cargo = self.formulario._cargo(datos['cargo'])
            self.formulario.empresa = self.formulario._empresa(datos['empresa'])

            return self.formulario  # retornamos el formulario completo
        except (ErrorFormulario, LetraInvalidaError, NumeroInvalidoError, ValueError) as e:  # si algo sale mal lanzamos la excepcion el error
            raise e
        except Exception as e:  # capturamos cualquier otro error inesperado
            raise e
