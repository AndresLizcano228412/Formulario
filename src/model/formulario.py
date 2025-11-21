from datetime import datetime
# importamos la biblioteca parea trabajar fechas y horas en el codigo
# creamos las clases errores que irán en la parte respectiva del codigo


class ErrorFormulario(Exception):
    pass


class LetraInvalidaError(Exception):
    pass


class NumeroInvalidoError(Exception):
    pass


# creamos la clase formulario
class Formulario:
    # creamos valores vacios para que reciban algo despues
    def __init__(self):
        self.nombre = ""
        self.apellido = ""
        self.numero_de_identificacion = ""
        self.fecha_nacimiento = {"fecha": None, "edad": 0}
        self.correo = ""
        self.direccion = ""
        self.numero_hijos = None
        self.cargo = ""
        self.empresa = ""

    # --------------INICIAMOS A CREAR FUNCIONES----------------
    def _nombre(self, nombres: str):
        if any(char.isdigit() for char in nombres):  # recorre cada caracter de la cadena y manda un true si encuentra un numero y lanza error
            raise NumeroInvalidoError("El nombre no puede contener números.")
        nombres = nombres.strip()  # elimina espacios en blanco al inicio y al final
        nombres = " ".join(nombres.split())  # elimina espacios entre palabras y join los une con un solo espacio
        nombres = nombres.title()  # convierte la primera letra de cada palabra en mayuscula
        return nombres  # retorna el valor procesado

    def _apellido(self, apellidos: str):
        if any(char.isdigit() for char in apellidos):
            raise NumeroInvalidoError("El apellido no puede contener números.")
        apellidos = apellidos.strip()
        apellidos = " ".join(apellidos.split())
        apellidos = apellidos.title()
        return apellidos

    def _numero_identificacion(self, numero_de_identificacion: str):
        numero_de_identificacion = numero_de_identificacion.strip()
        numero_de_identificacion = numero_de_identificacion.replace(" ", "")  # elimina espacios en blanco dentro de la cadena
        numero_de_identificacion = numero_de_identificacion.replace(".", "")  # elimina puntos en la cadena
        if not numero_de_identificacion.isdigit():  # aca se usa not para que regrese true si encuentra algo que no es un numero al contratio que en nombre y apellido
            raise LetraInvalidaError("El número de identificación debe contener solo numeros.")
        return numero_de_identificacion

    def _fecha_nacimiento(self, fecha: str):
        try:

            nacimiento = datetime.strptime(fecha, "%Y/%d/%m").date()  # convierte la cadena en un objeto de fecha usando el formato especificado si no manda un error que dice que lo corrija al especificado año dia mes
        except ValueError:
            raise ValueError("Formato inválido. Usa YYYY/DD/MM")

        hoy = datetime.now().date()  # obtiene la fecha actual
        edad = hoy.year - nacimiento.year  # calcula la edad restando los años
        if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):  # si el mes y dia actual es menor al mes y dia de nacimiento se resta 1 a la edad
            edad -= 1

        # retornamos siempre el diccionario con la fecha y la edad calculada
        return {"fecha": nacimiento, "edad": edad}

    def _correo_electronico(self, correo: str):
        correo = correo.strip().lower()  # elimina espacios en blanco y convierte a minusculas
        if "@" not in correo or "." not in correo:  # verifica si el correo contiene un @ y un . si no manda un error
            raise ValueError("Correo electrónico inválido.")
        return correo

    def _direccion_correspondencia(self, direccion: str):
        direccion = direccion.strip()
        return direccion

    def _numero_hijos(self, numero_hijos: str):
        try:
            numero = int(numero_hijos)  # convierte la cadena a un numero entero ni no es un numero manda error
        except ValueError:
            raise LetraInvalidaError("Debe ingresar un número válido.")

        if numero < 0 or numero > 10:  # verifica si el numero esta entre 0 y 10 si no manda error
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
