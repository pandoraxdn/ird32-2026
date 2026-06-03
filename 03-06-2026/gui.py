import tkinter as tk

ventana = tk.Tk()

ventana.title("Mi primer app")

ventana.geometry("800x600")

etiqueta = tk.Label(
    ventana,
    text="Hola mi nombre es Roself",
    font=("Arial",40),
    bg="pink",
    fg="white",
    width=20,
    height=2
)
etiqueta.pack()

def saludar():
    print("Hola")

button = tk.Button(
    ventana,
    text="Saludar",
    command=saludar
)
button.pack()

def sumar():
    valor1 = int(entrada1.get())
    valor2 = int(entrada2.get())
    print(valor1 + valor2)

entrada1 = tk.Entry(ventana)
entrada1.pack()
entrada2 = tk.Entry(ventana)
entrada2.pack()

button1 = tk.Button(
    ventana,
    text="Sumar",
    command=sumar
)
button1.pack()

ventana.mainloop()
