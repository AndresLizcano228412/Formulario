import tkinter as tk
from tkinter import messagebox


class AppView(tk.Tk):
    def __init__(self, controlador=None):
        super().__init__()
        self.controlador = controlador
        self.title("Rellena Tu Formulario")
        self.geometry("620x520")
        self.resizable(False, False)

        self.frm = tk.Frame(self, padx=12, pady=12)
        self.frm.pack(fill=tk.BOTH, expand=True)

        self.entries = {}
        self.crear_campos()

    def crear_campos(self):
        campos = [
            "nombre", "apellido", "numero_id",
            "fecha_nacimiento", "correo",
            "direccion", "numero_hijos", "cargo", "empresa"
        ]

        etiquetas = [
            "Nombre", "Apellido", "Número de Identificación",
            "Fecha de Nacimiento (DD/MM/YYYY)", "Correo Electrónico",
            "Dirección", "Número de Hijos", "Cargo", "Empresa"
        ]

        for i, campo in enumerate(campos):
            tk.Label(self.frm, text=etiquetas[i] + ":").grid(row=i, column=0, sticky="w", pady=5)
            entry = tk.Entry(self.frm, width=40)
            entry.grid(row=i, column=1, pady=5)
            self.entries[campo] = entry

        tk.Button(self.frm, text="Enviar", command=self.enviar).grid(row=len(campos), column=0, columnspan=2, pady=10)

    def enviar(self):
        datos = {k: e.get() for k, e in self.entries.items()}
        if self.controlador:
            self.controlador.procesar_datos(datos)
        else:
            self.mostrar_mensaje("Formulario ingresado sin controlador")

    def mostrar_mensaje(self, mensaje: str):
        messagebox.showinfo("Éxito", mensaje)

    def mostrar_error(self, mensaje: str):
        messagebox.showerror("Error", mensaje)

    def mostrar_formulario_procesado(self, formulario):
        ventana = tk.Toplevel(self)
        ventana.title("-----Toma tu formulario pues-----")
        ventana.geometry("400x400")

        datos = {
            "Nombre ": formulario.nombre,
            "Apellido ": formulario.apellido,
            "Número de ID ": formulario.numero_id,
            "Fecha de Nacimiento ": formulario.fecha_nacimiento["fecha"],
            "Edad ": formulario.fecha_nacimiento["edad"],
            "Correo ": formulario.correo,
            "Dirección ": formulario.direccion,
            "Número de Hijos ": formulario.numero_hijos,
            "Cargo ": formulario.cargo,
            "Empresa ": formulario.empresa
        }

        row = 0
        for etiqueta, valor in datos.items():
            tk.Label(ventana, text=f"{etiqueta}:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
            tk.Label(ventana, text=str(valor)).grid(row=row, column=1, sticky="w", padx=10, pady=5)
            row += 1
