from datetime import datetime


class ErrorFormulario(Exception):
    pass


class LetraInvalidaError(Exception):
    pass


class NumeroInvalidoError(Exception):
    pass


class Formulario:

    def __init__(self, nombre, apellido, numero_id, fecha_nacimiento, correo, direccion, numero_hijos, cargo, empresa):
        self.nombre = self._nombre(nombre)
        self.apellido = self._apellido(apellido)
        self.numero_id = self._numero_identificacion(numero_id)
        self.fecha_nacimiento = self._fecha_nacimiento(fecha_nacimiento)
        self.correo = self._correo_electronico(correo)
        self.direccion = self._direccion_correspondencia(direccion)
        self.numero_hijos = self._numero_hijos(numero_hijos)
        self.cargo = self._cargo(cargo)
        self.empresa = self._empresa(empresa)

    def _nombre(self, nombres: str):
        if any(char.isdigit() for char in nombres):
            raise NumeroInvalidoError("El nombre no puede contener números.")
        nombres = nombres.strip()
        nombres = " ".join(nombres.split())
        nombres = nombres.title()
        return nombres

    def _apellido(self, apellidos: str):
        if any(char.isdigit() for char in apellidos):
            raise NumeroInvalidoError("El apellido no puede contener números.")
        apellidos = apellidos.strip()
        apellidos = " ".join(apellidos.split())
        apellidos = apellidos.title()
        return apellidos

    def _numero_identificacion(self, numero_id: str):
        numero_id = numero_id.strip()
        numero_id = numero_id.replace(" ", "")
        numero_id = numero_id.replace(".", "")
        if not numero_id.isdigit():
            raise LetraInvalidaError("El número de identificación debe contener solo numeros.")
        return numero_id

    def _fecha_nacimiento(self, fecha: str):
        try:

            nacimiento = datetime.strptime(fecha, "%d/%m/%Y").date()
        except ValueError:
            raise ValueError("Formato inválido. Usa YYYY-DD-MM")

        hoy = datetime.now().date()
        edad = hoy.year - nacimiento.year
        if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):
            edad -= 1

            return {"fecha": nacimiento, "edad": edad}

    def _correo_electronico(self, correo: str):
        correo = correo.strip().lower()
        if "@" not in correo or "." not in correo:
            raise ValueError("Correo electrónico inválido.")
        return correo

    def _direccion_correspondencia(self, direccion: str):
        direccion = direccion.strip()
        return direccion

    def _numero_hijos(self, numero_hijos: str):
        try:
            numero = int(numero_hijos)
        except ValueError:
            raise LetraInvalidaError("Porfavor no ingrese.")

        if numero < 0 or numero > 10:
            raise ValueError("El número deve estar entre 0 y 10.")
        return numero

    def _cargo(self, cargo: str):
        if any(char.isdigit() for char in cargo):
            raise NumeroInvalidoError("El cargo no puede contener números.")
        cargo = cargo.strip()
        cargo = " ".join(cargo.split())
        cargo = cargo.lower()
        return cargo

    def _empresa(self, empresa: str):
        empresa = empresa.strip()
        empresa = " ".join(empresa.split())
        empresa = empresa.title()
        return empresa
