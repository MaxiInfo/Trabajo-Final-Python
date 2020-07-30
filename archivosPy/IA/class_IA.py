from archivosPy.IA.gen_dic import gen_dics
from archivosPy.IA.gen_word import main as gen_wordlist

path_letras = 'Imagenes/tablero/letras/'
extension = '.png'

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
        #serch type (pos,word)
        serch = self._select_word_and_position(matriz)
        if serch == None:
            #La IA pasa
            fichas_ant = self.get_letters()
            self.set_letters(admin.tomar_fichas(7))
            admin.devolver_a_bolsa(fichas_ant)
            self.add_changes()
        else:
            #La IA juega
            self._insert_word(window,serch[0],serch[1],board)
            self.set_score(admin.calcular_puntaje(serch[1],serch[0]))
            self._refill_letters(admin,serch[1])
        return

    def _refill_letters(self,admin,word):
        letters = self.get_letters() #Porque las vincula por valor??
        pos = 0
        while pos <= len(word)-1:
            letters[letters.index(word[pos])] = admin.tomar_fichas(1)[0]
            pos +=1
        pass

    def _insert_word(self,window,pos, word,board):
        for i in range(len(word)):
            window.FindElement(pos[i]).Update(image_filename = path_letras + word[i].upper() + extension,disabled=True,button_color = ('black','#58F76D'))
            board.mod_board(pos,word)
        pass

    def _select_word_and_position(self,matriz):
        """
        Funcion que en base a la matriz de estado del tablero y las letras en el atril de la clase busca el espacio para insertar alguna
        de las palabra generadas por el modulo genWord
        """
        def serch_pos(list_positions):
            maximo = -1
            positions = []
            #Busco la palabra mas grande
            for i in list_positions:
                if i['cant'] > maximo:
                    maximo = i['cant']
                    pos = i
            return pos,maximo
        def serch_word(maximo, wordlist):
            if len(wordlist) != 0:
                if maximo < len(wordlist[-1]):
                    serch_word(maximo,wordlist[0:-1])
                else:
                    return (wordlist[-1])         
            else:
                return "Error"

        list_positions = gen_dics(matriz,len(matriz),len(matriz[0]))
        wordlist = gen_wordlist(self.get_letters())
        pos,maximo = serch_pos(list_positions)
        word = serch_word(maximo, wordlist)
        if word != "Error" and len(word) > 1 and len(word) <= pos['cant']:
            return (pos['listTuplas'][0:len(word)], word)
        return None
