class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años de edad")

person1 = Person("Esneider", 40)
person2 = Person("Bryan", 36)

person1.greet()
person2.greet()