import csv
import pattern.es as pa
import random as r
from pattern.web import Wiktionary
w = Wiktionary(language="es")

class dificultad():
    dificultad_actual = 'medio' #puede cambiar pero puse medio como PREDETERMINADO
    diccionario_cantidad = {}
    diccionario_puntaje = {}

    def establecer_dificultad(self, nueva_dificultad):
        '''
            sólo establece la dificultad nueva para cambiar la predeterminada
        '''
        self.dificultad_actual = nueva_dificultad

    def crear_diccionarios(self):
        '''
            En base a la dificultad, toma la cantidad y puntaje de cada letra y mete ambas en dos diccionarios
        '''
        ubicacion = self.dificultad_actual + ".csv" # -> medio.csv, facil.csv, dificil.csv
        archivo_csv = open(ubicacion,'r',encoding= 'utf8')
        csv_reader = csv.reader(archivo_csv, delimiter = ',', quotechar = '"')
        next(archivo_csv) # me salteo la primer linea que sólo contiene la información de las columnas.

        puntajes = {}
        cantidades = {}

        #los identificadores de cada columna empiezan desde cero.
        for columna in csv_reader:
            letra_actual = columna[0] #letra
            cantidad_actual = columna[1] #cantidad
            puntaje_actual = columna[2] #puntaje
            cantidades[letra_actual] = cantidad_actual
            puntajes[letra_actual] = puntaje_actual
        
        self.diccionario_cantidad = cantidades
        self.diccionario_puntaje = puntajes

    def __es_correcta_facil(self,palabra):
        '''
        Evalúa la palabra y lo mete en una lista bastante asquerosa de acceder, pero el [0][0][1] es la información de qué es la palabra -> Adjetivo, Verbo, Sustantivo
        El problema con los sustantivos, es que también toman palabras inexistentes, hay que arreglar eso
        '''
        analisis = parse(palabra).split('/')
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


'''
El generar diccionarios funciona, en base a la dificultad, toma alguno u otro archivo csv. me pareció interesante meter la comprobación de palabras acá, ya que podemos
enlazar la dificultad con la configuración.
Lo unico que resta, es interconectar dicha clase de alguna forma con el tablero en cada juego que se efectue.

Cosas que me faltaron:
    -no me reconoce el import del pattern.es
    -comprobar que la palabra que cae en categoría NN sea un sustantivo y exista, o comprobar que no exista.

Cosas que hice:
    -Creé ésta clase
    -Moví los CSV por que sigo puteando en querer buscar por directorio, es una mierda.
    -Definí métodos privados, es_correcta tiene el control de llevar el flujo a donde sea necesario.

Lean los comentarios <3
'''