import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.geometry("600x400")

root.title("Sistema de acceso")

etiqueta = tk.Label(root,text="Login del Sistema", font=("Arial",50))
etiqueta.grid(row=0,column=1)

# Justificar texto de entry
# tk.CENTER, tk.LEFT, tk.RIGHT
entrada1 = tk.Entry(root,width=40,justify=tk.CENTER,font=("Arial",20))
entrada1.grid(row=1,column=1)
entrada1.insert(0,"Introduce el nombre del usuario: ")
entrada1.insert(tk.END, ".")

def enviar():
    """
    print(entrada1.get())
    boton.config(text=entrada1.get())
    # Limpiar la entrada
    entrada1.select_range(0,tk.END)
    entrada1.focus()
    """
    usuario = entrada1.get()
    if usuario == "Ana":
        messagebox.showwarning("Ten cuidado amigo","Piensalo dos veces")
    if usuario == "Osmar":
        messagebox.showerror("Mensaje de error","Tu nombre no es valido")
    if usuario == "Natasha":
        messagebox.showinfo("Mensaje Informativo","Dato Nuevo")

boton = tk.Button(root,text="Enviar", command=enviar, font=("Arial",20))
boton.grid(row=2,column=2)
root.mainloop()
