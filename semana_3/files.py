import csv
from services import userInput

# Function to save the CSV using Append mode. It creates the file with its headers if they do not already exist.It contains simple error
# handling and permissions management. Receive an inventory list created with the menu options
def save_CSV(inventory, route, include_header=True):
    import os
    file_exists = os.path.isfile(route)
    
    try:
        if inventory == []:
            print('The inventory is empty')
            return
        
        with open(route, 'r+', newline='') as f:
            writer = csv.writer(f, delimiter=',')
            reader = csv.reader(f, delimiter=',')
            db = list(reader)
            print(db)
            if not file_exists and include_header:
                writer.writerow(['name', 'price', 'quantity'])
            
            for product in inventory:
                writer.writerow([product['name'],product['price'],product['quantity']])
                    
    except PermissionError:
        print('You do not have permissions for this file.')
        return
    except Exception as e:
        print(f'Error saving file: {e}')
    print(f'Inventory stored in: {route}')

# This function completely overwrites the current CSV file, without preserving any previous data.
def overwrite_CSV(inventory, route, include_header=True):
    
    written_rows = 0
    
    try:
        if inventory == []:
            print('The inventory is empty')
            return
        
        with open(route, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')

            if include_header:
                writer.writerow(['name', 'price', 'quantity'])
            print(inventory)
            for product in inventory:
                    writer.writerow([product['name'],product['price'],product['quantity']])
                    written_rows += 1
                    
    except PermissionError:
        print('You do not have permissions for this file.')
        return
    except Exception as e:
        print(f'Error saving file: {e}')
    print(f'Inventory stored in: {route}')          

# This function merges the user-supplied CSV file with the existing one.
# It adds new products, increments the quantity of duplicates, and updates the price.
def fuse_CSV(inventory,route):
    repeated = []
        
    with open(route, 'r+', newline='') as f:
        reader = csv.DictReader(f, delimiter = ',')
        db = list(reader)
        
        # It iterates through each item in the database and updates the price and quantity if they are repeated.
        for item in db:
            for x in range(len(inventory)):
                print(item)
                if item['name'] == inventory[x]['name']:
                    item['price'] = inventory[x]['price']
                    item['quantity'] = int(item['quantity']) + int(inventory[x]['quantity'])
                    repeated.append(item['name'])
        
        # Change the name of each item found in the current database to null. 
        # This is done to differentiate them from those that have not been registered in the database.
        for new_item in inventory:
            for repeated_data in repeated:
                if new_item['name'] == repeated_data:
                    new_item['name'] = 'null'

        # Check if the object has a null value; if it does, it is ignored; if not, it is added to the database.
        for new_item in inventory:
            if new_item['name'] != 'null':
                db.append({'name': new_item['name'], 'price': new_item['price'], 'quantity': new_item['quantity']})     
        
        #The new, modified database is assigned to the overwrite function so that it replaces the old database.    
        overwrite_CSV(db, 'semana_3/db.csv',True)  
    
# This function loads a CSV file provided by the user. And it asks the user if they want
# to overwrite the current CSV file with the loaded one or merge them.
def load_CSV(route):

    try:
        product = {
            "name": str,
            "price": float,
            "quantity": int
        }
        products = []
        import os
        file_exists = os.path.isfile(route)
        error_rows = 0
        
        if not file_exists:
            raise FileNotFoundError
        
        with open(route, 'r', newline='') as f:
            reader = csv.reader(f, delimiter=',')
            next(reader)
            db = list(reader)
        
        loaded_products = 0
        
        print(f'\nName | Price | Quantity')
        for i in range(len(db)): 
            try:  
                product['name'] = db[i][0]
                product['price'] = db[i][1]
                product['quantity'] = db[i][2]
                products.append(product.copy())
                loaded_products += 1
                
                if int(product['quantity']) < 0 or float(product['price']) < 1:
                    raise ValueError
                
                print(f"{product['name']} | {product['price']} | {product['quantity']}")
                
            except ValueError:
                    error_rows += 1
        
    except FileNotFoundError:
        print('File not found')
        return
    except UnicodeDecodeError:
        print(f'Error: The {route} file is in an incorrect format')
        print('Make sure its saved in UTF-8')
        return
    
    running = True
    while running:
        overwrite = userInput('What action do you want to perform?\n1. Overwrite CSV\n2. Merge CSV\n\n','int','Please choose a valid option (1) (2)')
        if overwrite == 1:
            overwrite_CSV(products,'semana_3/db.csv',True)
            action = 'overwrite'
            running = False
        elif overwrite == 2:
            fuse_CSV(products,'semana_3/db.csv')
            running = False
            action = 'fusion'
        else:
            print('Please choose a valid option (1) (2)')
        
    print(f'We omitted {error_rows} rows that contained an error')
    print(f'Action: {action}')
