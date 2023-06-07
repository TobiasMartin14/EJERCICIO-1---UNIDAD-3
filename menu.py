
class Menu:
    __opcion = 0
    def __init__ (self):
        self.__opcion = 0
    def opciones(self, MF):
        indice = True
        while indice:
            print("\n") 
            print ("Opcion 1: Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.")
            print ("Opcion 2: Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta. ")
            print ("Opcion 3: Salir")
            self.__opcion = int(input("Seleccione una opcion: "))
            if (self.__opcion == 1):
                codigo = str(input("Ingrese el codigo de una Facultad: "))
                MF.mostrarInciso1(codigo)
            elif (self.__opcion == 2):
                nombre = str(input("Ingrese el nombre de una carrera: "))
                MF.mostrarInciso2(nombre)
            elif (self.__opcion == 3):
                indice = False
            else:
                print("La opcion ingresada no es valida.")