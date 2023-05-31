from modulo_cliente import *
from modulo_productos import *

# Crear instancias de las categorías de alimentos y electrónica
alimentos = CategoriaAlimento("Alimentos")
electronica = CategoriaElectronica("Electrónica")

# Set de autenticación de usuario
usuario_autenticado = False

# Menú principal
while True:
    print("1. Registro")
    print("2. Login")
    print("3. Agregar producto a la tienda de alimentos")
    print("4. Agregar producto a la tienda de electrónica")
    print("5. Mostrar productos de la tienda de alimentos")
    print("6. Mostrar productos de la tienda de electrónica")
    print("7. Comprar alimento")
    print("8. Comprar electronica")
    print("9. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        # Opción de registro de usuario
        usuario = input("Ingrese un nombre de usuario: ")
        contrasena = input("Ingrese una contraseña: ")
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        cliente = Cliente(usuario, contrasena, nombre, apellido)
        cliente.registro()
    elif opcion == "2":
        # Opción de login de usuario
        usuario = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")
        cliente = Cliente(usuario, contrasena, "", "")
        cliente.login()
        usuario_autenticado = True
    elif opcion == "3":
        # Opción de agregar alimentos a la tienda de alimentos, solo si el usuario esta logueado
        if not usuario_autenticado:
            print("Inicie sesión o registrese")
        else:
            id = int(input("Ingrese el id del alimento: "))
            producto = input("Ingrese el alimento que desee agregar a la tienda: ")
            precio = input("Ingrese el precio del alimento: ")
            alimentos = CategoriaAlimento("Alimentos")
            alimentos.agregar_producto(Producto(id, producto, precio))
            alimentos.guardar_en_json("alimentos.json")
    elif opcion == "4":
        # Opción de agregar tecnologia a la tienda de electronica, solo si el usuario esta logueado
        if not usuario_autenticado:
            print("Inicie sesión o registrese")
        else:
            id = int(input("Ingrese el id de la electronica: "))
            producto = input("Ingrese la tecnologia que desee agregar a la tienda: ")
            precio = input("Ingrese el precio de la tecnologia: ")
            electronica = CategoriaElectronica("Electronica")
            electronica.agregar_producto(Producto(id, producto, precio))
            electronica.guardar_en_json("electronica.json")
    elif opcion == "5":
        # Opción para mostrar los alimentos de la tienda de alimentos
        alimentos.cargar_desde_json("alimentos.json")
        alimentos.mostrar_productos()
    elif opcion == "6":
        # Opción para mostrar la tecnologia de la tienda de electronica
        electronica.cargar_desde_json("electronica.json")
        electronica.mostrar_productos()
    elif opcion == "7":
        # Opción para comprar un alimento de la tienda de alimentos
        id = int(input("Ingrese el ID del alimento que desea comprar: "))
        if not usuario_autenticado:
            print("Inicie sesión o regístrese")
        else:
            producto_comprado = alimentos.comprar_producto(id)
            if producto_comprado is not None:
                print("Producto comprado:")
                producto_comprado.mostrar_informacion()
                alimentos.guardar_en_json("alimentos.json")
            else:
                print("El producto no está disponible.")
    elif opcion == "8":
        # Opción para comprar un producto de electrónica de la tienda de electrónica
        id = int(input("Ingrese el ID del producto de electrónica que desea comprar: "))
        if not usuario_autenticado:
            print("Inicie sesión o regístrese")
        else:
            producto_comprado = electronica.comprar_producto(id)
            if producto_comprado is not None:
                print("Producto comprado:")
                producto_comprado.mostrar_informacion()
                electronica.guardar_en_json("electronica.json")
            else:
                print("El producto no está disponible.")
    elif opcion == "9":
        # Opción de salida
        print("¡Hasta luego!")
        break  # Salir del bucle
    else:
        # En caso de que elijan alguna opción fuera del bucle while
        print("Opción inválida. Por favor, ingrese una opción válida.")