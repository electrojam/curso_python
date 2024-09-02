# Ejemplo de iterador

#Crear una lista
my_list = [1,2,3,4]

#Obtener el iterador
my_iter = iter(my_list)

#Usar el iterador
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
#print(next(my_iter))


# Crear un iterador para los numeros impares

#Limite
limit = 10

#Crear iterador
odd_itter = iter(range(1,limit+1,2))

#Usar el iterador
for num in odd_itter:
    print(num)


# Iterar en cadenas
#Creando la cadena
text = "Hola mundo"
#Creando el iterador
iter_text = iter(text)

#Iterar en la cadena
for char in iter_text:
    print(char)

######## Generador simple

def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print("\n",value)


# FIBONACCI
# 0 1 1 2 3 5 8 13 21
def fibo(max):
    a, b= 0, 1
    # a = 0
    # b = 1
    while a < max:
        yield a
        a, b = b, a + b
        # a = b
        # b = a + b
for num in fibo(10):
    print(num)