import json

class Cliente:
    def __init__(self, usuario, contrasena, nombre, apellido):
        self.usuario = usuario
        self.contrasena = contrasena
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nUsuario: {self.usuario}"

    def cargar_usuarios():
        try:
            with open("usuarios.json", "r") as archivo:
                usuarios = json.load(archivo)
        except FileNotFoundError:
            usuarios = {}
        
        return usuarios

    def guardar_usuarios(usuarios):
        with open("usuarios.json", "w") as archivo:
            json.dump(usuarios, archivo)

    def registro(self):
        # Solicitar al usuario que ingrese un nombre de usuario, contraseña, nombre y apellido
        self.usuario
        self.contrasena
        self.nombre
        self.apellido
        
        # Cargar usuarios existentes desde el archivo JSON
        usuarios = Cliente.cargar_usuarios()
        
        # Verificar si el usuario ya existe
        if self.usuario in usuarios:
            print("El usuario ya está registrado.")
        else:
            # Agregar el usuario y la contraseña al diccionario de usuarios
            usuarios[self.usuario] = self.contrasena
            Cliente.guardar_usuarios(usuarios)
            print(f"Registro exitoso, bienvenido {self.usuario}.")

    def login(self):
        # Solicitar al usuario que ingrese su nombre de usuario y contraseña
        self.usuario
        self.contrasena
        
        # Cargar usuarios existentes desde el archivo JSON
        usuarios = Cliente.cargar_usuarios()
        
        # Verificar si el usuario y la contraseña coinciden
        if self.usuario in usuarios and usuarios[self.usuario] == self.contrasena:
            print(f"Bienvenido, {self.usuario}!")
        else:
            print("Usuario no encontrado. Por favor, regístrese.")