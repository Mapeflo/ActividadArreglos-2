import random

arreglo = [random.randint(1, 100) for _ in range(10)]

print("Arreglo original:")
print(arreglo)
print()

for i in range(len(arreglo)):
    if arreglo[i] % 2 != 0:      
        arreglo[i] = 0

print("Después de cambiar los impares por 0:")
print(arreglo)
print()

for i in range(len(arreglo)):
    arreglo[i] = arreglo[i] * i

print("Después de multiplicar cada valor por su índice:")
print(arreglo)