# reto cumplido
class Vehiculo:
    def __init__(self, marca, modelo, precio) -> None:
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.disponible = True

    def vender(self):
        if self.disponible:
            self.disponible = False
            print(f'El vehículo {self.marca} {self.modelo} ha sido vendido.')
        else:
            print(f'El vehículo {self.marca} {self.modelo} no está disponible.')
    
    def verificar_disponibilidad(self):
        return self.disponible

    def obtener_precio(self):
        return self.precio
    
    def iniciar_motor(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase") #levantamos excepción

    def parar_motor(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
class Carro(Vehiculo): # class Carro hereda de la super clase o padre Vehiculo
        def iniciar_motor(self):
            if not self.disponible:
                return f"El motor del auto {self.marca} está en marcha."
            else:
                return f"El auto {self.marca} no está disponible."
            
        def parar_motor(self):
            if self.disponible:
                return f"El motor del coche {self.marca} se ha detenido."
            else:
                return f"El auto {self.marca} no está disponble."


class Cliente:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.vehiculos_comprados = []

    def comprar_vehiculo(self, vehiculo):
        if vehiculo.verificar_disponibilidad():
            vehiculo.vender()
            self.vehiculos_comprados.append(vehiculo)
        else:
            print(f'El vehículo {vehiculo.marca} {vehiculo.modelo} no está disponible.')
    
    def consultar_vehiculo(self, vehiculo):
        disponibilidad = "disponible" if vehiculo.verificar_disponibilidad() else "no disponible"
        print(f"El vehículo {vehiculo.marca} {vehiculo.modelo} está {disponibilidad} y cuesta {vehiculo.precio}")


class Concesionaria:
    def __init__(self) -> None:
        self.vehiculos = []
        self.clientes = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)
        print(f'El vehículo {vehiculo.marca} {vehiculo.modelo} ha sido agregado al inventario.')

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f'El cliente {cliente.nombre} ha sido registrado.')

    def mostrar_vehiculos_disponibles(self):
        print('Vehículos disponibles en la concesionaria:')
        for vehiculo in self.vehiculos:
            if vehiculo.verificar_disponibilidad():
                print(f"- {vehiculo.marca} {vehiculo.modelo} por ${vehiculo.obtener_precio()}")

# Crear vehículos
vehiculo1 = Vehiculo("Toyota", "Corolla", 20000)
vehiculo2 = Vehiculo("Ford", "Fiesta", 15000)
vehiculo3 = Vehiculo("Honda", "Civic", 22000)
vehiculo4 = Vehiculo("Chevrolet", "Cruze", 18000)

# Crear clientes
cliente1 = Cliente("Juan")
cliente2 = Cliente("Ana")
cliente3 = Cliente("Carlos")

# Crear concesionaria
concesionaria = Concesionaria()
concesionaria.agregar_vehiculo(vehiculo1)
concesionaria.agregar_vehiculo(vehiculo2)
concesionaria.agregar_vehiculo(vehiculo3)
concesionaria.agregar_vehiculo(vehiculo4)
concesionaria.registrar_cliente(cliente1)
concesionaria.registrar_cliente(cliente2)
concesionaria.registrar_cliente(cliente3)

# Mostrar vehículos disponibles
concesionaria.mostrar_vehiculos_disponibles()

# Cliente consulta un coche
cliente1.consultar_vehiculo(vehiculo2)

# Realizar compras
cliente1.comprar_vehiculo(vehiculo1)
cliente2.comprar_vehiculo(vehiculo3)
cliente3.comprar_vehiculo(vehiculo2)

# Mostrar vehículos disponibles después de las compras
concesionaria.mostrar_vehiculos_disponibles()

# Cliente intenta comprar un vehículo ya vendido
cliente3.comprar_vehiculo(vehiculo1)