velocidad = 0
encendido = False
opcion = 99
distancia = 0
def encender():
    global encendido
    encendido = not(encendido)
    print("Vehículo encendido" if encendido else "Vehículo apagado")
def acelerar():
    global velocidad
    if velocidad>=0 and encendido:
        velocidad += 10 
        avanzar() 
    else:
        print("El vehículo está apagado o está en reversa")
    print("Velocidad actual "+(str(velocidad)))
def frenar():
    global velocidad
    if velocidad>=0 and encendido:
        velocidad -= 10  
    else:
        print("El vehículo está apagado o está detenido")
    print("Velocidad actual "+(str(velocidad)))
def avanzar():
    global velocidad, distancia
    if velocidad>0 and encendido:
        distancia += 10*velocidad  
    else:
        print("El vehículo está apagado o está detenido")
    print("La distancia recorrida es "+(str(distancia)))
def detener():
    global velocidad
    velocidad=0
    print("El vehículo se ha detenido")
nombre = input("Nombre conductor")
patente = input("patente vehiculo")
while(opcion != 0):
    print('*-'*20)
    print("1.- Acelerar")
    print("2.- Frenar")
    print("3.- Detener")
    print("4.- Encender / Apagar")
    print("0.- Salir")
    opcion = int(input("Ingrese opción"))
    if(opcion == 1):
        acelerar()
    elif(opcion==2):
        frenar()
    elif(opcion==3):
        detener()
    elif(opcion==4):
        encender()
    elif(opcion==0):
        print("Fin del programa, hasta pronto")