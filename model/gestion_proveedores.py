import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),'../app'))
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from proveedores import Proveedores

class GestionProveedores:
    def __init__(self,root):
        self.root = root
        self.root.title("Proveedores - Ferretería Argamasa")
        self.root.geometry("800x600")

        self.proveedores = Proveedores()

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill= tk.BOTH, expand= True)

        self.titulo = tk.Label(self.frame, text="Proveedores", font=("Arial",24))
        self.titulo.pack(pady=10)

        self.botones = tk.Frame(self.frame)
        self.botones.pack(pady=10)

        self.btn_agg = tk.Button(self.botones, text="AGREGAR PROVEEDOR",command=self.agregar_proveedor)
        self.btn_agg.grid(row=0, column=0, padx=10)

        self.btn_edit = tk.Button(self.botones, text="EDITAR PROVEEDOR",command=self.editar_proveedor)
        self.btn_edit.grid(row=0, column=1, padx=10)

        self.btn_eliminar = tk.Button(self.botones, text="ELIMINAR PROVEEDOR",command=self.eliminar_proveedor)
        self.btn_eliminar.grid(row=0, column=2, padx=10)

        self.tree = ttk.Treeview(self.frame, columns =("id_proveedor","nombre_proveedor","direccion","contacto","email"), show='headings')
        self.tree.heading("id_proveedor", text="Id_proveedor")
        self.tree.heading("nombre_proveedor", text="nombre_proveedor")
        self.tree.heading("direccion", text="Direccion")
        self.tree.heading("contacto", text="Contacto")
        self.tree.heading("email", text="Email")

        self.tree.pack(fill=tk.BOTH, expand=True)
        self.cargar_datos()

    def cargar_datos(self):
        for i in self.tree.get_children():
            self.tree.delete(i)

        proveedor = self.proveedores.obtener_proveedor()
        for i in proveedor:
            self.tree.insert("", tk.END, values=i)

    def agregar_proveedor(self):
        self.dialogo_producto("Añadir Proveedor", self.proveedores.agregar_proveedor)

    def editar_proveedor(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia","Selecciona un proveedor para editar")
            return
        proveedor = self.tree.item(seleccion[0])['values']
        self.dialogo_producto("Editar Proveedor", self.proveedores.editar_proveedor, proveedor)
    
    def eliminar_proveedor(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia","Selecciona un producto para eliminar")
            return
        ID = self.tree.item(seleccion[0])['values'][0]
        if messagebox.askyesno("Confirmación", f"¿Estás seguro de eliminar el Proveedor con código {ID}?"):
            self.proveedores.eliminar_proveedor(ID)
            self.cargar_datos()
        
    def dialogo_producto(self, titulo, accion, proveedor=None):
        dialogo = tk.Toplevel(self.root)
        dialogo.title(titulo)

        etiquetas = ["Id_proveedor","nombre_proveedor","direccion","contacto","email"]
        entradas = {}

        for i, etiqueta in enumerate(etiquetas):
            tk.Label(dialogo, text=etiqueta).grid(row=i, column=0, pady=5)
            entrada = tk.Entry(dialogo)
            entrada.grid(row=i, column=1, pady=5)
            if proveedor:
                entrada.insert(0, proveedor[i])
            entradas[etiqueta.lower()] = entrada

        def on_confirmar():
            try:
                datos = {campo: entradas[campo].get() for campo in entradas}
                if proveedor:
                    accion(proveedor[0], datos["nombre_proveedor"], datos["direccion"], datos["contacto"], datos["email"])
                else:
                    accion(datos["id_proveedor"], datos["nombre_proveedor"], datos["direccion"], datos["contacto"], datos["email"])
                self.cargar_datos()
                dialogo.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        btn_confirmar = tk.Button(dialogo, text="Confirmar", command=on_confirmar)
        btn_confirmar.grid(row=len(etiquetas), column=0, columnspan=2, pady=10)
        
if __name__ == "__main__":
    root = tk.Tk()
    app = GestionProveedores(root)
    root.mainloop()