from src.controller.app_controller import Controlador
from src.view.app_view import AppView

if _name_ == "_main_":
    controlador = Controlador()
    app = AppView(controlador=controlador)
    app.mainloop()