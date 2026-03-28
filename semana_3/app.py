from files import *
from services import *
inventory = []
products = {
    "name": str,
    "price": float,
    "quantity": int
}
opcion = 1

#Ciclo principal del programa
while opcion != 9:
    opcion = userInput('Choose the option to perform:\n1. Add product\n2. Show inventory\n3. Search product\n4. Update product\n5. Remove product\n6. Calculate statistics\n7. Save CSV\n8. Load CSV\n9. Exit\n','int','Please select a valid option. (1)(2)(3)(4)(5)(6)(7)(8)(9)')
    if opcion == 1:
        add_product(inventory)
    elif opcion == 2: 
        show_inventory(inventory)
    elif opcion == 3:
        search_product(inventory, userInput('Enter the name of the product you are searching for:\n','word','Only one word without punctuation marks is accepted.'))
    elif opcion == 4: 
        name = userInput('Enter the name of the product you are updating:\n','word','Only one word without punctuation marks is accepted.')
        new_price = userInput('Enter the new price of the product you are updating:\n','float','Only positive numbers are accepted.')
        new_quantity = userInput('Enter the new quantity of the product you are updating:\n','int','Only positive numbers are accepted.')
        update_product(inventory ,name ,new_price ,new_quantity)
    elif opcion == 5:
        remove_product(inventory, userInput('Enter the name of the product you are removing:\n','word','Only one word without punctuation marks is accepted.'))
    elif opcion == 6:
        calculate_statistics(inventory)
    elif opcion == 7:
        route = 'semana_3\db.csv'
        save_CSV(inventory, route, True)
        inventory.clear()
    elif opcion == 8:
        route = userInput('Enter the path to the CSV file you want to upload.','phrase','There was an error in the route.')
        load_CSV(route)
        inventory.clear()
    elif opcion == 9:
        print('Closing program...')
    else:
        print("\nPlease select a valid option. (1)(2)(3)(4)(5)(6)(7)(8)(9)")
        opcion = 1