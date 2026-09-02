import random

arreglo = [0] * 10

for i in range(10):
    arreglo[i] = random.randint(1, 100)

print("Arreglo de 10 enteros con valores aleatorios:")
print(arreglo)