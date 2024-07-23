import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'app'))

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from menu import MenuPrincipal

# Diccionario de usuarios permitidos con sus contraseñas
usuarios_permitidos = {
    "Cristian Garcés": "12345",
    "Samuel Arrata": "6789",
    "Melanie Sánchez": "101112",
    "Jessica Manrique": "131415",
    "c": "c"  # Usuario con contraseña de un solo carácter para pruebas
}

class LoginApp:
    def __init__(self, root):
        self.root = root
        # Configuración inicial de la ventana principal
        self.root.title("Login - Ferretería Argamasa") # Nombre de pantalla y título empresa 
        self.root.geometry("800x600")  # Tamaño de la ventana
        self.root.resizable(False, False)  # Ventana no redimensionable
        self.root.iconbitmap("recursos/LOGO.ico")  # Icono de la ventana
        
        self.crear_canvas()  # Crea el lienzo donde se dibujarán las imágenes
        self.create_widgets()  # Crea los widgets de la interfaz
        self.cargar_imagen_fondo()  # Carga la imagen de fondo
        self.actualizar_imagen_fondo()  # Ajusta la imagen de fondo al tamaño de la ventana
        self.root.bind("<Configure>", self.actualizar_imagen_fondo)  # Actualiza la imagen de fondo cuando cambia el tamaño de la ventana

    def crear_canvas(self):
        # Crea un lienzo para dibujar sobre él
        self.canvas = tk.Canvas(self.root, width=800, height=600)
        self.canvas.grid(row=0, column=0, rowspan=4, columnspan=4, sticky="nsew")

    def cargar_imagen_fondo(self):
        try:
            # Intenta cargar la imagen de fondo
            self.bg_image = Image.open("recursos/FONDO.png")
            self.bg_photo = ImageTk.PhotoImage(self.bg_image)
            # Coloca la imagen de fondo en el lienzo
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo, tags="bg_image")
        except Exception as e:
            print(f"Error al cargar la imagen de fondo: {e}")  # Manejo de errores en caso de fallo

    def actualizar_imagen_fondo(self, event=None):
        # Actualiza la imagen de fondo cuando cambia el tamaño de la ventana
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        resized_image = self.bg_image.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(resized_image)
        
        self.canvas.delete("bg_image")  # Elimina la imagen de fondo antigua
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_photo, tags="bg_image")
        
        self.actualizar_imagen_centrada()  # Actualiza la imagen centrada

    def actualizar_imagen_centrada(self):
        try:
            # Intenta cargar y centrar la imagen del logo
            image_path = "recursos/ARGAMASA_logo.png"
            centered_image = Image.open(image_path)
            centered_photo = ImageTk.PhotoImage(centered_image)

            img_width, img_height = centered_image.size
            canvas_width = self.canvas.winfo_width()
            canvas_height = self.canvas.winfo_height()

            # Calcula la posición para centrar la imagen
            x = (canvas_width - img_width) // 2
            y = -200
            
            self.canvas.delete("centered_image")  # Elimina la imagen centrada antigua
            self.canvas.create_image(x, y, anchor=tk.NW, image=centered_photo, tags="centered_image")
            
            self.centered_photo = centered_photo  # Guarda una referencia a la imagen centrada

        except Exception as e:
            print(f"Error al cargar la imagen centrada: {e}")  # Manejo de errores en caso de fallo

    def create_widgets(self):
        # Crea los widgets de la interfaz gráfica
        tk.Label(self.root, text="Usuario:", font=("Verdana", 10, "bold")).place(x=250, y=300)
        self.entry_usuario = tk.Entry(self.root, font=("Courier New", 11, "bold"))
        self.entry_usuario.place(x=350, y=300)

        tk.Label(self.root, text="Contraseña:", font=("Verdana", 10, "bold")).place(x=250, y=340)
        self.entry_contrasena = tk.Entry(self.root, show="*", font=("Courier New", 11, "bold"))
        self.entry_contrasena.place(x=350, y=340)

        self.btn_login = tk.Button(self.root, text="Ingresar", command=self.verificar_login, width=20, height=2, font=("Arial", 12, "bold"), bg="#DCD2F0", cursor="hand2")
        self.btn_login.place(x=300, y=400)

    def verificar_login(self):
        # Verifica si el usuario y la contraseña son correctos
        usuario = self.entry_usuario.get()
        contrasena = self.entry_contrasena.get()

        if usuario in usuarios_permitidos and usuarios_permitidos[usuario] == contrasena:
            messagebox.showinfo("Login", "Ingreso exitoso")  # Mensaje de éxito
            self.root.destroy()  # Cierra la ventana de login
            self.iniciar_aplicacion_principal()  # Inicia el Menú principal
        else:
            messagebox.showerror("Login", "Usuario o contraseña incorrectos")  # Mensaje de error

    def iniciar_aplicacion_principal(self):
        # Avanza hacia el Menú principal
        root = tk.Tk()
        app = MenuPrincipal(root)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()
