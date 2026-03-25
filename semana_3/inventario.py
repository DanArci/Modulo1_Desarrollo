#Funcion que pide valores al usuario
def inputUsuario(mensaje,tipo,mensajeError):

    #Variable que rompe el ciclo
    terminar = False
    while terminar == False:
        try:
            #Si se necesita un numero entero
            if tipo == "int":
                number = int(input(mensaje))
                if number <= 0:
                    print("Por favor coloque un numero mayor a 0.")
                    continue 
                terminar = True
                return number
            #Si se necesita un numero decimal
            elif tipo == "float":
                number = float(input(mensaje))
                if number <= 0:
                    print("Por favor coloque un numero mayor a 0.")
                    continue 
                terminar = True
                return number
            #Si se necesita una palabra o una frase
            elif tipo == "word" or tipo == "phrase":
                word = str(input(mensaje))
                #Verifica que en el caso que sea una palabra, que no se acepten espacios ni signos
                if tipo == "word" and word.isalpha():
                    terminar = 1
                    return word
                elif tipo == "phrase":
                    return word
                else:
                    raise ValueError
        #Se hace un print del parametro mensaje de error pasado a la funcion en el caso de que exista algun error al convertir los valores
        except ValueError:
            print(mensajeError)
            continue

#Funcion de menu
def menu():
    #Mostramos el menu 
    print("\n" , "-"*23 , "Por favor selecciona una opcion " , "-"*22 , "\n1: Agregar producto\n2: Mostrar inventario\n3: Calcular estadísticas\n4: salir\n")

    #Pedimos la opcion elegida
    opcion = inputUsuario(f"{user}: ", "int","Coloque una opcion valida (1)(2)(3)(4)")
    return opcion

#Funcion de agregar un producto nuevo al inventario de ventas
def agregar_producto():

    #Se le piden los valores al usuario
    nombre = inputUsuario("Coloque el nombre del producto: ","word","No se admiten signos, espacios o numeros. Vuelva a introducir el nombre del producto: ").upper()
    precio = inputUsuario("Coloque el precio del producto: ","float","No se admiten signos, espacios o letras. Vuelva a introducir el precio del producto: ")
    cantidad = inputUsuario(f"Coloque la cantidad de {nombre} que llevara: ","int",f"No se admiten signos, espacios o letras. Vuelva a introducir la cantidad de {nombre} que llevara: ")
    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    
    #Se agregan los datos al registro
    inventario.append(producto.copy())
    print("\nRegistro exitoso")

#Funcion de mostrar el inventario
def mostrar_inventario():

    #Se imprime el registro por cada venta que haya en la lista de iventario
    for i in range(len(inventario)):
        costo_total = inventario[i]['precio'] * inventario[i]['cantidad']
        print(f"Producto: {inventario[i]['nombre']} | Precio: {inventario[i]['precio']} | Cantidad: {inventario[i]['cantidad']} | Total: {costo_total}") 

#Funcion de calcular estadisticas
def calcular_estadisticas():

    #Declaracion de variables
    costo_total = 0
    cantidad_total = 0

    #Ciclo for para calcular el costo total y la cantidad total vendida
    for i in range(len(inventario)):
        costo_total = costo_total + (inventario[i]['precio'] * inventario[i]['cantidad'])
        cantidad_total = cantidad_total + inventario[i]['cantidad']

    #Impresion de el costo total y la cantidad total de ventas del dia 
    print(f"\nEl total vendido en el dia fue de: {costo_total}\nLa cantidad de productos total vendida en el dia fue de: {cantidad_total}")

#Input para colocar el nombre del usuario
user = inputUsuario("Coloque su nombre: ","word","No se admiten signos, espacios o numeros. Vuelva a introducir su nombre")

#Definicion de las variables esenciales para el programa
nombre = ""
precio = 0,0
cantidad = 0

#Definicion de lista de inventario y diccionario de producto
inventario = []
producto = {
    "nombre": "",
    "precio": "",
    "cantidad": ""
}

#Declaracion de variable para el inicio del programa
opcion = 1

#Ciclo principal del programa
while opcion != 4:
    opcion = menu()
    if opcion == 1:
        agregar_producto()
    if opcion == 2: 
        mostrar_inventario()
    if opcion == 3:
        calcular_estadisticas()
    if opcion == 4: 
        print("Gracias por usar el programa")
    else:
        print("\nColoque una opcion valida")
        opcion = 1

#Esta semana nos encargamos de colocar la funcionalidad del menu de opciones, que nos permite entre 4 opciones: 1. agregar un producto; 2. mostrar el inventario;
# 3. calcular estadisticas; 4. salir.
# Ademas, segun la funcionalidad cada producto que se agrega se guarda en un diccionario dentro de una lista la cual se llama inventario. Esto nos permite obtener 
# un registro que se muestra con la opcion 2 y los calculos de costo total y cantidad total vendida en el dia con la opcion 3. La opcion 4 cierra el programa