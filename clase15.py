squares = [x**2 for x in range(1,11)] #itere x en el rango 1 hasta 11
print("Cuadrados:", squares)

celsius = [0, 10, 20, 30, 40]
fahrenheit = [(temp * 9/5) *32 for temp in celsius] #itere temp en el rango de valores celsius
print("Temperatura en F:", fahrenheit)

#Numeros pares
evens = [x for x in range(1,21) if x%2 ==0] #itere o recorra x en el rango 1 hasta 21, para números pares de x x%3==0
print(evens)

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix)
#print(transposed)

transposed = []
for i in range(len(matrix[0])):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(transposed)