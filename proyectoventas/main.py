from tkinter import Label, Entry, Button
from tkinter import ttk

class Ventana:
    def __init__(self, master):
        self.master = master
        self.master.title("Proyecto Ventas")
        #self.master.geometry("800x800")
        #self.master.resizable(False, False)
        self.master.config(bg="blue")
class Usuario(ttk.Frame): 
    def __init__(self, master) -> None:
        self.UI(master)
    def saveUser(self):
        pass
    def deleteUser(self):
        pass
    def updateUser(self):
        pass
    def getUser(self):
        pass
    def UI(self, master):
        self.labelName = Label(self.master, text="Escribe tu nombre")
        self.labelName.grid(row=0, column=0)
        self.name = Entry(self.master)
        self.name.grid(row=0, column=1)
        ##############################
        self.labelLastName = Label(self.master, text="Escribe tu Apellido")
        self.labelLastName.grid(row=1, column=0)
        self.lastName = Entry(self.master)
        self.lastName.grid(row=1, column=1)
        ##############################
        self.labelAge = Label(self.master, text="Escribe tu nombre")
        self.labelAge.grid(row=0, column=0)
        self.age = Entry(self.master)
        self.age.grid(row=0, column=1)
        ##############################
        self.boton = Button(self.master, text="Aceptar", command=self.accion)
        self.boton.grid(row=1, column=0, columnspan=2)
    def accion(self):
        print("Hola", self.entry.get())
        
if __name__ == "__main__":
    from tkinter import Tk
    root = Tk()
    app = Ventana(root)
    usuario = Usuario(root)
    root.geometry("800x800")
    root.mainloop()
#Para un usuario, crea un formulario que pida 
#nombre, apellido, edad, sexo, correo, contraseña, username, hobbies.
#Al presionar el botón, almacena los datos en un diccionario, y posteriormente, genera la consulta 
#para insertar los datos en una tabla de una base de datos.