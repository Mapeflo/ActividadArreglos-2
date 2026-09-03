matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz 3x3 inicializada con valores del 1 al 9:")
print()

for fila in matriz:
    for elemento in fila:
        print(elemento, end="\t")
    print()