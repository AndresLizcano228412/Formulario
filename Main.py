from src.controller.app_controller import Controlador  # Importamos el controlador
from src.view.app_view import AppView  # Importamos la vista

if __name__ == "__main__":
    controlador = Controlador()  # Creamos una instancia del controlador
    app = AppView(controlador=controlador)  # Creamos la instancia de la vista y le pasamos el controlador
    app.mainloop()  # Iniciamos el bucle principal de la aplicación GUI
