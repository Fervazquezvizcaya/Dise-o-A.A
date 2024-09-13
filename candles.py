def candles(a: list[int]) -> int:
    """
    Args:
        a (list[int]): The candles heights.
    
    Returns:
        int: The number of candles that are tallest
    """

def candles(height: list[int]) -> int:
    
    
    max_height = max(height)  # Encuentra la altura máxima
    count_max_height = 0      # Inicializa el contador
    
    # Ciclo que cuenta cuántas veces aparece la altura máxima
    for h in height:
        if h == max_height:
            count_max_height += 1
    
    return count_max_height  # Regresa el contador



if __name__ == "__main__":
    print(candles([4, 4, 1, 3])) # 2
    print(candles([1, 1, 1, 1, 1])) # 5
    print(candles([5, 3, 1, 3, 5, 3, 1, 3, 5])) # 3
    print(candles([10000, 10001, 10002, 10002, 10000])) # 2
    print(candles([999, 1000, 99, 912, 100])) # 1
