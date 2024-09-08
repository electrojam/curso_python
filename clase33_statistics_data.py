import statistics
import csv

# Leer los datos de ventas mensuales desde un archivo CSV
monthly_sales = {}
with open('monthly_sales.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales # Guardamos datos en forma de diccionario

sales = list(monthly_sales.values()) # Guardamos solo valores en formato lista
print(monthly_sales)
print(sales)

# hallar la media de los datos
mean_sales = statistics.mean(sales)
print(f"\nLa media es: {mean_sales}")

# hallar la mediana de los datos
median_sales = statistics.median(sales)
print(f"\nLa mediana es: {median_sales}")

# Hallar la moda de los datos
moda_sales = statistics.mode(sales)
print(f"\nLa moda es: {moda_sales}")

# Hallar la desviación estándar
stdev_sales = statistics.stdev(sales)
print(f"\nLa Desviación Estándar es: {stdev_sales}")

# Hallar la varianza
variance_sales = statistics.variance(sales)
print(f"\nLa Varianza es: {variance_sales}")

# Hallar ato máximo y mínimo
max_sales = max(sales)
min_sales = min(sales)

range = max_sales - min_sales
print(f"\nEl Rango de ventas es: {range}")

