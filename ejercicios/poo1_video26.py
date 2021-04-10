print("-------------------------------------------------------------")

class coche():
    def __init__(self):
        self.__largo=250
        self.__ancho=120
        self.__ruedas=4
        self.__enmarcha=False
    
    def arrancar(self, arrancamos):
        self.__enmarcha=arrancamos
        
        if(self.__enmarcha):
            chequeo= self.__chequeoInterno()
        
        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        
        elif(self.__enmarcha and chequeo==False):
            return "Algo salio mal en el chequeo. no puede arrancar"
        else:
            return "El coche esta detenido"
                    
    def estado(self):
        print("Ruedas= ", self.__ruedas,
            "ancho= ", self.__ancho,
            "largo= ", self.__largo)
        
    def __chequeoInterno(self):
        print("Chequeo interno")
        
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False
        
        
            
micoche=coche()
print(micoche.arrancar(True))
micoche.estado()

print("___________________SEGUNDA CLASE____________________")

micarro=coche()
print(micarro.arrancar(False))
micarro.estado()

print("-------------------------------------------------------------")