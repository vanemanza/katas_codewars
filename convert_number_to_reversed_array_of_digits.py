def digitize(n):
    number = str(n)
    lista = []
    for x in number:
        lista.insert(0, x)
    return lista

test1 = digitize(2009)
test2 = digitize(35231)
print(test1)  
print(test2)       