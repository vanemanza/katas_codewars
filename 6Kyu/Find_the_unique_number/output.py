def find_uniq(arr):
    """
    Recibe un array de números, pueden ser int o float. 
    De len >= 3.
    Todos los números son iguales, excepto uno.
    Devuelve el número diferente.
    
    >>> find_uniq([ 1, 1, 1, 2, 1, 1 ])
    2

    >>> find_uniq([ 0, 0, 0.55, 0, 0 ])
    0.55
    """
    n = [x for x in arr if arr.count(x)==1]
    for item in n:
        if type(item) == float:
            return float(item)
        if type(item) == int:
            return int(item)
