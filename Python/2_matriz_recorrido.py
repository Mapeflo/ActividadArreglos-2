matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz en forma de tabla:")
print()

for fila in matriz:
    for elemento in fila:
        print(elemento, end="\t")
    print()

print()

print("Recorrido por columnas:")
print()

for j in range(len(matriz[0])):          
    print(f"Columna {j}: ", end="")
    for i in range(len(matriz)):        
        print(matriz[i][j], end=" ")
    print()