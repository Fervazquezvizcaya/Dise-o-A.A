
def InicioFin(A, ele,):
    # Un arreglo A de elementos ordenados
    # El inicio y el fin de un arreglo A 
    inicio = 0
    fin = 0
    i=0
    for _ in A:
        fin += 1
    fin -= 1 
    
    return BusquedaBinaria(A, ele, inicio, fin)

def BusquedaBinaria(A, ele, inicio, fin):
    # Input: un arreglo A con elementos ordenados 
    # Output: índice del elemento si se encuentra, -1 si no está
    if inicio > fin:
        return -1  
    m = (inicio + fin) // 2  
    if A[m] == ele:
        return m  
    elif ele < A[m]:
        return BusquedaBinaria(A, ele, inicio, m - 1)
    else:
        return BusquedaBinaria(A, ele, m + 1, fin)

if __name__ == "__main__":
    A1 = [1, 3, 5, 7, 9, 11, 13, 15]
    ele1 = 7
    resultado1 = InicioFin(A1, ele1)
    print(resultado1)  # 3

    A2 = [2, 4, 6, 8, 10, 12, 14]
    ele2 = 5
    resultado2 = InicioFin(A2, ele2)
    print(resultado2)  # -1

    A3 = [10, 20, 30, 40, 50, 60, 70]
    ele3 = 60
    resultado3 = InicioFin(A3, ele3)
    print(resultado3)  # 5

    A4 = [100, 200, 300, 400, 500, 600, 700]
    ele4 = 250
    resultado4 = InicioFin(A4, ele4)
    print(resultado4)  # -1

    A5 = [5, 10, 15, 20, 25, 30, 35]
    ele5 = 35
    resultado6 = InicioFin(A5, ele5)
    print(resultado6)  # 6

    A6 = []
    ele6 = 6
    resultado7 = InicioFin(A6, ele6)
    print(resultado7)  # -1

    A7 = [0]
    ele7 = 5
    resultado8 = InicioFin(A7, ele7)
    print(resultado8)  # -1

    A8 = [0]
    ele8 = 0
    resultado9 = InicioFin(A8, ele8)
    print(resultado9)  # 0

"""
    Codigo optimizado
    (aqui no se inicializan inicio y fin porque python ya detecta que en una busqueda binaria 
    inicio es el primer indice del arreglo y fin el ultimo)
    def BusquedaBinaria(A, ele, inicio, fin):
    # Input: un arreglo A con elementos ordenados 
    # Output: índice del elemento si se encuentra, -1 si no está
    if inicio > fin:
        return -1
    m = (inicio + fin) // 2  
    if A[m] == ele:
        return m  
    elif ele < A[m]:
        return BusquedaBinaria(A, ele, inicio, m - 1)
    else:
        return BusquedaBinaria(A, ele, m + 1, fin)

if __name__ == "__main__":
    A1 = [1, 3, 5, 7, 9, 11, 13, 15]
    ele1 = 7
    resultado1 = BusquedaBinaria(A1, ele1, 0, len(A1) - 1)  
    print(resultado1)  # 3

    A2 = [2, 4, 6, 8, 10, 12, 14]
    ele2 = 5
    resultado2 = BusquedaBinaria(A2, ele2, 0, len(A2) - 1)  
    print(resultado2)  # -1

    A3 = [10, 20, 30, 40, 50, 60, 70]
    ele3 = 60
    resultado3 = BusquedaBinaria(A3, ele3, 0, len(A3) - 1)  
    print(resultado3)  # 5

    A4 = [100, 200, 300, 400, 500, 600, 700]
    ele4 = 250
    resultado4 = BusquedaBinaria(A4, ele4, 0, len(A4) - 1)  
    print(resultado4)  # -1

    A5 = [5, 10, 15, 20, 25, 30, 35]
    ele5 = 35
    resultado5 = BusquedaBinaria(A5, ele5, 0, len(A5) - 1)  
    print(resultado5)  # 6

    A6 = []
    ele6 = 6
    resultado6 = BusquedaBinaria(A6, ele6, 0, len(A6) - 1)  
    print(resultado6)  # -1

    A7 = [0]
    ele7 = 1
    resultado7 = BusquedaBinaria(A7, ele7, 0, len(A7) - 1)  
    print(resultado7)  # -1

    A8 = [0]
    ele8 = 0
    resultado8 = BusquedaBinaria(A8, ele8, 0, len(A8) - 1)  
    print(resultado8)  # 0"""
