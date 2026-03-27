import csv
from services import userInput
inventory = [{"name": 'LIMONADA', "price": '100', "quantity": '2'},{"name": 'TELEFONO', "price": '2000', "quantity": '4'}]

def save_csv(inventory, route, include_header=True):
    import os
    file_exists = os.path.isfile(route)
    
    try:
        if inventory == []:
            print('The inventory is empty')
            return
        
        with open(route, 'a', newline='') as f:
            writer = csv.writer(f, delimiter=',')

            if not file_exists and include_header:
                writer.writerow(['Name', 'Price', 'Quantity'])
            
            for product in inventory:
                    writer.writerow([product['name'],product['price'],product['quantity']])
                    
                    
    except PermissionError:
        print('You do not have permissions for this file.')
        return
    except Exception as e:
        print(f'Error saving file: {e}')
    print(f'Inventory stored in: {route}')

def overwrite_csv(inventory, route, include_header=True):
    
    import os
    file_exists = os.path.isfile(route)
    written_rows = 0
    
    try:
        if inventory == []:
            print('The inventory is empty')
            return
        
        with open(route, 'w', newline='') as f:
            writer = csv.writer(f, delimiter=',')

            if include_header:
                writer.writerow(['Name', 'Price', 'Quantity'])
            
            for product in inventory:
                    writer.writerow([product['name'],product['price'],product['quantity']])
                    written_rows += 1
                    
    except PermissionError:
        print('You do not have permissions for this file.')
        return
    except Exception as e:
        print(f'Error saving file: {e}')
    print(f'Inventory stored in: {route}')          

def fuse_CSV(inventory,route):
    product = {
            "name": str,
            "price": float,
            "quantity": int
        }
    products = []
        
    with open(route, 'r+', newline='') as f:
        reader = csv.reader(f, delimiter = ',')
        next(reader)
        db = list(reader)
        
        for i in range(len(db)):
            product['name'] = db[i][0]
            product['price'] = db[i][1]   
            product['quantity'] = db[i][2]
            for i in range(len(inventory)): 
                if product['name'] == inventory[i]['name']:
                    product['price'] = inventory[i]['price']
                    product['quantity'] = int(product['quantity']) + int(inventory[i]['quantity'])
            products.append(product.copy())
            
    save_csv(products,'semana_3/db.csv',True)

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
                
                print(f'{product['name']} | {product['price']} | {product['quantity']}')
                
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
            overwrite_csv(products,'semana_3/db.csv',True)
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