vehiculos = []

def validar_patente(patente):
    if len(patente) != 6:
        return False
    letras = patente[:4]
    numeros = patente[4:]
    if not letras.isalpha() or not numeros.isdigit():
        return False
    return True

def validar_marca(marca):
    if len(marca) < 2 or len(marca) > 15:
        return False
    return True

def agregar_vehiculo():
    vehiculo = {}
    vehiculo["tipo"] = input ("\nIngrese el tipo de vehiculo (4 letras y 2 numeros): ")
    while True:
        patente = input("Ingrese la patente del vehiculo: ")
        if validar_patente(patente):
            vehiculo["patente"] = patente
            break
        else:
            print("La patente no cumple con el formato requerido. Intente nuevamente.")
    while True:
        marca = input("Ingrese la marca de su vehiculo (entre 2 y 15 caracteres): ")
        if validar_marca(marca):
            vehiculo["marca"] = marca
            break
        else: 
            print("La marca no cumple con la longitud requerida. Intente Nuevamente.")
    while True:
        precio = float(input("Ingrese el precio del vehiculo (debe ser mayor a $5.000.000): "))
        if precio > 5000000:
            vehiculo["precio"] = precio
            break
        else: 
            print("El precio debe ser mayor a $5.000.000. Intente Nuevamente.")
    vehiculo["precio"] = float(input("Ingrese el precio de su vehiculo: $"))
    vehiculo["multas"] = []
    vehiculo["fecha_registro"] = input("Ingrese la fecha de resgistro del vehiculo: ")
    vehiculo["nombre_dueño"] = input("Ingrese el nombre del dueño del vehiculo: ")
    vehiculos.append(vehiculo)
    print("vehiculo agregado correctamete.")

def agregar_multa(patente):
    for vehiculo in vehiculos:
        if vehiculo["patente"] == patente:
            multa = {}
            multa["monto"] = float(input("Ingrese el monto de la multa: "))
            multa["fecha"] = input("Ingrese la fecha de la multa: ")
            vehiculo["multas"].append(multa)
            print("Multa agregada correctamente.")
            return
    print("No se encontro un vehiculo con esa patente.")

def buscar_vehiculo(patente):
    for vehiculo in vehiculos:
        if vehiculo["patente"] == patente:
            print("Informacion del vehiculo: ")
            print(f"Tipo: {vehiculo['tipo']} ")
            print(f"Patente: {vehiculo['patente']}")
            print(f"Marca {vehiculo['marca']}")
            print(f"Precio: {vehiculo['precio']}")
            print(f"Fecha de resgistro: {vehiculo['fecha_registro']}")
            print(f"Nombre del dueño: {vehiculo['nombre_dueno']}")
            print("Multas")
            if vehiculo['multas']:
                for multa in vehiculo['multas']:
                    print(f"Monto: {multa['monto']}")
                    print(f"Fecha: {multa['fecha']}")
            else:
                print("No se registran multas para este vehiculo.")
            return
        
def imprimir_certificado_emision_contaminantes(patente):
    for vehiculo in vehiculos:
        if vehiculo['patente'] == patente:
            print("Certificado de emision de contaminantes")
            print(f"Patente del vehiculo_ {vehiculo[patente]}")
            print(f"Nombre del sueño: {vehiculo['nombre_dueno']}")
            return
    print("No se encontro vehiculo con esa patente.")

def imprimir_certificado_anotaciones_vigentes(patente):
    for vehiculo in vehiculos:
        if vehiculo['patente'] == patente:
            print("Certificado de Anotaciones Vigentes")
            print(f"Patente del vehiculo: {vehiculo[patente]})")
            print(f"Nombre del sueño: {vehiculo['nombre_dueno']})")
            return
    print("No se encontrovehiculo con esa patente.")

while True:
    print("\nOpcion 1: Registar vehiculo(tipo, patente, marca y precio, multas(monto y fecha), fecha de registro del vehiculo.)",
        "\nOpcion 2: Buscar el tipo de vehiculo",
        "\nOpcion 3: Imprimir Certificados",
        "\nOpcion 4: Salir")

    opc = int(input('ingrese una opc: >> '))


    if (opc == 1):
        agregar_vehiculo()
    elif (opc == 2):
        buscar_vehiculo()
    elif (opc == 3):
        imprimir_certificado_anotaciones_vigentes()
        imprimir_certificado_anotaciones_vigentes()
    elif (opc == 4):
        break
    else:
        print("Opcion no valida.")
        
        