import random

arreglo = [random.randint(1, 100) for _ in range(10)]

print("Arreglo generado:")
print(arreglo)
print()

valor_buscado = int(input("Ingrese el valor que desea buscar: "))

posicion = -1  

for i in range(len(arreglo)):
    if arreglo[i] == valor_buscado:
        posicion = i
        break  

if posicion != -1:
    print(f"El valor {valor_buscado} se encontró en la posición: {posicion}")
else:
    print(f"El valor {valor_buscado} NO se encuentra en el arreglo.")