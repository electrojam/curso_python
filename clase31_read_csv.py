import csv

# Leer archivo csv y guardar en formato diccionario clave valor
with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        print(row)

# Mostrar la información por columnas de interés, solo algunas
with open('products.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        print(f"Prodcut: {row['name']}, Precio: {row['price']}")
