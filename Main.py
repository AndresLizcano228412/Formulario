from src.controller.app_controller import Controlador
from src.view.app_view import AppView

if __name__ == "__main__":
    controlador = Controlador()
    app = AppView(controlador=controlador)
    app.mainloop()
