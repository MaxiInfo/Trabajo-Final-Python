from pattern.text.es import parse , split, lexicon, spelling , verbs
tupla_adj = ('AO','JJ','AQ','DI','DT')
tupla_sus = ('NC','NN','NCS','NCP','NNS','NP','NNP','W')
tupla_verb = ('VAG','VBG','VAI','VAN','MD','VAS','VMG','VMI','VB','VMM','VMN','VMP','VBN','VMS','VSG','VSI','VSN','VSP','VSS')
    

def existe_en(palabra):
    '''
        Comprueba en el spelling y en el lexicon
    '''
    return palabra in verbs or (palabra in spelling and palabra in lexicon)

def __es_correcta_facil(palabra):
    '''
    Evalúa la palabra y lo mete en una lista bastante asquerosa de acceder, pero el [0][0][1] es la información de qué es la palabra -> Adjetivo, Verbo, Sustantivo
    El problema con los sustantivos, es que también toman palabras inexistentes, hay que arreglar eso
    '''
    booleano = existe_en(palabra)
    return booleano

def __es_correcta_medio(palabra):
    '''
        Ver comentario en naranja de arriba

        MOD: la catedra cambió, en medio sólo acepta adjetivos o verbos.
    '''
    palabra_split = (parse(palabra).split('/'))
    booleano = False
    if palabra_split[1] in tupla_adj and existe_en(palabra):
        booleano = True
    elif palabra_split[1] in tupla_verb and existe_en(palabra):
        booleano = True
    return booleano
    
def __es_correcta_dificil(palabra):
    '''
        MOD: la catedra sólo acepta adjetivos o verbos, en difícil se toma aleatoriamente cualquiera de los dos.
    '''
    lista = ['verb','adj']
    azar = lista[r.randint(0,1)]
    palabra_split = (parse(palabra).split('/'))
    booleano = False
    print(azar)
    if azar == 'verb':
        if palabra_split[1] in tupla_verb and existe_en(palabra):
            booleano = True
    else:
        if palabra_split[1] in tupla_adj and existe_en(palabra):
            booleano = True

    return booleano
    
def es_correcta(palabra):
    dificultad = 'medio' 
    if dificultad == 'facil':
        #llamo a modulo es_correcta_facil
        booleano = __es_correcta_facil(palabra)
    elif dificultad == 'medio':
        #llamo a modulo es_correcta_medio
        booleano = __es_correcta_medio(palabra)
    else:
        #llamo a modulo es_correcta_dificil
        booleano = __es_correcta_dificil(palabra)
    return booleano

palabra = 'pie'
print(existe_en(palabra))