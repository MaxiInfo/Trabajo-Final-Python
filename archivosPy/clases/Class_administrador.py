import csv
from pattern.text.es import parse , split, lexicon, spelling , verbs
import random as r
from collections import Counter


class AdministradorDeJuego():
    tupla_adj = ('AO','JJ','AQ','DI','DT')
    tupla_sus = ('NC','NN','NCS','NCP','NNS','NP','NNP','W')
    tupla_verb = ('VAG','VBG','VAI','VAN','MD','VAS','VMG','VMI','VB','VMM','VMN','VMP','VBN','VMS','VSG','VSI','VSN','VSP','VSS')
    

    def __init__(self,dif,modsBolsa = [None,None]):
        self._dificultad_actual = dif
        self._tuplas_DL = []
        self._tuplas_TL = []
        self._tuplas_DW = []
        self._tuplas_TW = []
        self._tuplas_R10 = []
        self._tuplas_R20 = []
        self.__crear_tuplas()
        self.__crear_diccionarios(modsBolsa)

    def get_dificultad(self):
        return self._dificultad_actual

    def __crear_diccionarios(self, bolsa_fichas):
        '''
            En base a la dificultad, toma la cantidad y puntaje de cada letra y mete ambas en dos diccionarios
        '''
        ubicacion = 'archivosCSV/'+self._dificultad_actual + ".csv" # -> medio.csv, facil.csv, dificil.csv
        archivo_csv = open(ubicacion,'r',encoding= 'utf8')
        csv_reader = csv.reader(archivo_csv, delimiter = ',', quotechar = '"')
        next(archivo_csv) # me salteo la primer linea que sólo contiene la información de las columnas.

        '''
            Corregí lo siguiente xq si fuera el caso que ninguno se haya modificado, daría error ya que procesaría dos veces
                el CSV.
        '''

        if bolsa_fichas[0] == None and bolsa_fichas[1] == None: #NINGUNO SE MODIFICÓ.
            puntajes = {}
            cantidades = {}
            #los identificadores de cada columna empiezan desde cero.
            for columna in csv_reader:
                letra_actual = columna[0] #letra
                cantidad_actual = int(columna[1]) #cantidad
                puntaje_actual = int(columna[2]) #puntaje
                cantidades[letra_actual] = cantidad_actual
                puntajes[letra_actual] = puntaje_actual

        elif bolsa_fichas[0] == None and bolsa_fichas[1] != None: #Cantidades no se modificó, pero puntajes si.
            cantidades = {}
            for columna in csv_reader:
                letra_actual = columna[0]
                cantidad_actual = int(columna[1])
                cantidades[letra_actual] = cantidad_actual
            puntajes = bolsa_fichas[1] #modifico puntajes con lo modificado en configuraciones.

        elif bolsa_fichas[0] != None and bolsa_fichas[1] == None: #Cantidades se modificó, pero puntajes no.
            puntajes = {}
            for columna in csv_reader:
                letra_actual = columna[0]
                puntaje_actual = int(columna[2])
                puntajes[letra_actual] = puntaje_actual
            cantidades = bolsa_fichas[0] #modifico cantidades con lo modificado en configuraciones.
            
        else: #AMBOS SE MODIFICAN
            cantidades = bolsa_fichas[0]
            puntajes = bolsa_fichas[1]
        
        self._diccionario_cantidad = cantidades
        self._diccionario_puntaje = puntajes

        archivo_csv.close()

    def get_cantidad(self):
        return self._diccionario_cantidad
    
    def get_puntaje(self):
        return self._diccionario_puntaje

    def get_dificultad(self):
        return self._dificultad_actual
    
    def existe_en(self,palabra):
        '''
            Comprueba en el spelling y en el lexicon
        '''
        return palabra in verbs or (palabra in spelling and palabra in lexicon)

    def __es_correcta_facil(self,palabra):
        '''
        Evalúa la palabra y lo mete en una lista bastante asquerosa de acceder, pero el [0][0][1] es la información de qué es la palabra -> Adjetivo, Verbo, Sustantivo
        El problema con los sustantivos, es que también toman palabras inexistentes, hay que arreglar eso
        '''
        booleano = self.existe_en(palabra)
        return booleano
             
    def __es_correcta_medio(self,palabra):
        '''
            Ver comentario en naranja de arriba

            MOD: la catedra cambió, en medio sólo acepta adjetivos o verbos.
        '''
        palabra_split = (parse(palabra).split())
        booleano = False
        if palabra_split[0][0][1] in self.tupla_adj and self.existe_en(palabra):
            booleano = True
        elif palabra_split[0][0][1] in self.tupla_verb and self.existe_en(palabra):
            booleano = True 
        return booleano
        
    def __es_correcta_dificil(self,palabra):
        '''
            MOD: la catedra sólo acepta adjetivos o verbos, en difícil se toma aleatoriamente cualquiera de los dos.
        '''
        lista = ['verb','adj']
        azar = lista[r.randint(0,1)]
        palabra_split = (parse(palabra).split())
        booleano = False

        if azar == 'verb':
            if palabra_split[0][0][1] in self.tupla_verb and self.existe_en(palabra):
                booleano = True
        else:
            if palabra_split[0][0][1] in self.tupla_adj and self.existe_en(palabra):
                booleano = True

        return booleano
        
    def es_correcta(self,palabra):
        dificultad = self._dificultad_actual 
        if dificultad == 'facil':
            #llamo a modulo es_correcta_facil
            booleano = self.__es_correcta_facil(palabra)
        elif dificultad == 'medio':
            #llamo a modulo es_correcta_medio
            booleano = self.__es_correcta_medio(palabra)
        else:
            #llamo a modulo es_correcta_dificil
            booleano = self.__es_correcta_dificil
        return booleano

    #=======================================================================================================================#
    def _no_hay_mas(self,auxiliar,letra):
        '''
            Si auxiliar me queda en cero, entonces es momento de hacer un delete de esa letra del diccionario de cantidades
        '''
        if auxiliar <= 0:
            del self._diccionario_cantidad[letra]
    
    
    def _comprobar(self,auxiliar):
        '''
            True si auxiliar (cantidad de la letra -1) no es negativo, para tomarlo
            False si auxiliar es negativo, osea que bueno, no podés tomar nada.
        '''
        if auxiliar >= 0:
            return True
        else:
            return False

    def _elegir_letra(self,lista_letras, lista_prohibidas, lista_rng):
        '''
            r.choice(lista) -> agarra una letra aleatoria. El while sirve para que la letra que se agarre siempre sea valida
              -> osea que no esté en la lista de letras prohibidas y que la letra generada esté en la lista_rng.
              -> también está contemplado el caso donde se eliminen letras del diccionario (lista_letras contiene solo las letras disponibles)

        '''
        booleano = True
        while booleano:
            caracter = r.choice(lista_letras)
            if caracter not in lista_prohibidas and caracter in lista_rng:
                booleano = False
        return caracter

    def tomar_fichas(self,cantidad_fichas):
        '''
            El primer prototipo de este metodo fue HORRIBLE, explico que hace este método hermoso:
                fichas -> lo que retorno, es una lista por que si es string, letras como RR o LL se toman obviamente como dos fichas gastadas
                lista -> va almacenando todo lo que se ingresa
                contador -> contabiliza lo de lista, y en el for, por cada letra que aparezca 2 o más veces, la mete en lista_prohibidas
                lista_prohibidas -> controla que las letras no ingresen más de dos veces

                agregado: generador de numeros aleatorios y listas que contienen letras en base a su frecuencia en el idioma español.
                me encantaría creer que ésta modificación, va a dar un margen de letras más usables para generar palabras.

                Vean los comentarios y ya para entender.
        '''
        fichas = []
        lista = []
        lista_prohibidas = []
        frecuencia_alta = ['E', 'A','O' ,'S' ,'R' ,'N', 'I', 'D' ,'L' ,'C' ,'T' ,'U' ,'M' ,'P']
        frecuencia_media = ['B', 'G', 'V', 'Y', 'Q', 'H', 'F','RR','LL']
        frecuencia_baja = ['Z', 'J', 'Ñ', 'X', 'K', 'W']
        while len(fichas) < cantidad_fichas:
            #Creo una lista con las llaves(letras) disponibles del diccionario
            letras = list(self._diccionario_cantidad.keys()) 

            RNG = r.randint(1,100)
            letra_actual = ''
            if RNG <= 60: #FRECUENCIA ALTA
                letra_actual = self._elegir_letra(letras,lista_prohibidas,frecuencia_alta)
            elif RNG > 60 and RNG <=90: #FRECUENCIA MEDIA
                letra_actual = self._elegir_letra(letras,lista_prohibidas,frecuencia_media)
            else: #FRECUENCIA BAJA
                letra_actual = self._elegir_letra(letras,lista_prohibidas,frecuencia_baja)

            #Tomo la cantidad actual de la letra, la guardo en aux restada en 1.
            aux = self._diccionario_cantidad[letra_actual] -1
            #Ver documentación de comprobar
            if self._comprobar(aux) and len(fichas) < cantidad_fichas:
                fichas.append(letra_actual.lower())
                self._diccionario_cantidad[letra_actual] -= 1
                lista.append(letra_actual)

            contador = Counter(lista)
            for clave,valor in contador.items():
                if valor >= 2: 
                    lista_prohibidas.append(clave)
            #Ver documentación de no_hay_mas
            self._no_hay_mas(aux,letra_actual)
                
        return fichas
    #=======================================================================================================================#

    def __crear_tuplas(self):
        '''
            usado en el __init__, en base a la dificultad llena la lista de tuplas correspondiente. PARA EL TABLERO
        '''
        ubicacion = 'archivosCSV/tuplas_' + self._dificultad_actual + ".csv" # tuplas_dificultad.csv. Sólo para abrir
        archivo_csv = open(ubicacion,'r',encoding= 'utf8') #abro el archivo
        csv_reader = csv.reader(archivo_csv, delimiter = ',', quotechar = '"') 
        next(archivo_csv) # me salteo la primer linea que sólo contiene la información de las columnas.


        for columna in csv_reader:
            fila_actual = int(columna[0])
            columna_actual = int(columna[1])
            tupla = (fila_actual,columna_actual)
            identificador = columna[2] # DL, TL, DW, TW, R10, R20

            if identificador == 'DW':
                self._tuplas_DW.append(tupla)
            elif identificador == 'TW':
                self._tuplas_TW.append(tupla)
            elif identificador == 'DL':
                self._tuplas_DL.append(tupla)
            elif identificador == 'TL':
                self._tuplas_TL.append(tupla)
            elif identificador == 'R10':
                self._tuplas_R10.append(tupla)
            else:
                self._tuplas_R20.append(tupla)

    def devolver_tuplas(self):
        '''
            devuelve una lista de listas con todas las tuplas
            [0] -> Double Word
            [1] -> Triple Word
            [2] -> Double Letter
            [3] -> Triple Letter
            [4] -> Resta 10
            [5] -> Resta 20
        '''
        lista_tuplas = [self._tuplas_DW,self._tuplas_TW,self._tuplas_DL,self._tuplas_TL,self._tuplas_R10,self._tuplas_R20]
        return lista_tuplas

    def calcular_puntaje(self,palabra,tupla):
        puntaje = 0
        multiplicador = 0

        for i in range(len(palabra)): #de 0 hasta len(palabra) -1
            posicion_actual = tupla[i]

            if posicion_actual in self._tuplas_DW: #Double word
                puntaje += self._diccionario_puntaje[palabra[i].upper()]
                multiplicador += 2
            elif posicion_actual in self._tuplas_TW: #Triple word
                puntaje += self._diccionario_puntaje[palabra[i].upper()]
                multiplicador += 3
            elif posicion_actual in self._tuplas_DL: #Double letter
                puntaje += self._diccionario_puntaje[palabra[i].upper()] * 2
            elif posicion_actual in self._tuplas_TL: #Triple letter
                puntaje += self._diccionario_puntaje[palabra[i].upper()] * 3
            elif posicion_actual in self._tuplas_R10: #Restar 10
                puntaje += self._diccionario_puntaje[palabra[i].upper()] -10
            elif posicion_actual in self._tuplas_R20: #Restar 20
                puntaje += self._diccionario_puntaje[palabra[i].upper()] -20
            else: #La letra tocó una casilla no especial
                puntaje += self._diccionario_puntaje[palabra[i].upper()]

        if multiplicador != 0 and puntaje > 0: #Significa que tocó algun DoubleWord o Triple Word. Eso sí, si el puntaje es negativo, no se aumenta
            puntaje *= multiplicador
        return puntaje
    def calcular_sobrante(self,lista_caracteres):
        '''
            Recibe una lista de caracteres. Retorna la suma de todos los caracteres.
        '''
        puntaje = 0
        for char in lista_caracteres:
            puntaje += self._diccionario_puntaje[char.upper()]
        return puntaje * -1

