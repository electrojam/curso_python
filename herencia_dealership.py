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

class Bicicleta(Vehiculo):
    def inicar_motor(self):
        if not self.disponible:
            return f"La bicicleta {self.marca} está en marcha"
        else:
            return f"La bibicleta {self.marca} No está disponible"
    
    def parar_motor(self):
        if self.disponible:
            return f"La bicicleta {self.marca} se ha detenido"
        else:
            return f"La bicicleta {self.marca} No está disponible"
        
class Camion(Vehiculo):
    def iniciar_motor(self):
        if not self.disponible:
            return f"El motor del camión {self.marca} está en marcha"
        else:
            return f"El camión {self.marca} no está disponible"
        
    def parar_motor(self):
        if self.disponible:
            return f"El motor del camión {self.marca} se ha detenido"
        else:
            return f"El camión {self.marca} no está disponible"
        
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculos_comprados = []

    def comprar_vehiculos(self, vehiculo: Vehiculo): # recibo parámetro de clase Vehiculo
        if vehiculo.verificar_disponibilidad(): #verificamos si vehículo está disponible
            vehiculo.vender() # vendemos el vehículo
            self.vehiculos_comprados.append(vehiculo) #añadimos objeto vehiculo a la colección
        else:
            print(f"El vehículo {vehiculo.marca} no está disponible")

    def consultar_vehiculo(self, vehiculo: Vehiculo):
        if vehiculo.verificar_disponibilidad():
            disponibilidad = "Disponible"
        else:
            disponibilidad = "No disponible"
        print(f"El {vehiculo.marca} está {disponibilidad} y tiene un valor de {vehiculo.obtener_precio()}")

class Concecionaria:
    def __init__(self):
        self.vehiculos = []
        self.clientes = []
    
    def agregar_vehiculo(self, vehiculo: Vehiculo):
        self.vehiculos.append(vehiculo)
        print(f"El vehículo {vehiculo.marca} ha sido añadido al inventario")
    
    def registrar_cliente(self, cliente: Cliente):
        self.clientes.append(cliente)
        print(f"El cliente {cliente.nombre} ha sido registrado")
    
    def mostrar_vehiculos_disponibles(self):
        print("Vehículos disponbiles en la tienda")
        for vehiculo in self.vehiculos:
            if vehiculo.verificar_disponibilidad():
                print(f"-- El vehículo {vehiculo.marca} {vehiculo.modelo} por {vehiculo.obtener_precio()}")

carro1 = Carro("Toyota", "Corolla", 20000)
bicicleta1 = Bicicleta("Yamaha", "MT-07", 7000)
camion1 = Camion("Volvo", "FH16", 80000)

cliente1 = Cliente("James")

concecionaria = Concecionaria()

concecionaria.agregar_vehiculo(carro1)
concecionaria.agregar_vehiculo(bicicleta1)
concecionaria.agregar_vehiculo(camion1)

# Mostrar vehículos disponibles
concecionaria.mostrar_vehiculos_disponibles()

# Cliente consulta un vehículo
cliente1.consultar_vehiculo(carro1)

# Cliente comprar un vehículo
cliente1.comprar_vehiculos