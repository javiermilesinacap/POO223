import pygame
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
objeto = Vehiculo()
pygame.init()
ventana = pygame.display.set_mode((800,600))
autito = pygame.image.load('./car.png').convert_alpha()
while(True):
    for event in pygame.event.get():
        if(event.type== pygame.KEYDOWN and event.key == pygame.K_w):
            objeto.acelerar()
            objeto.avanzar()
            print(objeto)    
        if(event.type== pygame.KEYDOWN and event.key == pygame.K_s):
            objeto.frenar()
            objeto.retroceder() 
            print(objeto)  
        ventana.blit(autito,(objeto.lat,300))
        pygame.display.update() 