import tkinter as tk  # Importamos la libreria tkinter para crear la interfaz grafica
from tkinter import messagebox  # Importamos el modulo messagebox para mostrar mensajes emergentes


# Creamos la clase AppView que hereda de tk.Tk
class AppView(tk.Tk):
    def __init__(self, controlador=None):
        super().__init__()  # inicializamos la clase padre tk.Tk
        self.controlador = controlador  # guardamos la referencia al controlador
        self.title("Formulario")  # escojemos el titulo de la ventana
        self.geometry("520x620")  # elejimos el tamaño de la ventana
        self.resizable(False, False)  # que no puedan agrandar ni encojer la ventana

        self.frm = tk.Frame(self, padx=12, pady=12)  # creamos una marjen para que lo escrito no slaga de hay
        self.frm.pack(fill=tk.BOTH, expand=True)  # hacemos que el marco ocupe todo el espacio de la ventana

        self.entries = {}  # diccionario para guardar las referencias a los campos de entrada
        self.crear_campos()  # llamamos al metodo para crear los campos de entrada

    def crear_campos(self):
        self.frm.columnconfigure(0, weight=1)
        # lista de los campos que van a aber
        campos = [
            ("Nombre", "nombre"),
            ("Apellido", "apellido"),
            ("Número de Identificación", "numero_de_identificacion"),
            ("Fecha de Nacimiento (YYYY/DD/MM)", "fecha_nacimiento"),
            ("Correo", "correo"),
            ("Dirección", "direccion"),
            ("Número de Hijos", "numero_hijos"),
            ("Cargo", "cargo"),
            ("Empresa", "empresa"),
        ]

        row = 0  # esta es la fila inicial para colocar los campos
        for etiqueta, clave in campos:  # recorremos la lista de campos
            tk.Label(self.frm, text=etiqueta, bg="green", fg="white").grid(row=row, column=0, pady=(10, 0), sticky="N")  # creamos la etiqueta que va antes de e cuadro de escribir
            row += 1  # aumentamos la fila para colocar el cuadro de escribir debajo de la etiqueta
            entry = tk.Entry(self.frm, width=40)  # creamos el cuadro de escribir
            entry.grid(row=row, column=0, pady=5)  # colocamos el cuadro en su pocicion
            self.entries[clave] = entry  # guardamos la referencia del cuadro en el diccionario con su clave correspondiente
            row += 1  # aumentamos la fila para el siguiente campo

        tk.Button(self.frm, text="Enviar", command=self.enviar).grid(row=row, column=0, columnspan=2, pady=10)  # creamos el boton de enviar que llama al metodo enviar

    def enviar(self):  # metodo que se llama cuando se presiona el boton enviar
        datos = {}  # diccionario para guardar los datos ingresados
        for clave, entry in self.entries.items():  # recorremos los cuadros de entrada
            datos[clave] = entry.get()  # obtenemos el texto ingresado y lo guardamos en el diccionario

        if self.controlador:
            try:
                formulario_completo = self.controlador.procesar_datos(datos)  # llamamos al metodo del controlador para procesar los datos
                self.mostrar_formulario_procesado(formulario_completo)
            except Exception as e:  # si hay un error lo mostramos en un mensaje emergente
                self.mostrar_error(str(e))
        else:
            self.mostrar_mensaje("Problema en el controlador.")

    def mostrar_mensaje(self, mensaje: str):
        messagebox.showinfo("Éxito", mensaje)  # mostramos un mensaje emergente de informacion

    def mostrar_error(self, mensaje: str):
        messagebox.showerror("Error", mensaje)

# ---------------- Creamos una nueva ventana que muestre los datos procesados ----------------
    def mostrar_formulario_procesado(self, formulario_completo):
        ventana = tk.Toplevel(self)
        ventana.title("Formulario Procesado")
        ventana.geometry("400x400")
        # diccionario con los datos procesados
        datos = {
            "Nombre": formulario_completo.nombre,
            "Apellido": formulario_completo.apellido,
            "Número de ID": formulario_completo.numero_de_identificacion,
            "Fecha de Nacimiento": formulario_completo.fecha_nacimiento['fecha'],
            "Edad": formulario_completo.fecha_nacimiento['edad'],
            "Correo": formulario_completo.correo,
            "Dirección": formulario_completo.direccion,
            "Número de Hijos": formulario_completo.numero_hijos,
            "Cargo": formulario_completo.cargo,
            "Empresa": formulario_completo.empresa
        }

        row = 0  # fila inicial
        for etiqueta, valor in datos.items():  # recorremos los datos procesados
            tk.Label(ventana, text=f"{etiqueta}:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
            tk.Label(ventana, text=str(valor)).grid(row=row, column=1, sticky="w", padx=10, pady=5)  # convertimos el valor a cadena para mostrarlo
            row += 1
