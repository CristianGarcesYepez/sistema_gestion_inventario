import sys
import os

# Añadir rutas a sys.path para poder importar módulos desde directorios específicos
sys.path.append(os.path.join(os.path.dirname(__file__), '../model'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../reporte'))

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Importar las clases de gestión
from gestion_inventario import GestionInventario
from gestion_categoria import GestionCategoria
from gestion_proveedores import GestionProveedores
from gestion_reporte import GestionReporte

class MenuPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("FERRETERIA ARGAMASA")  # Establecer el título de la ventana principal
        self.root.geometry("800x600")  # Establecer el tamaño de la ventana principal
        self.root.resizable(False, False)  # Desactivar el redimensionamiento de la ventana
        self.root.iconbitmap("recursos/LOGO.ico")  # Establecer el icono de la ventana principal
        
        # Llamar a métodos para configurar la interfaz
        self.crear_canvas()
        self.create_widgets()
        self.cargar_imagen_fondo()
        self.actualizar_imagen_fondo()

        # Actualizar la imagen de fondo cuando se redimensiona la ventana
        self.root.bind("<Configure>", self.actualizar_imagen_fondo)

    def crear_canvas(self):
        # Crear un canvas para colocar elementos gráficos
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="nsew")

    def cargar_imagen_fondo(self):
        try:
            # Intentar cargar la imagen de fondo
            self.bg_image = Image.open("recursos/FONDO.png")
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo, tags="bg_image")
        except Exception as e:
            # Manejo de errores en caso de fallo al cargar la imagen
            print(f"Error al cargar la imagen de fondo: {e}")

    def actualizar_imagen_fondo(self, event=None):
        # Ajustar la imagen de fondo al tamaño del canvas
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        resized_image = self.bg_image.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(resized_image)
        
        self.canvas.delete("bg_image")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo, tags="bg_image")
        
        self.actualizar_imagen_centrada()

    def actualizar_imagen_centrada(self):
        try:
            # Cargar y centrar la imagen del logo
            image_path = "recursos/ARGAMASA_logo.png"
            centered_image = Image.open(image_path)
            centered_photo = ImageTk.PhotoImage(centered_image)

            img_width, img_height = centered_image.size
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()

            # Calcular la posición del logo centrado
            x = (canvas_width - img_width) // 2
            y = -200
            
            self.canvas.delete("centered_image")
            self.canvas.create_image(x, y, anchor=tk.NW, image=centered_photo, tags="centered_image")
            
            # Agregar texto al canvas
            title_text = "MENÚ"
            self.canvas.create_text(x + img_width // 2, y + img_height - 190, text="MENÚ", font=("Arial", 30, "bold"), fill="black", tags="title_text")
            
            self.centered_photo = centered_photo

        except Exception as e:
            # Manejo de errores en caso de fallo al cargar la imagen centrada
            print(f"Error al cargar la imagen centrada: {e}")

    def create_widgets(self):
        # Crear y colocar los botones en el menú principal
        self.btn_inventario = tk.Button(self.root, text="INVENTARIO", command=self.abrir_inventario, width=20, height=4, font=("Arial", 12, "bold"), bg="#DCD2F0", cursor="hand2")
        self.btn_inventario.grid(row=1, column=1, padx=0, pady=60)

        self.btn_categoria = tk.Button(self.root, text="CATEGORÍA", command=self.abrir_categoria, width=20, height=4, font=("Arial", 12, "bold"), bg="#DCD2F0", cursor="hand2")
        self.btn_categoria.grid(row=2, column=1, padx=0, pady=5)

        self.btn_proveedores = tk.Button(self.root, text="PROVEEDORES", command=self.abrir_proveedores, width=20, height=4, font=("Arial", 12, "bold"), bg="#DCD2F0", cursor="hand2")
        self.btn_proveedores.grid(row=1, column=2, padx=0, pady=0)

        self.btn_reportes = tk.Button(self.root, text="REPORTES", command=self.abrir_reportes, width=20, height=4, font=("Arial", 12, "bold"), bg="#DCD2F0", cursor="hand2")
        self.btn_reportes.grid(row=2, column=2, padx=0, pady=5)

        self.btn_salir = tk.Button(self.root, text="SALIR", command=self.confirmar_salida, width=20, height=4, font=("Arial", 12, "bold"), bg="#DCD2F0", cursor="hand2")
        self.btn_salir.grid(row=3, column=1, columnspan=2, padx=0, pady=0)

    def abrir_inventario(self):
        # Abrir la ventana de gestión de inventario
        self.root.withdraw()  # Ocultar el menú principal
        inventario_root = tk.Toplevel(self.root)
        app = GestionInventario(inventario_root)
        inventario_root.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(inventario_root))

    def abrir_categoria(self):
        # Abrir la ventana de gestión de categorías
        self.root.withdraw()
        categoria_root = tk.Toplevel(self.root)
        app = GestionCategoria(categoria_root)
        categoria_root.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(categoria_root))

    def on_closing(self, window):
        # Mostrar el menú principal al cerrar una ventana secundaria
        window.destroy()
        self.root.deiconify()

    def abrir_proveedores(self):
        # Abrir la ventana de gestión de proveedores
        self.root.withdraw()
        proveedores_root = tk.Toplevel(self.root)
        app = GestionProveedores(proveedores_root)
        proveedores_root.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(proveedores_root))

    def abrir_reportes(self):
        # Abrir la ventana de gestión de reportes
        self.root.withdraw()
        reportes_root = tk.Toplevel(self.root)
        app = GestionReporte(reportes_root)
        reportes_root.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(reportes_root))

    def confirmar_salida(self):
        # Confirmar la salida de la aplicación
        respuesta = messagebox.askyesno("Confirmación", "¿Estás seguro de que deseas salir?")
        if respuesta:
            self.root.quit()

if __name__ == "__main__":
    # Inicializar la aplicación principal
    root = tk.Tk()
    app = MenuPrincipal(root)
    root.mainloop()
