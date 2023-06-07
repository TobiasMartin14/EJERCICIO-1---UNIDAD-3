from manejaFacultades import ManejaFacultades
from menu import Menu

if __name__ == '__main__':
    MF = ManejaFacultades()
    MF.cargarFacultades()
    MF.mostrarCarga()
    M = Menu()
    M.opciones(MF)