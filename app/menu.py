import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '../model'))
import tkinter as tk
from tkinter import messagebox
from gestion_inventario import GestionInventario  # Importar la clase GestionInventario
from gestion_categoria import GestionCategoria

class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("FERRETERIA ARGAMASA")
        self.root.geometry("500x500")
        

        self.label_titulo = tk.Label(self.root, text="FERRETERIA ARGAMASA", font=("Arial", 24))
        self.label_titulo.pack(pady=20)

        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=20)

        self.btn_inventario = tk.Button(self.frame_botones, text="INVENTARIO", command=self.abrir_inventario, width=30, height=2, cursor="hand2")
        self.btn_inventario.grid(row=0, column=0, pady=5)

        self.btn_categoria = tk.Button(self.frame_botones, text="CATEGORÍA", command=self.abrir_categoria, width=30, height=2, cursor="hand2")
        self.btn_categoria.grid(row=0, column=1, padx=10, pady=10)

        self.btn_proveedores = tk.Button(self.frame_botones, text="PROVEEDORES", command=self.abrir_proveedores, width=30, height=2, cursor="hand2")
        self.btn_proveedores.grid(row=1, column=0, padx=10, pady=10)

        self.btn_reportes = tk.Button(self.frame_botones, text="REPORTES", command=self.abrir_reportes, width=30, height=2, cursor="hand2")
2        self.btn_reportes.grid(row=1, column=1, padx=10, pady=10)

        self.btn_salir = tk.Button(self.frame_botones, text="Salir", command=self.confirmar_salida, width=30, height=2, cursor="hand2")
        self.btn_salir.grid(row=4, column=0, padx=10, pady=10)

    def abrir_inventario(self):
        self.root.withdraw()  # Ocultar el menú principal
        inventario_root = tk.Toplevel(self.root)
        app = GestionInventario(inventario_root)
        inventario_root.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(inventario_root))

    def abrir_categoria(self):
        self.root.withdraw()
        categoria_root = tk.Toplevel(self.root)
        app = GestionCategoria(categoria_root)
        categoria_root.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(categoria_root))

    def on_closing(self, window):
        window.destroy()
        self.root.deiconify()  # Mostrar el menú principal nuevamente

    def abrir_proveedores(self):
        messagebox.showinfo("PROVEEDORES", "Abriendo Proveedores")

    def abrir_reportes(self):
        messagebox.showinfo("REPORTES", "Abriendo Reportes")

    def confirmar_salida(self):
        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas salir?")
        if respuesta:
 8           self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = MenuPrincipal(root)
    root.mainloop()
8
