def calculaEleA(A, ele):
    # input: Un arreglo A de elemntos ordenados
    # output: El numero de elementos del arreglo
    n = 0
    for _ in A:
        n += 1
    # No necesitamos restar 1 aquí, ya que usaremos n como es
    return BusquedaBinaria(A, ele, n)

def BusquedaBinaria(A, ele, n):
    # Input: un arreglo A con elementos ordenados
    # Output: True si el elemento está en el arreglo, False si no está
    if n == 1:
        if A[0] == ele:
            return True
        else:
            return False

    m = n // 2  

    if A[m] == ele:
        return True
    elif A[m] < ele:
        # mitad derecha
        return BusquedaBinaria(A[m:], ele, n - m) 
    else:
        # mitad izquierda
        return BusquedaBinaria(A[:m], ele, m)  

# Ejemplo de uso
if __name__ == "__main__":
    A = [2, 5, 7, 11, 13, 17, 18]
    elemento_a_buscar = 13
    resultado = calculaEleA(A, elemento_a_buscar)  
    print(resultado)  # True

    elemento_a_buscar = 4
    resultado = calculaEleA(A, elemento_a_buscar)  
    print(resultado)  # False




"""""
    -----OPCION DE UN CODIGO MAS CENCILLO Y OPTIMIZADO-----
    def BusquedaBinaria(A, ele):
    # Input: un arreglo A con elementos ordenados
    # Output: True si el elemento está en el arreglo, False si no está
    
    n = len(A)  # Este paso te ahorra crear un new def exclusivo para declarar n 
    # n = len(A) obtiene el numero de elementos del arreglo 
    if n == 1:
        if A[0] == ele:
            return True
        else:
            return False
    m = n // 2  
    if A[m] == ele:
        return True
    elif A[m] < ele:
        return BusquedaBinaria(A[m:], ele)
    else:
        return BusquedaBinaria(A[:m], ele) 

# Ejemplos
if __name__ == "__main__":

    A = [2,5,7,11,13,17,18]
    elemento_a_buscar = 13
    resultado = BusquedaBinaria(A, elemento_a_buscar)
    print(resultado)  # True

    elemento_a_buscar = 4
    resultado = BusquedaBinaria(A, elemento_a_buscar)
    print(resultado)  # False 
    
"""