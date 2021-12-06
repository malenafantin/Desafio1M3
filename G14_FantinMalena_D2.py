' ' ' Mi agenda telefonica de mis amigos ' ' '

telefonos = {
    "Andrea Gimenez": "3624567890",
    "Malena Fantin" : "3624565432",
    "mm": "54645476",
}

consultar = True

while consultar:
    print ()
    print ("MIS TELEFONOS")
    print ()
    print ("1- Crear un nuevo contacto ")
    print ("2- Buscar contacto con nombre completo")
    print ("3- Mostrar todos mis contactos")
    print ()

    opcion=int(input("Ingrese una opción: "))

    if(opcion==1):
        nombre=input("Ingrese el nombre: ")
        numero=input("Ingrese el Numero de telefono: ")
        
        telefonos[nombre]= numero
        print("El contacto se agrego a la lista con exito")
           
    if(opcion==2):
        nombre=input("Ingrese el nombre del contacto: ")
        if nombre not in telefonos.keys():
            print("No existe el contacto buscado")
        else:
            print(f"Contacto: {nombre} - Teléfono: {telefonos[nombre]}")
    if (opcion==3):
        print(telefonos)
