to_do = [
    "Dirigirnos al hotel",
    "Ir a cenar",
    "Visitar playa",
    "dormir"
]

print(to_do)
numbers = [1,2,3,4,"cinco"]
print(type(numbers))
mix = ["uno", 2, 3.20, True, [5,6,7]]
print(mix)
print(len(mix))
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print("Último elemento", mix[-1])
string = "Hola mundo"
print("Primer elemento", string[0])
print("Segundo elemento", string[1])
print("Último elemento", string[-1])
print(mix[0:2])
print(mix[2:-2])

mix.append(False)
print(mix)
mix.append(["a", "b"])
print(mix)
mix.insert(1, ["a", "b"])
print(mix)
numbers = [1,2,10,90.45,3,4,5]
print("Mayor: ", max(numbers))
print("Min: ", min(numbers))
del numbers[-1]
print(numbers)
del numbers
print(numbers)
