from archivosPy.IA.gen_list_positions import main as serch_positions
from archivosPy.IA.gen_word import main as gen_wordlist
from random import randint as r

PATH_LETRAS = 'Imagenes/tablero/letras/'
EXTENSION = '.png'

class Computer:
    def __init__(self):
        self._letters = []
        self._score = 0
        self._changes = 0
        pass

    def get_letters(self):
        return self._letters

    def set_letters(self,new_letters):
        #new_letters type = list of chars
        self._letters = new_letters
        pass

    def get_score(self):
        return self._score 

    def set_score(self,add_score):
        self._score += add_score
        pass

    def get_changes(self):
        return self._changes 

    def add_changes(self):
        self._changes += 1
        pass
    def play (self,window,admin,board): 
        matriz = board.get_board()
        pos,word = self._select_word_and_position(matriz,admin.get_dificultad())
        if pos == None:
            #La IA pasa
            fichas_ant = self.get_letters()
            self.set_letters(admin.tomar_fichas(7))
            admin.devolver_a_bolsa(fichas_ant)
            self.add_changes()
        else:
            #La IA juega
            self._insert_word(window,pos,word,board)
            self.set_score(admin.calcular_puntaje(word,pos))
            self._refill_letters(admin,word)
        return

    def _refill_letters(self,admin,word):
        letters = self.get_letters() #Porque las vincula por valor??
        pos = 0
        while pos <= len(word)-1:
            letters[letters.index(word[pos])] = admin.tomar_fichas(1)[0]
            pos +=1
        pass

    def _insert_word(self,window,pos, word,board):
        """
        Inserta una palabra recibida como parametro en la window con key (int,int)
        hace modificaciones a la matriz recibida como parametro en dichas posiciones
        """
        '''print('+'*20)
        print(pos)
        print(word)'''
        for i in range(len(word)):
            window.FindElement(pos[i]).Update(image_filename = PATH_LETRAS + word[i].upper() + EXTENSION,disabled=True,button_color = ('black','#58F76D'))
            board.mod_board(pos,word)
        pass

    def __serch_pos(self,list_positions,wordlist,dif):
        """
        Esta funcion se encarga de ejecutar uno u otra funcion de busqueda segun la dificultad del juego
        """
        if dif == 'facil':
            pos, word = self.serch_easy(list_positions,wordlist)
        elif dif == 'medio':
            pos, word = self.serch_medium(list_positions,wordlist)
        else:
            pos, word = self.serch_dificult(list_positions,wordlist)
        return pos,word

    def serch_dificult(self,list_positions,wordlist):
        pass

    def serch_medium(self,list_positions,wordlist):
        pass

    def serch_easy(self,list_positions,wordlist):
        """
        Funcion que busca segun el ultimo valor de la lista wordlist el que seria el mas grande
        busca las posiciones donde entraria y retorna la posicion a ingresar y la palabra
        """
        if wordlist == []:
            return None,None
        word_act = wordlist[-1]
        ls_aux =[]
        for i in list_positions:
            if len(i) >= len(word_act):
                ls_aux.append(i)
        if ls_aux != []:
            ls_def = ls_aux[r(0,len(ls_aux)-1)]
            st_pos = r(0,(len(ls_def)-1)-(len(word_act)-1))
            return ls_def[st_pos:st_pos+len(word_act)],word_act
        else:
            serch_easy(list_positions,wordlist[0:-1])

    def _select_word_and_position(self,matriz,dif):
        """
        Funcion que en base a la matriz de estado del tablero y las letras en el atril de la clase busca el espacio para insertar alguna
        de las palabra generadas por el modulo genWord
        """
        list_positions = serch_positions(matriz,len(matriz),len(matriz[0]))
        if list_positions == []:
            return (None,None)
        wordlist = gen_wordlist(self.get_letters())
        if wordlist == []:
            return (None,None)
        pos,word = self.__serch_pos(list_positions,wordlist,dif)
        return (pos,word)
