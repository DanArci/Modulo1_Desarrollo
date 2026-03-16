#Definiciond de las variables esenciales para el programa
nombre = ""
precio = 0,0
cantidad = 0

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

#Solicitar datos al usuario
nombre = inputUsuario("Coloque el nombre del producto: ","word","No se admiten signos, espacios o numeros. Vuelva a introducir el nombre del producto: ").upper()
precio = inputUsuario("Coloque el precio del producto: ","float","No se admiten signos, espacios o letras. Vuelva a introducir el precio del producto: ")
cantidad = inputUsuario(f"Coloque la cantidad de {nombre} que llevara: ","int",f"No se admiten signos, espacios o letras. Vuelva a introducir la cantidad de {nombre} que llevara: ")
#Calcular el costo total de la compra
costo_total = precio * cantidad
#Mostrar el resumen de la compra
print(f"Producto: {nombre} | Precio: {precio} | Cantidad: {cantidad} | Total: {costo_total}")

#Este programa se encarga de pedirle al usuario 3 datos; El nombre; El precio; La cantidad de un producto para posteriormente calcular el costo total
# de la compra de este producto. Y para finalizar le muestra un resumen de la compra al usuario.