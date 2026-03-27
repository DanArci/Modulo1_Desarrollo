from files import *
from services import *
opcion = 1

#Ciclo principal del programa
while opcion != 9:
    opcion = userInput()
    if opcion == 1:
        add_product()
    elif opcion == 2: 
        show_inventory()
    elif opcion == 3:
        search_product
    elif opcion == 4: 
        update_product()
    elif opcion == 5:
        remove_product()
    elif opcion == 6:
        calculate_statistics()
    elif opcion == 7:
        save_csv()
    elif opcion == 8:
        load_CSV()
    elif opcion == 9:
        print('Cerrando programa')
    else:
        print("\nColoque una opcion valida")
        opcion = 1
