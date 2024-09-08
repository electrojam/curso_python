# Leer un archivo por línea
with open('caperucita.txt', 'r') as file:
    for lineas in file:
        print(lineas.strip())

# Leer todas las líneas y guardar en una lista
with open('caperucita.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# Añadir un texto nuevo
with open('caperucita.txt', 'a') as file:
    file.write('\n\nBy:ChatGPT')
'''
# Sobreescribir el texto
with open('caperucita.txt', 'w') as file:
    file.write('\n\nBy:ChatGPT')
'''
# Conteo de líneas de un texto
with open('caperucita.txt', 'r') as file:
    lines = file.readlines()

    n_lines = 0
    
    for line in lines:
        n_lines += 1
    
    print(n_lines)