import random

arreglo = [random.randint(1, 100) for _ in range(10)]

print("Arreglo original:")
print(arreglo)
print()

print("Recorrido con for clásico:")
for i in range(len(arreglo)):
    print(f"Índice {i} → valor: {arreglo[i]}")

print()

print("Recorrido con for-each:")
for valor in arreglo:
    print(valor, end=" ")
print()