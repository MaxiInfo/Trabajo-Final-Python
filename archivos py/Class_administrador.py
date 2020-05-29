import csv
from pattern.text.es import parse , split, lexicon, spelling
import random as r
from collections import Counter


class AdministradorDeJuego():
    tupla_adj = ('AO','JJ','AQ','DI','DT')
    tupla_sus = ('NC','NN','NCS','NCP','NNS','NP','NNP','W')
    tupla_verb = ('VAG','VBG','VAI','VAN','MD','VAS','VMG','VMI','VB','VMM','VMN','VMP','VBN','VMS','VSG','VSI','VSN','VSP','VSS')
    

    def __init__(self,dif = 'facil'):
        self._dificultad_actual = dif #puede cambiar pero puse medio como PREDETERMINADO
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

    
    def existe_en(self,palabra):
        '''
            Comprueba en el spelling y en el lexicon
        '''
        return palabra in spelling and palabra in lexicon

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
        '''
        palabra_split = (parse(palabra).split())
        booleano = False
        if palabra_split[0][0][1] in self.tupla_sus and self.existe_en(palabra):
            booleano = True
        elif palabra_split[0][0][1] in self.tupla_verb and self.existe_en(palabra):
            booleano = True 
        return booleano
        
    def __es_correcta_dificil(self,palabra):
        lista = ['verb','adj','sus']
        azar = lista[r.randint(0,2)]
        palabra_split = (parse(palabra).split())
        booleano = False

        if azar == 'verb':
            if palabra_split[0][0][1] in self.tupla_verb and self.existe_en(palabra):
                booleano = True
        elif azar == 'adj':
            if palabra_split[0][0][1] in self.tupla_adj and self.existe_en(palabra):
                booleano = True
        else:
            if palabra_split[0][0][1] in self.tupla_sus and self.existe_en(palabra):
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


objeto = AdministradorDeJuego('facil')
print(objeto.es_correcta('lápiz'))

