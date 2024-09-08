import json

# Cargue y Lectura del archivo json
with open('products.json', mode='r') as file:
    products = json.load(file)

# Mostrar el contenido 
for product in products:
    print(product)

# Mostrar claves específicas
for product in products:
    print(f"Product: {product['name']}, Price: {product['price']}")