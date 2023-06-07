
class Carrera:
    __codigo = str
    __nombre = str
    __fechaInicio = str
    __duracion = str
    __titulo = str

    def __init__(self, co, no, fe, du, ti):
        self.__codigo = co
        self.__nombre = no
        self.__fechaInicio = fe
        self.__duracion = du
        self.__titulo = ti

    def getCodigo (self):
        return self.__codigo
    
    def getNombre (self):
        return self.__nombre

    def getFechaInicio (self):
        return self.__fechaInicio
    
    def getDuracion (self):
        return self.__duracion
    
    def getTitulo (self):
        return self.__titulo
    
    def __str__(self):
        return self.__codigo + ' ' + self.__nombre + ' ' + self.__fechaInicio + ' ' + self.__duracion + ' ' + self.__titulo
    
