memo_fib = {}

def dic(num):
    if num in memo_fib:
        return memo_fib[num] # Si el valor ya está en memo_fib, se retorna directamente
    
    # Caso inicial
    if num < 2:
        memo_fib[num] = num
        return num
    
    # Caso recursivo
    resultado = dic(num - 1) + dic(num - 2)
    memo_fib[num] = resultado
    return resultado
    #Casos de prueba 
if __name__ == "__main__":
    print(f"Fibonacci de 8: {dic(8)}")   # Debería imprimir 21
    print(f"Fibonacci de 8: {dic(8)}")   # Ya almacenado, debería imprimir 21 sin recalcular
    print(f"Fibonacci de 10: {dic(10)}") # Debería imprimir 55
    print(f"Fibonacci de 10: {dic(10)}") # Ya almacenado, debería imprimir 55 sin recalcular

    # Mostrar lo que hay en memo_fib
    print("Valores almacenados en memo_fib:", memo_fib)