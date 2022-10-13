class Vehiculo:
    def acelerar(self,cuanto=0)-> None:
        self.velocidad += 10 + cuanto
    def frenar(self,cuanto=0)-> None:
        self.velocidad -= 10 + cuanto
    def avanzar(self):
        self.lat += (self.velocidad/100)+5
        pass
    def retroceder(self):
        self.lat -= (self.velocidad/100)+5
        pass
    def __init__(self,velocidad=0,lat=0.0,lon=0.0,modelo="",ppu="",color="") -> None:
        self.velocidad = velocidad
        self.lat = lat
        self.lon = lon
        self.modelo = modelo
        self.ppu = ppu
        self.color= color
    def __str__(self)->str:
        return (f'El vehiculo {self.modelo} patente {self.ppu} color {self.color} va a {self.velocidad} km/h')
base=[]
while(True):
    print("1 crear vehiculo, 9.- imprimir 0 salir")
    opcion = int(input())
    if(opcion==1):
        a = input("Ingrese marca")
        b = input("Ingrese patenet")
        objeto = Vehiculo(100,12.4,33.6,a,b,"Gris")
        print(objeto)
        objeto.acelerar()
        print(objeto.velocidad)
        base.append(objeto)
    if(opcion==9):
        print(base)
    