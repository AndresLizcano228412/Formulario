from src.controller.app_controller import Controlador
from src.view.app_view import AppView


def main():
    controlador = Controlador()
    vista = AppView(controlador=controlador)
    controlador.set_vista(vista)
    vista.mainloop()


if __name__ == "__main__":
    main()
