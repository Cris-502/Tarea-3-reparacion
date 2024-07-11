import tkinter as tk
from tkinter import messagebox

def saludar():
    print("hola mundo")
    messagebox.showinfo("Lcp","Hola Mundo")

ventana=tk.Tk()
ventana.title("prueba")

boton_saludar=tk.Button(ventana,text="Aceptar", command=saludar)
boton_saludar.pack()


ventana.mainloop()