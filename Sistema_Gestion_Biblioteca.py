from abc import ABC, abstractmethod


#clase abstracta 
class MaterialBiblioteca(ABC):
    def _init_(self, titulo:str, autor:str, anio:int):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio
        self.__disponible = True

    def get_titulo(self)->str:
        return self.__titulo
    
    def set_titulo(self, titulo:str)->None:
        self.__titulo = titulo

    def get_autor(self)->str:
        return self.__autor
    
    def set_autor(self,autor)->None:
        self.__autor
        
    def get_anio(self)->int:
        return self.__anio
    
    def set_anio(self,anio:int)->None:
        self.__anio = anio

    def esta_disponible(self)->bool:
        return self.__disponible
    
    def set_disponible(self, disponible:bool)->bool:
        self.__disponible = disponible

    def prestar(self)->bool:
        if self.__disponible:
            self.__disponible = False
            return True
        return False

    def devolver(self):
        self.__disponible = True

    # Método abstracto 
    @abstractmethod
    def calcular_fecha_devolucion(self, dia_actual):
        pass

    @abstractmethod
    def obtener_detalles(self):
        pass


class Libro(MaterialBiblioteca):
    def _init_(self, titulo, autor, anio, genero):
        super()._init_(titulo, autor, anio)
        self.__genero = genero
    #polimorfismo
    def calcular_fecha_devolucion(self, dia_actual):
        return dia_actual + 15   

    def obtener_detalles(self):
        return f"[Libro] {self.get_titulo()} - {self.get_autor()} ({self.get_anio()}) - {self.__genero}"


class Revista(MaterialBiblioteca):
    def _init_(self, titulo, autor, anio, numero):
        super()._init_(titulo, autor, anio)
        self.__numero = numero

    def calcular_fecha_devolucion(self, dia_actual):
        return dia_actual + 7    # préstamo de 7 días

    def obtener_detalles(self):
        return f"[Revista] {self.get_titulo()} - {self.get_autor()} (N° {self.__numero}, {self.get_anio()})"


class MaterialAudiovisual(MaterialBiblioteca):
    def _init_(self, titulo, autor, anio, formato):
        super()._init_(titulo, autor, anio)
        self.__formato = formato

    def calcular_fecha_devolucion(self, dia_actual):
        return dia_actual + 3    # préstamo de 3 días

    def obtener_detalles(self):
        return f"[Audiovisual] {self.get_titulo()} - {self.get_autor()} ({self.get_anio()}) - {self.__formato}"

class Usuario:
    def _init_(self, nombre, cedula):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__prestamos = []

    def prestar_material(self, material, dia_actual):
        if material.prestar():
            fecha_devolucion = material.calcular_fecha_devolucion(dia_actual)
            self.__prestamos.append((material, fecha_devolucion))
            print(f"{self.__nombre} ha prestado '{material.get_titulo()}'. Debe devolverlo en el día {fecha_devolucion}.")
        else:
            print(f"El material '{material.get_titulo()}' no está disponible.")

    def mostrar_prestamos(self):
        print(f"📚 Materiales prestados por {self.__nombre}:")
        for material, fecha in self.__prestamos:
            print(f"- {material.obtener_detalles()} | Fecha de devolución: día {fecha}")



if _name_ == "_main_":

    dia_actual = 100

    # Crear materiales
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Realismo mágico")
    revista1 = Revista("National Geographic", "Varios", 2023, 150)
    dvd1 = MaterialAudiovisual("El Padrino", "Francis Ford Coppola", 1972, "DVD")

    # Crear usuario
    usuario1 = Usuario("Juan Restrepo")

    # Usuario presta materiales
    usuario1.prestar_material(libro1, dia_actual)
    usuario1.prestar_material(revista1, dia_actual)
    usuario1.prestar_material(dvd1, dia_actual)

    # Mostrar préstamos
    usuario1.mostrar_prestamos()


