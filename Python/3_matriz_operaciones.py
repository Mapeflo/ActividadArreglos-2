matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()

print("Matriz original:")
imprimir_matriz(matriz)
print()

suma = 0
for fila in matriz:
    for elemento in fila:
        suma += elemento

print(f"Suma de todos los elementos: {suma}")
print()

matriz[0], matriz[2] = matriz[2], matriz[0]

print("Matriz después de intercambiar la primera fila con la última:")
imprimir_matriz(matriz)