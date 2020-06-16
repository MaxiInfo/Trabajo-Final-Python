from pattern.text.es import lexicon, spelling, verbs

def comprobar(palabra):
    '''
        Comprueba en el spelling y en el lexicon
    '''
    return palabra in verbs or ((palabra in spelling) and (palabra in lexicon))

def potencia(list_letters):
    """Calcula y devuelve el conjunto potencia del 
       conjunto list_letters.
    """
    if len(list_letters) == 0:
        return [[]]
    result = potencia(list_letters[:-1])
    return result + [s + [list_letters[-1]] for s in result]

def inserta(x, lst, i):
    """Devuelve una nueva lista resultado de insertar
       x dentro de lst en la posición i.
    """
    return lst[:i] + [x] + lst[i:]

def inserta_multiple(x, lst):
    """Devuelve una lista con el resultado de
       insertar x en todas las posiciones de lst.  
    """
    return [inserta(x, lst, i) for i in range(len(lst) + 1)]
    

def permuta(c):
    """Calcula y devuelve una lista con todas las
       permutaciones posibles que se pueden hacer
       con los elementos contenidos en c.
    """
    if len(c) == 0:
        return [[]]
    return sum([inserta_multiple(c[0], s) for s in permuta(c[1:])], [])

def imprime_ordenado(list_final):
    """Imprime en la salida estándar todos los
       subconjuntos del conjunto c (una lista de
       listas) ordenados primero por tamaño y
       luego lexicográficamente. Cada subconjunto
       se imprime en su propia línea. Los
       elementos de los subconjuntos deben ser
       comparables entre sí, de otra forma puede
       ocurrir un TypeError.
    """
    list_ok = []

    for i in sorted(list_final, key=lambda s: (len(s), s)):
        palabra = ''
        for j in i:
            palabra += j
        ok = comprobar(palabra)
        if ok and len(palabra) > 1:
            list_ok.append(palabra)
    
    print(list_ok)
    pass

def main():
    list_letters =  ['a','l','i','e','p','ñ','u']
    list_final = []

    list_conj_potencia = potencia(list_letters)

    #print(list_conj_potencia)

    for i in list_conj_potencia:
        list_final += permuta(i)

    #print(list_final)
    imprime_ordenado(list_final)
    pass


main()