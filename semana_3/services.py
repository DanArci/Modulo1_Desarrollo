subtotal = (lambda p: p["price"] * p["quantity"])

def userInput(msg,type,errorMsg):
    terminate = False
    while terminate == False:
        try:
            if type == "int":
                number = int(input(msg))
                if number <= 0:
                    print("Please enter a number greater than 0")
                    continue 
                terminate = True
                return number
            elif type == "float":
                number = float(input(msg))
                if number <= 0:
                    print("Please enter a number greater than 0.")
                    continue 
                terminate = True
                return number
            elif type == "word" or type == "phrase":
                word = str(input(msg))
                if type == "word" and word.isalpha():
                    terminate = 1
                    return word
                elif type == "phrase":
                    return word
                else:
                    raise ValueError
        except ValueError:
            print(errorMsg)
            continue

def add_product(inventory):
    name = userInput("Enter the product name: ","word","Punctuation marks, spaces, or numbers are not allowed. Please re-enter the product name: ").upper()
    price = userInput("Enter the product price: ","float","Special characters, spaces, or letters are not allowed. Please re-enter the product price: ")
    quantity = userInput(f"Add the desired amount of {name}: ","int",f"No symbols, spaces, or letters are allowed. Please re-enter the quantity of {name} you will be taking: ")
    product = {"name": name, "price": price, "quantity": quantity}
    inventory.append(product.copy())
    print("\nSaved successfully")
    return inventory

def show_inventory(inventory):
    print('-'*70)
    for i in range(len(inventory)):
        total_cost = subtotal(inventory[i])
        print(f"Product: {inventory[i]['name']} | price: {inventory[i]['price']} | quantity: {inventory[i]['quantity']} | Total: {total_cost}")
    print('-'*70)

def search_product(inventory, name):
    for i in range(len(inventory)):
        names = list(inventory[i].values())
        if names[0] == name.upper().strip():
            print(f'Product: {names[0]} | price: {names[1]} | quantity: {names[2]} ')

def update_product(inventory, name, new_price=None, new_quantity=None):
    for i in range(len(inventory)):
        names = list(inventory[i].values())
        if names[0] == name.upper().strip():
            inventory[i]['price'] = new_price
            inventory[i]['quantity'] = new_quantity

def remove_product(inventory, name):
    for i in range(len(inventory)):
        names = list(inventory[i].values())
        if names[0] == name.upper().strip():
            inventory.pop(i)
            break

def calculate_statistics(inventory):
    total_cost = 0
    total_quantity = 0
    most_expensive_product = 0
    product_largest_quantity = 0
    for i in range(len(inventory)):
        total_cost = total_cost + (inventory[i]['price'] * inventory[i]['quantity'])
        total_quantity = total_quantity + inventory[i]['quantity']
        if inventory[i]['price'] > most_expensive_product:
            most_expensive_product = inventory[i]['price']
            most_expensive_product_msg = f"Most expensive product of the day: {inventory[i]['name']} | price: {inventory[i]['price']}."
        if inventory[i]['quantity'] > product_largest_quantity:
            product_largest_quantity = inventory[i]['quantity']
            product_largest_quantity_msg = f"Highest quantity sold on the day: {inventory[i]['name']} | quantity: {inventory[i]['quantity']}."
    print(f"\nThe total sold on the day was: {total_cost}\nThe total number of products sold on the day was: {total_quantity}\n{most_expensive_product_msg}\n{product_largest_quantity_msg}")


# add_product()
# add_product()
# show_inventory()
# print('-'*20)
# calculate_statistics(inventory)


#FALTAN LOS COMENTARIOS Y DOCSTRINGS