from facultad import Facultad
import csv

class ManejaFacultades:
    __listaF = []

    def __init__(self):
        self.__listaF = []
    
    def cargarFacultades(self):
        indice = 0
        archivo = open('facultades.csv', encoding='utf-8')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            if indice == int(fila[0]):
                self.__listaF[indice-1].agregarCarrera(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
            else:
                instancia = Facultad(fila[0], fila[1], fila[2], fila[3], fila[4])
                self.__listaF.append(instancia)
                indice = int(fila[0])
        archivo.close()
    
    def mostrarCarga(self):
        for fac in self.__listaF:
            print("{}" .format(fac))
            fac.mostrarCarreras()
    
    def buscarFacultad(self, codigo):
        indice = True
        i = 0
        while i < len(self.__listaF) and indice:
            if codigo == self.__listaF[i].getCodigo():
                indice = False
            else:
                i = i + 1
        return i

    def mostrarInciso1(self, codigo):
        i = self.buscarFacultad(codigo)
        if i < len(self.__listaF):
            print("{}:" .format(self.__listaF[i].getNombre()))
            self.__listaF[i].mostrarCarreras()

    def buscarCarrera (self, nombre):
        indice = True
        i = 0
        while i < len(self.__listaF) and indice:
            carreras = self.__listaF[i].getCarreras()
            j = 0
            indic = True
            while j < len(carreras) and indic:
                if carreras[j].getNombre() == nombre:
                    indic = False
                    cod = carreras[j].getCodigo()
                else:
                    j = j + 1
            if j < len(carreras):
                indice = False
            else:
                i = i + 1
        return cod

    def mostrarInciso2(self, nombre):
        codigo = self.buscarCarrera(nombre)
        parte =  codigo.split(".")
        parte1 = int(parte[0])
        print("El codigo es: {}, la facultad es: {} y la localidad donde se encuentra es: {}" .format(codigo, self.__listaF[parte1-1].getNombre(), self.__listaF[parte1-1].getLocalidad()))
