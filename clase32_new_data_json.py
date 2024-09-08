import json

file_path = 'products.json'

new_products = {
        "name": "Laptop",
        "price": 1200,
        "quantity": 4,
        "brand": "BrandName",
        "category": "Electronics",
        "entry_date": "2024-01-05"
    }


with open(file_path, mode='r') as file:
    products = json.load(file)

products.append(new_products)

with open(file_path, mode='w') as file:
    json.dump(products,file, indent=4)