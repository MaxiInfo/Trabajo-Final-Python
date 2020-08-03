import json

def actualizar(nombre_jugador,puntaje,fecha,dificultad_jugada):
    '''El siguiente modulo lo que hace es actualizar el top10 de una dificultad previamente jugada.
        Abarca todos los casos posibles:
            Sí repito el NOMBRE como jugador y supero el puntaje existente -> lo actualizo.
            Sí repito el NOMBRE como jugador PERO no supero el puntaje existente -> no se actualiza.
            Sí es un nuevo NOMBRE, puede que entre o no al top10, de todas formas sí entra se verá bién posicionado, caso contrario 
                no ingresa.
    '''

    NOMBRE = 'archivosJSON/archivoTop.json'
    sigo = True
    try:
        with open(NOMBRE,'r') as archivo_top:
            diccionario_completo = json.load(archivo_top) #Tomo todo el diccionario
            diccionario_ordenar = diccionario_completo[dificultad_jugada] #facil, medio, o dificil.

            if nombre_jugador in diccionario_ordenar: #Sí existe mi jugador. 
                if puntaje > diccionario_ordenar[nombre_jugador][0]: #Sí existe mi jugador y el puntaje que tiene es mayor al original.
                    diccionario_ordenar[nombre_jugador] = [puntaje,fecha]
                else:
                    sigo = False
                #El hecho de usar dos if's, es que si uso AND se puede dar el caso que -> existe el jugador, pero no supera el puntaje.
                    #Por lo tanto iría al else y así y todo actualizaría con el puntaje menor, DEJENLO COMO ESTÁ.
            else:
                diccionario_ordenar[nombre_jugador] = [puntaje,fecha] #Inserto
            if sigo:
                lista = sorted(diccionario_ordenar.items(), key = lambda item : item[1][0],reverse = True)
                if len(lista) == 11:
                    del lista[10]
                    
                diccionario_actualizado = {elemento[0]:[elemento[1][0],elemento[1][1]] for elemento in lista}
                diccionario_completo[dificultad_jugada] = diccionario_actualizado
                json.dump(diccionario_completo,archivo_top) #Guardo el diccionario actualizado.
            archivo_top.close()

    except FileNotFoundError:
        #Si se dá el caso que el usuario borra el archivoTop.json por que es un cliente desastroso, no estaría mal generarlo de nuevo.
        diccionario = {"facil": {"AAA": [50, "22/5"], "BBB": [45, "22/5"], "CCC": [40, "22/5"], "DDD": [35, "22/5"], "EEE": [30, "22/5"], "FFF": [25, "22/5"], "GGG": [20, "22/5"], "HHH": [15, "22/5"], "III": [10, "22/5"], "JJJ": [5, "22/5"]}, "medio": {"KKK": [70, "23/5"], "LLL": [65, "23/5"], "MMM": [60, "23/5"], "NNN": [55, "23/5"], "OOO": [50, "23/5"], "PPP": [45, "23/5"], "QQQ": [40, "23/5"], "RRR": [35, "23/5"], "SSS": [30, "23/5"], "TTT": [25, "23/5"]}, "dificil": {"j1": [45, "24/5"], "j2": [40, "24/5"], "j3": [35, "24/5"], "j4": [30, "24/5"], "j5": [25, "24/5"], "j6": [20, "24/5"], "j7": [15, "24/5"], "j8": [10, "24/5"], "j9": [5, "24/5"], "j10": [0, "24/5"]}}
        archivo_nuevo = open(NOMBRE,'w')
        json.dump(diccionario,archivo_nuevo)
        archivo_nuevo.close()
def get_ult_top10(dif):
    '''
        En base a la dificultad toma el peor puntaje del top10. La precondición es que sí o sí exista dicho archivo.
    '''
    nombre_archivo = 'archivosJSON/archivoTop.json'
    archivo = open(nombre_archivo,'r') #Apertura de archivo
    diccionario_completo = json.load(archivo)
    archivo.close() #Cierre de archivo
    diccionario_buscado = diccionario_completo[dif]
    llaves = list(diccionario_buscado.keys()) #Toma todas las llaves, hace la conversión a lista para poder hacer uso de indice. (dict_keys no soporta indice)
    return diccionario_buscado[llaves[9]][0] #Devuelve el puntaje del ultimo en el top de la dificultad.
