from modulo_cliente import Cliente
from modulo_productos import Producto, CategoriaAlimento, CategoriaElectronica

usuario_autenticado = False

# Menú principal
while True:
    print("1. Registro")
    print("2. Login")
    print("3. Agregue producto a la tienda alimentos")
    print("4. Agregue producto a la tienda electronica")
    print("5. Tienda alimentos")
    print("6. Tienda electronica")
    print("7. Salir")
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
            producto = input("Ingrese el alimento que desee agregar a la tienda: ")
            precio = input("Ingrese el precio del alimento: ")
            alimentos = CategoriaAlimento("Alimentos")
            alimentos.agregar_producto(Producto(producto, precio))
            alimentos.guardar_en_json("alimentos.json")
    elif opcion == "4":
        # Opción de agregar tecnologia a la tienda de electronica, solo si el usuario esta logueado
        if not usuario_autenticado:
            print("Inicie sesión o registrese")
        else:
            producto = input("Ingrese la tecnologia que desee agregar a la tienda: ")
            precio = input("Ingrese el precio de la tecnologia: ")
            electronica = CategoriaElectronica("Electronica")
            electronica.agregar_producto(Producto(producto, precio))
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
        # Opción de salida
        print("¡Hasta luego!")
        break  # Salir del bucle
    else:
        # En caso de que eligan alguna opción fuera del bucle while
        print("Opción inválida. Por favor, ingrese una opción válida.")