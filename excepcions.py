try:
    divisor = int(input("Porfavor Ingresa un número divisor: "))
    result = 100/divisor
    print(result)
except ZeroDivisionError as e:
    print("Error: El divisor no puede ser igual a cero")
    print("Ha ocurrido el siguiente error: ", e)
except ValueError as e:
    print("Debes digitar un número válido.")
    print("Ha ocurrido el siguiente error: ", e)