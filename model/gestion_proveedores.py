import sys
import os

# Añadir rutas al sys.path para poder importar módulos desde directorios específicos
sys.path.append(os.path.join(os.path.dirname(__file__), '../app'))

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from proveedores import Proveedores

class GestionProveedores:
    def __init__(self, root):
        # Inicializa la ventana principal
        self.root = root
        self.root.title("Proveedores - Ferretería Argamasa")  # Establecer el título de la ventana
        self.root.geometry("800x600")  # Establecer el tamaño de la ventana principal

        # Crear una instancia de la clase Proveedores
        self.proveedores = Proveedores()

        # Configuración del marco principal
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)  # Empaquetar el marco para llenar el espacio disponible

        # Título de la ventana
        self.titulo = tk.Label(self.frame, text="Proveedores", font=("Arial", 24))
        self.titulo.pack(pady=10)  # Añadir un espaciado vertical

        # Contenedor de botones
        self.botones = tk.Frame(self.frame)
        self.botones.pack(pady=10)  # Añadir un espaciado vertical

        # Botón para agregar proveedor
        self.btn_agg = tk.Button(self.botones, text="AGREGAR PROVEEDOR", command=self.agregar_proveedor)
        self.btn_agg.grid(row=0, column=0, padx=10)  # Añadir un espaciado horizontal

        # Botón para editar proveedor
        self.btn_edit = tk.Button(self.botones, text="EDITAR PROVEEDOR", command=self.editar_proveedor)
        self.btn_edit.grid(row=0, column=1, padx=10)  # Añadir un espaciado horizontal

        # Botón para eliminar proveedor
        self.btn_eliminar = tk.Button(self.botones, text="ELIMINAR PROVEEDOR", command=self.eliminar_proveedor)
        self.btn_eliminar.grid(row=0, column=2, padx=10)  # Añadir un espaciado horizontal

        # Crear una tabla (Treeview) para mostrar los proveedores
        self.tree = ttk.Treeview(self.frame, columns=("id_proveedor", "nombre_proveedor", "direccion", "contacto", "email"), show='headings')
        self.tree.heading("id_proveedor", text="Codigo")  # Configurar encabezados de columna
        self.tree.heading("nombre_proveedor", text="Proveedor")
        self.tree.heading("direccion", text="Direccion")
        self.tree.heading("contacto", text="Contacto")
        self.tree.heading("email", text="Email")

        self.tree.pack(fill=tk.BOTH, expand=True)  # Empaquetar la tabla para llenar el espacio disponible
        self.cargar_datos()  # Cargar datos en la tabla al iniciar

    def cargar_datos(self):
        # Limpiar datos actuales de la tabla
        for i in self.tree.get_children():
            self.tree.delete(i)

        # Obtener los proveedores desde la base de datos y agregarlos a la tabla
        proveedor = self.proveedores.obtener_proveedor()
        for i in proveedor:
            self.tree.insert("", tk.END, values=i)

    def agregar_proveedor(self):
        # Abrir un diálogo para agregar un nuevo proveedor
        self.dialogo_producto("Añadir Proveedor", self.proveedores.agregar_proveedor)

    def editar_proveedor(self):
        # Editar el proveedor seleccionado en la tabla
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un proveedor para editar")
            return
        proveedor = self.tree.item(seleccion[0])['values']
        self.dialogo_producto("Editar Proveedor", self.proveedores.editar_proveedor, proveedor)

    def eliminar_proveedor(self):
        # Eliminar el proveedor seleccionado en la tabla
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showwarning("Advertencia", "Selecciona un producto para eliminar")
            return
        ID = self.tree.item(seleccion[0])['values'][0]
        if messagebox.askyesno("Confirmación", f"¿Estás seguro de eliminar el Proveedor con código {ID}?"):
            self.proveedores.eliminar_proveedor(ID)
            self.cargar_datos()

    def dialogo_producto(self, titulo, accion, proveedor=None):
        # Abre un diálogo para ingresar o editar datos del proveedor
        dialogo = tk.Toplevel(self.root)
        dialogo.title(titulo)

        # Etiquetas y campos de entrada para los datos del proveedor
        etiquetas = ["Id_proveedor", "nombre_proveedor", "direccion", "contacto", "email"]
        entradas = {}

        for i, etiqueta in enumerate(etiquetas):
            tk.Label(dialogo, text=etiqueta).grid(row=i, column=0, pady=5)  # Etiquetas en la columna 0
            entrada = tk.Entry(dialogo)
            entrada.grid(row=i, column=1, pady=5)  # Campos de entrada en la columna 1
            if proveedor:
                entrada.insert(0, proveedor[i])  # Rellenar campos si se está editando un proveedor
            entradas[etiqueta.lower()] = entrada

        def on_confirmar():
            # Valida y guarda los datos del proveedor
            try:
                datos = {campo: entradas[campo].get() for campo in entradas}
                if proveedor:
                    # Editar proveedor existente
                    accion(proveedor[0], datos["nombre_proveedor"], datos["direccion"], datos["contacto"], datos["email"])
                else:
                    # Agregar nuevo proveedor
                    accion(datos["id_proveedor"], datos["nombre_proveedor"], datos["direccion"], datos["contacto"], datos["email"])
                self.cargar_datos()
                dialogo.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        # Botón para confirmar la acción en el diálogo
        btn_confirmar = tk.Button(dialogo, text="Confirmar", command=on_confirmar)
        btn_confirmar.grid(row=len(etiquetas), column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = GestionProveedores(root)
    root.mainloop()
