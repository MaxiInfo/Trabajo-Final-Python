import csv
import pattern.es as pa
import random as r
from pattern.web import Wiktionary
from collections import Counter
w = Wiktionary(language="es")

class dificultad():
    

    def __init__(self):
        self._dificultad_actual = 'medio' #puede cambiar pero puse medio como PREDETERMINADO
        self.crear_diccionarios()

    def set_dificultad(self, nueva_dificultad):
        '''
            sólo establece la dificultad nueva para cambiar la predeterminada
        '''
        self._dificultad_actual = nueva_dificultad

    def crear_diccionarios(self):
        '''
            En base a la dificultad, toma la cantidad y puntaje de cada letra y mete ambas en dos diccionarios
        '''
        ubicacion = self._dificultad_actual + ".csv" # -> medio.csv, facil.csv, dificil.csv
        archivo_csv = open(ubicacion,'r',encoding= 'utf8')
        csv_reader = csv.reader(archivo_csv, delimiter = ',', quotechar = '"')
        next(archivo_csv) # me salteo la primer linea que sólo contiene la información de las columnas.

        puntajes = {}
        cantidades = {}

        #los identificadores de cada columna empiezan desde cero.
        for columna in csv_reader:
            letra_actual = columna[0] #letra
            cantidad_actual = int(columna[1]) #cantidad
            puntaje_actual = int(columna[2]) #puntaje
            cantidades[letra_actual] = cantidad_actual
            puntajes[letra_actual] = puntaje_actual
        
        self._diccionario_cantidad = cantidades
        self._diccionario_puntaje = puntajes

    def __es_correcta_facil(self,palabra):
        '''
        Evalúa la palabra y lo mete en una lista bastante asquerosa de acceder, pero el [0][0][1] es la información de qué es la palabra -> Adjetivo, Verbo, Sustantivo
        El problema con los sustantivos, es que también toman palabras inexistentes, hay que arreglar eso
        '''
        analisis = pa.parse(palabra).split('/')
        palabra_correcta = False
        if analisis[1] == "JJ" or analisis[1] == "VB":
            palabra_correcta = True
        elif (analisis[1] == "NN"):
            article=w.search(palabra)
            if article != None:
                palabra_correcta = True
        return palabra_correcta
        
    def __es_correcta_medio(self,palabra):
        '''
            Ver comentario en naranja de arriba
        '''
        palabra_split = (pa.parse(palabra).split())
        if palabra_split[0][0][1] == 'NN': #es sustantivo, pero también toma palabras que no existen como NN
            #acá se debería comprobar si la palabra EXISTE en el diccionario español, y en base a eso retornar true o false.
            pass
        return palabra_split[0][0][1] == 'VB'
        
    def __es_correcta_dificil(self,palabra):
        palabra_split = (pa.parse(palabra).split())
        lista = ['VB','JJ','NN']
        azar = lista[r.randint(0,2)]
        if azar == 'NN': #es sustantivo, pero también puede tomar una palabra que NO EXISTE como si existiera, hay que comprobarla.
            pass #meto el pass por que todavía no sé como hacer dicha comprobación

        return palabra_split[0][0][1] == azar #sí la palabra entra en los verbos o los adjetivos -> EXISTE, por lo tanto retorno true, retornará false sino entra.

    def es_correcta(self,palabra):
        dificultad = self.dificultad_actual
        if dificultad == 'facil':
            #llamo a modulo es_correcta_facil
            self.__es_correcta_facil(palabra)
        elif dificultad == 'medio':
            #llamo a modulo es_correcta_medio
            self.__es_correcta_medio(palabra)
        else:
            #llamo a modulo es_correcta_dificil
            self.__es_correcta_dificil

    ###########################################################
    def no_hay_mas(self,auxiliar,letra):
        '''
            Si auxiliar me queda en cero, entonces es momento de hacer un delete de esa letra del diccionario de cantidades
        '''
        if auxiliar <= 0:
            del self._diccionario_cantidad[letra]
    
    
    def comprobar(self,auxiliar):
        '''
            True si auxiliar (cantidad de la letra -1) no es negativo, para tomarlo
            False si auxiliar es negativo, osea que bueno, no podés tomar nada.
        '''
        if auxiliar >= 0:
            return True
        else:
            return False
    def tomar_fichas(self,cantidad_fichas):
        '''
            El primer prototipo de este metodo fue HORRIBLE, explico que hace este método hermoso:
                fichas -> lo que retorno, es una lista por que si es string, letras como RR o LL se toman obviamente como dos fichas gastadas
                lista -> va almacenando todo lo que se ingresa
                contador -> contabiliza lo de lista, y en el for, por cada letra que aparezca 2 o más veces, la mete en lista_prohibidas
                lista_prohibidas -> controla que las letras no ingresen más de dos veces

                Vean los comentarios y ya para entender.
        '''
        fichas = []
        lista = []
        lista_prohibidas = []
        while len(fichas) < cantidad_fichas:
            #Creo una lista con las llaves(letras) disponibles del diccionario
            letras = list(self._diccionario_cantidad.keys()) 

            #r.choice(lista) -> agarra una letra aleatoria. El while sirve para que la letra que se agarre siempre sea valida
             # -> osea que no esté en la lista de letras prohibidas.
            booleano = True
            while booleano:
                letra_actual = r.choice(letras) #tomo una letra aleatoria.
                if letra_actual not in lista_prohibidas:
                    booleano = False

            #Tomo la cantidad actual de la letra, la guardo en aux restada en 1.
            aux = self._diccionario_cantidad[letra_actual] -1
            #Ver documentación de comprobar
            if self.comprobar(aux) and len(fichas) < cantidad_fichas:
                fichas.append(letra_actual.lower())
                self._diccionario_cantidad[letra_actual] -= 1
                lista.append(letra_actual)

            contador = Counter(lista)
            for clave,valor in contador.items():
                if valor >= 2:
                    lista_prohibidas.append(clave)
            #Ver documentación de no_hay_mas
            self.no_hay_mas(aux,letra_actual)
                
        return fichas


objeto = dificultad()
objeto.crear_diccionarios()

#print('PRIMER PRINT DICT')
#print(objeto._diccionario_cantidad)
lista = objeto.tomar_fichas(7)
print(lista)
#print('SEGUNDO PRINT DICT')
#print(objeto._diccionario_cantidad)