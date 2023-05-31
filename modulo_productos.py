import json

class Producto:
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def mostrar_informacion(self):
        print("ID:", self.id)
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "precio": self.precio
        }

    def from_dict(producto_dict):
        return Producto(producto_dict["id"], producto_dict["nombre"], producto_dict["precio"])


class CategoriaAlimento:
    def __init__(self, nombre_categoria):
        self.nombre_categoria = nombre_categoria
        self.productos = []  # Lista para almacenar los productos de la categoría

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Categoría:", self.nombre_categoria)
        print("Productos:")
        for producto in self.productos:
            producto.mostrar_informacion()
            print()

    def comprar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id == id_producto:
                self.productos.remove(producto)
                return producto
        return None

    def guardar_en_json(self, archivo):
        productos_dict = [producto.to_dict() for producto in self.productos]
        data = {
            "nombre_categoria": self.nombre_categoria,
            "productos": productos_dict
        }
        with open(archivo, "w") as file:
            json.dump(data, file, indent=4)

    def cargar_desde_json(self, archivo):
        with open(archivo, "r") as file:
            data = json.load(file)
        categoria = CategoriaAlimento(data["nombre_categoria"])
        for producto_dict in data["productos"]:
            producto = Producto.from_dict(producto_dict)
            categoria.agregar_producto(producto)
        return categoria


class CategoriaElectronica:
    def __init__(self, nombre_categoria):
        self.nombre_categoria = nombre_categoria
        self.productos = []  # Lista para almacenar los productos de la categoría

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Categoría:", self.nombre_categoria)
        print("Productos:")
        for producto in self.productos:
            producto.mostrar_informacion()
            print()

    def comprar_producto(self, nombre_producto):
        for producto in self.productos:
            if producto.nombre == nombre_producto:
                self.productos.remove(producto)
                return producto
        return None
    
    def guardar_en_json(self, archivo):
        productos_dict = [producto.to_dict() for producto in self.productos]
        data = {
            "nombre_categoria": self.nombre_categoria,
            "productos": productos_dict
        }
        with open(archivo, "w") as file:
            json.dump(data, file, indent=4)

    def cargar_desde_json(self, archivo):
        with open(archivo, "r") as file:
            data = json.load(file)
        categoria = CategoriaElectronica(data["nombre_categoria"])
        for producto_dict in data["productos"]:
            producto = Producto.from_dict(producto_dict)
            categoria.agregar_producto(producto)
        return categoria