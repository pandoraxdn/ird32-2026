import tkinter as tk

root = tk.Tk()

root.geometry("600x400")

root.title("Sistema de acceso")

def evento_click():
    boton1.config(text="Botón presionado")
    print("Ejecución de botón")
    boton2 = tk.Button(root,text="Nuevo botón")
    boton2.pack()

boton1 = tk.Button(root,text="Dar click", command=evento_click)
boton1.pack()

root.mainloop()
