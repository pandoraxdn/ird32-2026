import tkinter as tk

root = tk.Tk()

root.geometry("600x400")

root.title("Sistema de acceso")

root.rowconfigure(0,weight=2)
root.rowconfigure(1,weight=10)
root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=5)

def evento1():
    boton1.config(text="Presione botón 1",fg="white",bg="pink")

def evento2():
    boton2.config(text="Presione botón 2")

"""
    GRID
    0   1   2   3
0   x   x   x   x
1   x   x   x   x
2   x   x   x   x
3   x   x   x   x
"""

boton1 = tk.Button(
    root,
    text="Boton 1",
    command=evento1,
    bg="violet",
    fg="white",
    font=("Arial",20)
)

# N (arriba), E (derecha), S (abajo), W (izquierda)
boton1.grid(row=0,column=0,sticky="W",padx=10,pady=10)

boton2 = tk.Button(
    root,
    text="Boton 2",
    command=evento2
)
boton2.grid(row=2,column=2,sticky="E")

root.mainloop()
