def suma_pares_matriz(matriz):
    suma_pares = 0

    for fila in matriz:
        for elemento in fila:
            if elemento % 2 == 0:  # Verifica si el número es par
                suma_pares += elemento
    return suma_pares
    

if __name__ == "__main__":
    # Matrices de prueba
    matriz1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    matriz2 = [
        [10, 21, 32],
        [43, 54, 65],
        [76, 87, 98]
    ]
    
    matriz3 = [
        [0, -2, -4],
        [5, 6, 7],
        [8, 9, 10]
    ]
    matriz_un_par = [
    [1, 3, 5],
    [7, 9, 2],  # Solo el número 2 es par
    [13, 15, 17]
]
    
    print(suma_pares_matriz(matriz1))  # 20
    print(suma_pares_matriz(matriz2))  # 270
    print(suma_pares_matriz(matriz3))  # 18
    print(suma_pares_matriz(matriz_un_par))  # 2
