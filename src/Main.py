from __future__ import annotations
from src.controller.app_controller import Controlador
from src.model.formulario import Formulario
from src.view.app_view import AppView


if __name__ == "__main__":
    formulario = Formulario()  # modelo
    controlador = Controlador(formulario)  # controlador
    app = AppView()  # vista
    app.set_controlador(controlador)  # conectas controlador con vista
    app.mainloop()
