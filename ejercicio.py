def validar_nombremascota(nombremascota):
    if nombremascota == "":
        return False
    else:
        return True
def validar_edadmascota(edadmascota):
    if edadmascota > 0:
        return True
    else:
        return False

def validar_pesomascota(pesomascota):
    if pesomascota > 0.0:
        return True
    else:
        return False

def mostrar_menu():
    print("===== MENU PRINCIPAL ======")
    print("1.- Agregar mascota")
    print("2.- Buscar mascota")
    print("3.- Eliminar mascota")
    print("4.- Actualizar estado")
    print("5.- Mostrar mascotas")
    print("6.- Salir")
    print("===============================")

def leer_opcion(opcion):
    try:
        opcion = int(input("Escoja una opción del 1 al 6 porfavor: "))
        if opcion <= 1 or opcion <= 6:
            return opcion
        else:
            print("Error,la opción debe ser entre 1 y 6.")
    except ValueError:
        print("Error, el valor ingresado debe ser un numero entero.")

def agregar_mascota(mascotas,mascota,pesomascota,edadmascota,nombremascota):
    mascotas = []
    nombremascota = input("Ingrese el nombre de la mascota por favor: ")
    while not validar_nombremascota(nombremascota):
        print("Error, el nombre no puede estar vacío.")
        nombremascota = input("Ingrese el nombre de la mascota por favor: ")
    pesomascota = float(input("Ingrese peso de la mascota por favor: "))
    while not validar_pesomascota(pesomascota):
        print("Error, el peso debe ser mayor a 0.")
        pesomascota = float(input("Ingrese peso de la mascota por favor: "))
    edadmascota = int(input("Ingrese edad de la mascota por favor:"))
    while not validar_edadmascota(edadmascota):
        print("Error, la edad debe ser mayor a 0.")
    edadmascota = int(input("Ingrese edad de la mascota por favor:"))
    mascota = {
        "Nombre de la mascota": nombremascota,
        "Peso de la mascota": pesomascota,
        "Edad de la mascota": edadmascota,
    }
    mascotas.append(mascota)
    print(f"Mascota: {nombremascota} agregada con éxito!")
def buscar_mascota(mascotaabuscar, mascotas):
    for i in range(len(mascotas)):
        if mascotas[i]["Nombre de la mascota"] == mascotaabuscar:
            return i
    return -1
def eliminar_mascota(mascotas):
    nombre_eliminar = input("Ingresa el nombre de la mascota que desea eliminar: ")
    posicion = buscar_mascota(mascotas,nombre_eliminar)
    if posicion != -1:
        mascotas.pop(posicion)
        print(f"La mascota '{nombre_eliminar} fue eliminado correctamente.")
    else:
        print(f"La mascota '{nombre_eliminar} no se encuentra registrado.")

def actualizar_estado(mascotas):
    for mascota in mascotas:
        if mascota["Peso de la mascota"] <= 15.0:
            mascota["adoptado"] = True
        else:
            mascota["adoptado"] = False

def mostrar_mascotas(mascotas):
    actualizar_estado(mascotas)
    print("\n=== LISTA DE MASCOTAS =====")
    if len(mascotas) == 0:
        print("No hay mascotas registradas")
        return 
    for mascota in mascotas:
        if mascota["adoptado"]:
            estado_texto = "ADOPTADO"
        else:
            estado_texto = "EN ADOPCIÓN"
            print("============= RESUMEN =============================================")
            print(f"Nombre de la mascota: {mascota['Nombre de la mascota']}")
            print(f"Peso de la mascota: {mascota['Peso de la mascota']}")
            print(f"Edad de la mascota: {mascota['Edad de la mascota']}")
            print("=====================================================================")
        print()

mascotas = []
opcion = 0
while opcion != 6:
    mostrar_menu()
    opcion = leer_opcion(opcion)
    if opcion == 1:
        agregar_mascota(mascotas)
    elif opcion == 2:
        nombre_buscar = input("Ingrese el nombre de la mascota a buscar: ")
        posicion = buscar_mascota(mascotas,nombre_buscar)
        if posicion != -1:
            print(f"\nMascota encontrada en la posición: {posicion}")
            print(f"Nombre: {mascotas[posicion]['Nombre de la mascota']}")
            print(f"Edad: {mascotas[posicion]['Edad de la mascota']}")
            print(f"Peso: {mascotas[posicion]['Peso de la mascota']}")
        else:
            print(f"\nLa mascota '{nombre_buscar}' no se encuentra registrada.")
    elif opcion == 3:
        eliminar_mascota(mascotas)
    elif opcion == 4:
        actualizar_estado(mascotas)
    elif opcion == 5:
        mostrar_mascotas(mascotas)
    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto")