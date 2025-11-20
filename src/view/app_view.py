import tkinter as tk
from tkinter import messagebox


class AppView(tk.Tk):
    def __init__(self, controlador=None):
        super().__init__()
        self.controlador = controlador
        self.title("Formulario")
        self.geometry("620x520")
        self.resizable(False, False)

        self.frm = tk.Frame(self, padx=12, pady=12)
        self.frm.pack(fill=tk.BOTH, expand=True)

        self.entries = {}
        self.crear_campos()

    def crear_campos(self):
        campos = [
            "Nombre", "Apellido", "Número de Identificación",
            "Fecha de Nacimiento (YYYY/DD/MM)", "Correo",
            "Dirección", "Número de Hijos", "Cargo", "Empresa"
        ]

        row = 0
        for campo in campos:
            tk.Label(self.frm, text=campo + ":").grid(row=row, column=0, sticky="w", pady=5)
            entry = tk.Entry(self.frm, width=40)
            entry.grid(row=row, column=1, pady=5)
            self.entries[campo] = entry
            row += 1

        tk.Button(self.frm, text="Enviar", command=self.enviar).grid(row=row, column=0, columnspan=2, pady=10)

    def enviar(self):
        datos = {}
        for campo, entry in self.entries.items():
            datos[campo.lower().replace(" ", "_")] = entry.get()

        if self.controlador:
            try:
                formulario_completo = self.controlador.procesar_datos(datos)
                self.mostrar_formulario_procesado(formulario_completo)
            except Exception as e:
                self.mostrar_error(str(e))
        else:
            self.mostrar_mensaje("Problema en el controlador.")

    def mostrar_mensaje(self, mensaje: str):
        messagebox.showinfo("Éxito", mensaje)

    def mostrar_error(self, mensaje: str):
        messagebox.showerror("Error", mensaje)

    def mostrar_formulario_procesado(self, formulario_completo):
        ventana = tk.Toplevel(self)
        ventana.title("Formulario Procesado")
        ventana.geometry("400x400")

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

        row = 0
        for etiqueta, valor in datos.items():
            tk.Label(ventana, text=f"{etiqueta}:").grid(row=row, column=0, sticky="w", padx=10, pady=5)
            tk.Label(ventana, text=str(valor)).grid(row=row, column=1, sticky="w", padx=10, pady=5)
            row += 1
