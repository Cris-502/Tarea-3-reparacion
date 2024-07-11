import tkinter as tk
from tkinter import messagebox

def sumar_numeros():
    num1=float (entrada_num1.get())
    num2=float (entrada_num2.get())
    num3=float (entrada_num3.get())
    resultado=num1+num2+num3
    
    messagebox.showinfo("Resultado",f"la suma es de: {resultado}")

def restar_numeros():
    num1=float (entrada_num1.get())
    num2=float (entrada_num2.get())
    num3=float (entrada_num3.get())
    resultado=num1-num2-num3
    messagebox.showinfo("Resultado",f"La resta es de: {resultado}")

def multiplicar_numeros():
    num1=float (entrada_num1.get())
    num2=float (entrada_num2.get())
    num3=float (entrada_num3.get())
    resultado=num1*num2*num3
    messagebox.showinfo("Resultado",f"La resta es de: {resultado}")

def dividir_numeros():
    num1=float (entrada_num1.get())
    num2=float (entrada_num2.get())
    num3=float (entrada_num3.get())
    resultado=num1/num2/num3
    messagebox.showinfo("Resultado",f"La resta es de: {resultado}")


ventana=tk.Tk()
ventana.title("Operaciones Aritmeticas")

etiqueta_num1=tk.Label(ventana,text="Numero 1:")
etiqueta_num1.grid(row=0, column=0, padx=10, pady=10)

etiqueta_num2=tk.Label(ventana,text="Numero 2:")
etiqueta_num2.grid(row=1, column=0, padx=10, pady=10)

etiqueta_num3=tk.Label(ventana,text="Numero 3:")
etiqueta_num3.grid(row=2, column=0, padx=10, pady=10)

#creacion de campos de entrada
entrada_num1=tk.Entry(ventana)
entrada_num1.grid(row=0, column=1, padx=10, pady=10)

entrada_num2=tk.Entry(ventana)
entrada_num2.grid(row=1, column=1, padx=10, pady=10)

entrada_num3=tk.Entry(ventana)
entrada_num3.grid(row=2, column=1, padx=10, pady=10)

#boton para realizar la operacion de suma
boton_sumar=tk.Button(ventana,text="suma", command=sumar_numeros)
boton_sumar.grid(row=4, column=0, columnspan=1, padx=2, pady=10)

boton_restar=tk.Button(ventana,text="Resta", command=restar_numeros)
boton_restar.grid(row=4, column=1, columnspan=1, padx=2, pady=10)

boton_multiplicar=tk.Button(ventana,text="Multiplicacion", command=multiplicar_numeros)
boton_multiplicar.grid(row=4, column=2, columnspan=1, padx=2, pady=10)

boton_dividir=tk.Button(ventana,text="Division", command=dividir_numeros)
boton_dividir.grid(row=4, column=3, columnspan=1, padx=10, pady=10)

ventana.mainloop()