# Factorial
def factorial(n): # Factorial de n
    if n == 0:                          # este es nuestro caso base osea nuestro caso minimo o de origne 
        return 1                        # en este ejemplo no resta nada solo nos da un 1
    else:                               #este es nuestro caso recursuvi mientras no se cumpla el 0 seguiremos restando n-1
        return n * factorial(n - 1)     # en este ejemplo si tuvieramos n=5 seria sum_numbers(5-1) osea sum_numbers(4)

factorial_a = print(factorial(5))


# Fibonacci

def fibonacci(n):
    # Caso base: si n es 0, la suma es 0
    if n == 0:
        return 0
    # Caso recursivo: n + suma de (n-1)
    else:
        return n + fibonacci(n - 1)

# Llamada a la función
result = fibonacci(5)
print(f"Suma de los primeros 5 números es: {result}")