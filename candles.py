def candles(height: list[int]) -> int:
    """
    Args:
        height (list[int]): The candles heights.
    
    Returns:
        int: The number of candles that are tallest
    """
    
    # max_height = max(height)  # Encuentra la altura máxima de forma directa pero se utilizara el ciclo for para ejemplificar el D-F y PS
    
    if not height:
        return 0  # Maneja el caso donde la lista está vacía

    max_height = height[0]  # Inicializa max_height con el primer elemento
    for h in height:  # Recorre cada altura en la lista
        if h > max_height:
            max_height = h  # Actualiza max_height si se encuentra un valor mayor
    
    count_max_height = 0      # Inicializa el contador
    
    for h in height:
        if h == max_height:
            count_max_height += 1
    
    # count_max_height = height.count(max_height): esta linea sustituiria el ciclo segundo ciclo for 
    
    return count_max_height  # Regresa el contador
    
    """
    Codigo ejemplificado con un solo ciclo for
    if not height:
        return 0  # Maneja el caso donde la lista está vacía

    max_height = height[0]  # Inicializa max_height con el primer elemento
    count_max_height = 0  # Inicializa el contador

    for h in height:  # Un solo ciclo que encuentra la altura máxima y cuenta
        if h > max_height:
            max_height = h  # Actualiza max_height si encuentra un valor mayor
            count_max_height = 1  # Reinicia el contador para la nueva altura máxima
        elif h == max_height:
            count_max_height += 1  # Incrementa el contador si encuentra otra vela igual de alta
    return count_max_height  # Regresa el contador
    """
    """
    codigo con instrcciones minimizadas 
    max_height = max(height)
    count_max_height = height.count(max_height)
    
    return count_max_height
    """
if __name__ == "__main__":
    print(candles([4, 4, 1, 3])) # 2
    print(candles([1, 1, 1, 1, 1])) # 5
    print(candles([5, 3, 1, 3, 5, 3, 1, 3, 5])) # 3
    print(candles([10000, 10001, 10002, 10002, 10000])) # 2
    print(candles([999, 1000, 99, 912, 100])) # 1
