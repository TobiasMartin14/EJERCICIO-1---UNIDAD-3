from carrera import Carrera

class Facultad:
    __codigo = str
    __nombre = str
    __direccion = str
    __localidad = str
    __telefono = str
    __carreras = list

    def __init__(self, co, no, di, lo, te):
        self.__codigo = co
        self.__nombre = no
        self.__direccion = di
        self.__localidad = lo
        self.__telefono = te
        self.__carreras = []

    def agregarCarrera(self, codF, codC, nombre, fechaI, duracion, titulo):
        codigo =  codF + '.' + codC
        instancia = Carrera(codigo, nombre, fechaI, duracion, titulo)
        self.__carreras.append(instancia)

    def __str__(self):
        return self.__codigo + ' ' + self.__nombre + ' ' + self.__direccion + ' ' + self.__localidad + ' ' + self.__telefono
    
    def mostrarCarreras(self):
        for car in self.__carreras:
            print(car)
    
    def getCodigo (self):
        return self.__codigo
    
    def getNombre (self):
        return self.__nombre
    
    def getDireccion (self):
        return self.__direccion
    
    def getLocalidad (self):
        return self.__localidad
    
    def getTelefono (self):
        return self.__telefono
    
    def getCarreras(self):
        return self.__carreras
