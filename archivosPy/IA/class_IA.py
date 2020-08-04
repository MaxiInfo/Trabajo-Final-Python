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
    def play (self,window,admin,board,player_score): 
        """
        este modulo es el que se encarga de todo lo necesario para que la IA juegue un turno
        """
        matriz = board.get_board()
        pos,word = self._select_word_and_position(matriz,admin,player_score)
        #print(pos)
        #print(admin.get_bad_positions())
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
            window.FindElement('-iaSize-').Update(str(self._score))
        return

    def _refill_letters(self,admin,word):
        """
        toma las letras de la bolsa y las remplaza donde estaban las letras las cuales formaron la palabra
        """
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
        for i in range(len(word)):
            window.FindElement(pos[i]).Update(image_filename = PATH_LETRAS + word[i].upper() + EXTENSION,disabled=True,button_color = ('black','#58F76D'))
            board.mod_board(pos,word)
        pass

    def __search_pos(self,list_positions,word_list,admin,player_score):
        """
        Esta funcion se encarga de ejecutar uno u otra funcion de busqueda segun la dificultad del juego
        """
        if admin.get_dificultad() == 'facil':
            pos, word = self.search_easy(list_positions,player_score,admin,word_list)
        elif admin.get_dificultad() == 'medio':
            pos, word = self.search_medium(list_positions,admin,word_list)
        else:
            pos, word = self.search_dificult(list_positions,word_list,admin)
        return pos,word

    def search_easy(self,list_positions,player_score,admin,word_list):
        """
        Funcion recursiva, busca si la ultima palabra que se encuentra en la lista 'word_list'
        entra en las posiciones de 'list_positions', se agrea todos los posibles lugares en 'l_aux'
        luego se busca un lugar aleatorio de todos los posibles y se acomoda la palabra en una posicion 
        aleatoria dentro del arreglo escogido, tanto esta ultima posicion como la palabra son retornados
        parametros
        list_positions type = lista de tuplas
        word_list = lista de listas de caracteres o lista de palabras
        """
        if word_list == []:
            return None,None
        word_act = word_list[0]
        ls_aux =[]
        if self.get_score() >= player_score:
            for i in list_positions:
                if len(i) >= len(word_act):
                    for j in range(len(i)-len(word_act)):
                        ok = False
                        for k in i[j:j+len(word_act)]:
                            if k in admin.get_bad_positions():
                                ok = True
                        if ok:
                            ls_aux.append(i[j:j+len(word_act)])
            if ls_aux == []:
                for i in list_positions:
                    if len(i) >= len(word_act):
                        ls_aux.append(i)
        else:
            for i in list_positions:
                if len(i) >= len(word_act):
                    ls_aux.append(i)
        if ls_aux != []:
            ls_def = ls_aux[r(0,len(ls_aux)-1)]
            st_pos = r(0,(len(ls_def)-1)-(len(word_act)-1))
            return ls_def[st_pos:st_pos+len(word_act)],word_act
        else:
            search_easy(list_positions,player_score,admin,word_list[1:])

    def search_medium(self,list_positions,admin,word_list):
        """
        Funcion similar a serch_easy el unico cambio es que la IA primero busca si existen posiciones 
        posibles sin descuentos de puntaje y de no haber ingresa la palabra en una posicion con descuentos de puntaje
        """
        if word_list == []:
            return None,None
        word_act = word_list[-1]
        ls_aux =[]
        for i in list_positions:
            if len(i) >= len(word_act):
                for j in range(len(i)-len(word_act)):
                    ok = True
                    for k in i[j:j+len(word_act)]:
                        if k in admin.get_bad_positions():
                            ok = False
                    if ok:
                        ls_aux.append(i)
        if ls_aux == []:
            for i in list_positions:
                if len(i) >= len(word_act):
                    ls_aux.append(i)
        if ls_aux != []:
            ls_def = ls_aux[r(0,len(ls_aux)-1)]
            st_pos = r(0,(len(ls_def)-1)-(len(word_act)-1))
            return ls_def[st_pos:st_pos+len(word_act)],word_act
        else:
            serach_medium(list_positions,admin,word_list[0:-1])

    def search_dificult(self,list_positions,word_list,admin):
        """
        esta funcion realiza un calculo de cada lugar donde se puede ingresar la ultima lpalabra recibida por 
        el parametro word_list, se queda con el mayor puntaje y las posiciones donde seria ese mayor puntaje,
        en caso de que la palabra no entre se llama de forma recursiva a la funcion con el parametro acotado
        desde la primera posicion hasta la ultima
        """
        if word_list == []:
            return None,None
        word_act = word_list[-1]
        ls_tuplas = []
        pun_max = -1
        for i in list_positions:
            if len(i) >= len(word_act):
                for j in range(len(i)-len(word_act)):
                    pun_act = admin.calcular_puntaje(word_act,i[j:j+len(word_act)])
                    if pun_act > pun_max:
                        pun_max = pun_act
                        ls_tuplas = i[j:j+len(word_act)]
        if ls_tuplas != []:
            return ls_tuplas,word_act
        else:
            search_dificult(list_positions,admin,word_list[0:-1])

    def _select_word_and_position(self,matriz,admin,player_score):
        """
        Funcion que en base a la matriz de estado del tablero y las letras en el atril de la clase busca el espacio para insertar alguna
        de las palabra generadas por el modulo genWord
        """
        list_positions = serch_positions(matriz,len(matriz),len(matriz[0]))
        if list_positions == []:
            return (None,None)
        word_list = gen_wordlist(self.get_letters(),admin)
        if word_list == []:
            return (None,None)
        pos,word = self.__search_pos(list_positions,word_list,admin,player_score)
        return (pos,word)
