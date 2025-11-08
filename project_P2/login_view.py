# -----------------------------------------------------------
# Archivo: login_view.py
# Función: Ventana de inicio de sesión (Tkinter)
# -----------------------------------------------------------
import tkinter as tk
from tkinter import messagebox
from auth_controller import validar_credenciales
from dashboard_view import DashboardApp  # Se abre después del login

class LoginApp:
    def __init__(self):
        # Crear ventana principal
        self.root = tk.Tk()
        self.root.title("Login - Sistema Administrativo")
        self.root.geometry("350x200")
        self.root.resizable(False, False)

        # Etiqueta y campo de usuario
        tk.Label(self.root, text="Usuario:").pack(pady=(20,5))
        self.usuario_entry = tk.Entry(self.root)
        self.usuario_entry.pack()

        # Etiqueta y campo de contraseña
        tk.Label(self.root, text="Contraseña:").pack(pady=(10,5))
        self.password_entry = tk.Entry(self.root, show='*')
        self.password_entry.pack()

        # Botón para iniciar sesión
        tk.Button(self.root, text="Ingresar", command=self.login).pack(pady=15)

    def login(self):
        """Verifica credenciales y abre el menú principal si son correctas."""
        usuario = self.usuario_entry.get().strip()
        password = self.password_entry.get().strip()

        if not usuario or not password:
            messagebox.showerror("Error", "Por favor completa todos los campos.")
            return

        valido = validar_credenciales(usuario, password)
        if valido:
            messagebox.showinfo("Éxito", f"Bienvenido {usuario}")
            self.root.destroy()  # Cierra ventana de login
            DashboardApp(usuario).run()  # Abre el dashboard
        else:
            messagebox.showerror("Error", "Credenciales incorrectas.")

    def run(self):
        """Mantiene la ventana abierta."""
        self.root.mainloop()

if __name__ == '__main__':
    LoginApp().run()
