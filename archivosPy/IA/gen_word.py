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


def palabras_correctas(list_combinaciones):
    #me ordena la lista por longitud de palbra de menor a mayor
    test_list = []
    for i in list_combinaciones:
        palabra = ''
        for j in i:
            palabra += j
        ok = comprobar(palabra)
        if ok and len(i) > 1:
            test_list.append(i)
    return test_list

def main(list_letters):
    list_conj_potencia = potencia(list_letters)

    list_combinaciones = []
    for i in list_conj_potencia:
        list_combinaciones += permuta(i)

    list_final = palabras_correctas(list_combinaciones)
    #list_final = list(set(list_final))
    list_final = sorted(list_final, key=lambda s:(len(s),s))
    return list_final

'''def main():
    list_letters = ['a','z','o','z','c','p','i']
    list_conj_potencia = potencia(list_letters)
    print(list_conj_potencia)
    list_combinaciones = []
    for i in list_conj_potencia:
        list_combinaciones += permuta(i)
    print(list_combinaciones)
    print(len(list_combinaciones))


    list_final = palabras_correctas(list_combinaciones)

    print(list_final)
    pass

main()'''