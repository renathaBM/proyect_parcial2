# -----------------------------------------------------------
# Archivo: user_view.py
# Función: Interfaz Tkinter del CRUD de usuarios
# -----------------------------------------------------------
import tkinter as tk
from tkinter import ttk, messagebox
from user_controlller import obtener_usuarios, agregar_usuario, actualizar_usuario, eliminar_usuario

class UserApp:
    def __init__(self, logged_user):
        self.logged_user = logged_user
        self.root = tk.Tk()
        self.root.title(f"Gestión de Usuarios - Sesión: {logged_user}")
        self.root.geometry("700x450")
        self.root.resizable(False, False)
        self.crear_widgets()
        self.cargar_usuarios()

    def crear_widgets(self):
        """Crea los elementos gráficos de la ventana."""
        frame = tk.Frame(self.root, padx=10, pady=10)
        frame.pack(fill='both', expand=True)

        # Campos de texto
        tk.Label(frame, text="ID:").grid(row=0, column=0)
        self.id_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.id_var, state="readonly", width=10).grid(row=0, column=1, padx=5)

        tk.Label(frame, text="Usuario:").grid(row=0, column=2)
        self.usuario_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.usuario_var, width=25).grid(row=0, column=3, padx=5)

        tk.Label(frame, text="Contraseña:").grid(row=1, column=2)
        self.pass_var = tk.StringVar()
        tk.Entry(frame, textvariable=self.pass_var, show="*", width=25).grid(row=1, column=3, padx=5)

        # Botones CRUD
        botones = tk.Frame(frame)
        botones.grid(row=2, column=0, columnspan=4, pady=10)
        tk.Button(botones, text="Agregar", command=self.agregar_usuario).pack(side="left", padx=5)
        tk.Button(botones, text="Actualizar", command=self.actualizar_usuario).pack(side="left", padx=5)
        tk.Button(botones, text="Eliminar", command=self.eliminar_usuario).pack(side="left", padx=5)
        tk.Button(botones, text="Limpiar", command=self.limpiar_campos).pack(side="left", padx=5)

        # Tabla
        self.tree = ttk.Treeview(frame, columns=("ID","Usuario","Contraseña"), show="headings")
        for col in ("ID","Usuario","Contraseña"):
            self.tree.heading(col, text=col)
        self.tree.bind("<<TreeviewSelect>>", self.seleccionar_usuario)
        self.tree.grid(row=3, column=0, columnspan=4, sticky="nsew")

    def cargar_usuarios(self):
        """Carga todos los usuarios en la tabla."""
        for row in self.tree.get_children():
            self.tree.delete(row)
        for u in obtener_usuarios():
            self.tree.insert("", "end", values=u)

    def seleccionar_usuario(self, event):
        """Carga los datos seleccionados en los campos."""
        sel = self.tree.selection()
        if not sel: return
        vals = self.tree.item(sel[0])["values"]
        self.id_var.set(vals[0])
        self.usuario_var.set(vals[1])
        self.pass_var.set(vals[2])

    def agregar_usuario(self):
        """Agrega un nuevo usuario."""
        usuario = self.usuario_var.get().strip()
        password = self.pass_var.get().strip()
        ok, msg = agregar_usuario(usuario, password)
        messagebox.showinfo("Resultado", msg)
        if ok: self.cargar_usuarios(); self.limpiar_campos()

    def actualizar_usuario(self):
        """Actualiza usuario seleccionado."""
        idu = self.id_var.get().strip()
        usuario = self.usuario_var.get().strip()
        password = self.pass_var.get().strip()
        ok, msg = actualizar_usuario(idu, usuario, password)
        messagebox.showinfo("Resultado", msg)
        if ok: self.cargar_usuarios(); self.limpiar_campos()

    def eliminar_usuario(self):
        """Elimina usuario seleccionado."""
        idu = self.id_var.get().strip()
        if not idu: return messagebox.showerror("Error", "Selecciona un usuario")
        if messagebox.askyesno("Confirmar", "¿Eliminar usuario?"):
            ok, msg = eliminar_usuario(idu)
            messagebox.showinfo("Resultado", msg)
            if ok: self.cargar_usuarios(); self.limpiar_campos()

    def limpiar_campos(self):
        """Limpia los campos."""
        self.id_var.set(""); self.usuario_var.set(""); self.pass_var.set("")

    def run(self):
        self.root.mainloop()
