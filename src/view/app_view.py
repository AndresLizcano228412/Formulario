import tkinter as tk
from tkinter import messagebox


class AppView(tk.Tk):

    def __init__(self):
        super().__init__()
        self.ventana = tk.Tk()
        self.ventana.title("Formulario")
        self.ventana.geometry("400x400")
        self.resizable(False, False)

        frm = tk.Frame(self, padx=12, pady=12)
        frm.pack(fill=tk.BOTH, expand=True)

        tk.Label(frm, text="Formulario de registro", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=12)

        row = 1
        self.lbl_nombre = tk.Label(frm, text="Nombre:")
        self.lbl_nombre.grid(row=row, column=0, sticky="e", padx=10, pady=6)
        self.entry_nombre = tk.Entry(frm)
        self.entry_nombre.grid(row=row, column=1, sticky="w", padx=10, pady=6)

        row += 1
        self.lbl_apellido = tk.Label(frm, text="Apellidos:")
        self.lbl_apellido.grid(row=row, column=0, sticky="e", padx=10, pady=6)
        self.entry_apellido = tk.Entry(frm)
        self.entry_apellido.grid(row=row, column=1, sticky="w", padx=10, pady=6)

        row += 1
        self.lbl_numero_id = tk.Label(frm, text="Número de identificación:")
        self.lbl_numero_id.grid(row=row, column=0, sticky="e", padx=10, pady=6)
        self.entry_numero_id = tk.Entry(frm)
        self.entry_numero_id.grid(row=row, column=1, sticky="w", padx=10, pady=6)

        row += 1
        self.lbl_fecha = tk.Label(frm, text="Fecha de nacimiento (YYYY/DD/MM):")
        self.lbl_fecha.grid(row=row, column=0, sticky="e", padx=10, pady=6)
        self.entry_fecha = tk.Entry(frm)
        self.entry_fecha.grid(row=row, column=1, sticky="w", padx=10, pady=6)

        row += 1
        self.lbl_correo = tk.Label(frm, text="Correo electrónico:")
        self.lbl_correo.grid(row=row, column=0, sticky="e", padx=10, pady=6)
        self.entry_correo = tk.Entry(frm)
        self.entry_correo.grid(row=row, column=1, sticky="w", padx=10, pady=6)

        row += 1
        self.lbl_direccion = tk.Label(frm, text="Dirección:")
        self.lbl_direccion.grid(row=row, column=0, sticky="e", padx=10, pady=6)
        self.entry_direccion = tk.Entry(frm)
        self.entry_direccion.grid(row=row, column=1, sticky="w", padx=10, pady=6)

        row += 1
        self.lbl_hijos = tk.Label(frm, text="Número de hijos:")
        self.lbl_hijos.grid(row=row, column=0, sticky="e", padx=10, pady=6)
        self.entry_hijos = tk.Entry(frm)
        self.entry_hijos.grid(row=row, column=1, sticky="w", padx=10, pady=6)

        row += 1
        self.lbl_cargo = tk.Label(frm, text="Cargo:")
        self.lbl_cargo.grid(row=row, column=0, sticky="e", padx=10, pady=6)
        self.entry_cargo = tk.Entry(frm)
        self.entry_cargo.grid(row=row, column=1, sticky="w", padx=10, pady=6)

        row += 1
        self.lbl_empresa = tk.Label(frm, text="Empresa:")
        self.lbl_empresa.grid(row=row, column=0, sticky="e", padx=10, pady=6)
        self.entry_empresa = tk.Entry(frm)
        self.entry_empresa.grid(row=row, column=1, sticky="w", padx=10, pady=6)

        # --- Botón Enviar ---
        row += 1
        self.btn_enviar = tk.Button(frm, text="Enviar", width=15, command=self.enviar_formulario)
        self.btn_enviar.grid(row=row, column=0, columnspan=2, pady=18)

        self.controlador = None

    def set_controlador(self, controlador):
        """Permite asignar el controlador después de crear la vista."""
        self.controlador = controlador

    def enviar_formulario(self):
        """Recolecta los datos y los envía al controlador (o los imprime si no hay controlador)."""
        datos = {
            "nombre": self.entry_nombre.get(),
            "apellido": self.entry_apellido.get(),
            "numero_id": self.entry_numero_id.get(),
            "fecha_nacimiento": self.entry_fecha.get(),
            "correo": self.entry_correo.get(),
            "direccion": self.entry_direccion.get(),
            "numero_hijos": self.entry_hijos.get(),
            "cargo": self.entry_cargo.get(),
            "empresa": self.entry_empresa.get(),
        }

        if self.controlador:
            # Aquí llamará al controlador que valida los datos
            self.controlador.procesar_datos(datos)
        else:
            # Para pruebas rápidas sin controlador
            print("Datos recogidos:", datos)
            messagebox.showinfo("Prueba", "Datos recogidos (revisa la consola).")

    def mostrar_mensaje(self, mensaje: str):
        messagebox.showinfo("Éxito", mensaje)

    def mostrar_error(self, mensaje: str):
        messagebox.showerror("Error", mensaje)


if __name__ == "__main__":
    vista = Vista()
    vista.mainloop()