import tkinter as tk
from tkinter import Menu
import sys

root = tk.Tk()

root.geometry("600x400")

root.title("Sistema de acceso")

def salir():
    root.destroy()
    sys.exit() 

def desplegar_menu():
    menu_principal = Menu(root)
    submenu_archivo = Menu(menu_principal,tearoff=0)
    submenu_archivo.add_command(label="Nuevo")
    submenu_archivo.add_command(label="Salir",command=salir)
    submenu_crud = Menu(menu_principal,tearoff=0)
    submenu_crud.add_command(label="Añadir usuario")
    menu_principal.add_cascade(menu=submenu_archivo,label="Archivo")
    menu_principal.add_cascade(menu=submenu_crud,label="CRUD")
    root.config(menu=menu_principal)

desplegar_menu()


root.mainloop()
