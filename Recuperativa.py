productos = []

def validar_producto(producto):
    if len(producto) <= 5:
        return False
    return True

def validar_parte(parte):
    if isinstance(parte, str):
        return True
    return False

def agregar_producto():
    producto = {}

    partes_ingresadas = 0
    partes_faltantes = float('inf')
    partes_registradas = []

    while True:
        parte = input("\nIngrese el MPN de su producto (Para finalizar introduzca 0): ")
        if parte == '0':
            break

        if validar_parte(parte):
            partes_registradas.append(parte)
            partes_ingresadas += 1
            partes_faltantes = max(10 - partes_ingresadas, 0)
            print(f"Faltan {partes_faltantes} partes.")
        else:
            print("El parte no cumple con el formato requerido. Intente nuevamente.")

    producto["partes"] = partes_registradas

    while True:
        modelo = input("\nIngrese el nombre del producto (mínimo 6 caracteres): ")
        if validar_producto(modelo):
            producto["modelo"] = modelo
            break
        else:
            print("El producto no cumple con el formato requerido. Intente nuevamente.")

    while True:
        try:
            precio = float(input("\nIngrese el precio del producto: $"))
            if precio > 0:
                producto["precio"] = f"${precio}"
                break
            else:
                print("El precio debe ser mayor a 0.")
        except ValueError:
            print("Debe ingresar un valor numérico válido para el precio.")

    descripcion = input("\nIngrese la descripción del producto: ")
    producto["descripcion"] = descripcion

    productos.append(producto)
    print("\nProducto registrado exitosamente:", producto)


def buscar_producto(partes_registradas):
    encontrado = False
    for producto in productos:
        if partes_registradas in producto["partes"]:
            if float(producto["precio"][1:]) >= 500:
                print("\nInformación del producto:")
                print(f"MPN: {producto['partes']}")
                print(f"Producto: {producto['modelo']}")
                print(f"Precio: {producto['precio']}")
                encontrado = True
            else:
                print("Producto sin stock")
            break

    else: 
        not encontrado
        print("No se encontró ningún producto con el número de parte especificado.")

def imprimir_reporte():
    print("\nReporte:")
    for producto in productos:
        print(f"\nNombre del producto: {producto['modelo']}")
        print(f"Número de parte: {producto['partes']}")
        print(f"Descripción del producto: {producto.get('descripcion', 'Sin descripción')}")
        print(f"Valor del producto: {producto['precio']}")

    if not productos:
        print("No hay productos registrados.")

while True:
    print("\nOpcion 1: Registrar producto",
          "\nOpcion 2: Buscar producto (por su número de parte)",
          "\nOpcion 3: Imprimir reporte (Producto, número de parte y descripción del producto junto al valor.)",
          "\nOpcion 4: Salir")
    try:
        opcion = int(input("\nIngrese una opción: >> "))
    except ValueError:
        print("Debe elegir una opción numérica")
        continue

    if opcion == 1:
        agregar_producto()

    elif opcion == 2:
        try:
            parte_buscar = input("\nIngrese el número de parte que desea buscar: ")
            buscar_producto(parte_buscar)
        except ValueError:
            print("Solo se aceptan dígitos numéricos")

    elif opcion == 3:
        imprimir_reporte()

    elif opcion == 4:
        print("\n¡Muchas Gracias!",
              "\n\nMatias Roa Mura",
              "\nVersion 1.0")
        break

    else:
        print("Opción no válida.")
