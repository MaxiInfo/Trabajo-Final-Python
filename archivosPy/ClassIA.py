from GenDic import gen_dics
from GenWord import main as gen_wordlist
import InsertWord
class Computer:
    def __init__(self):
        self._letters = []
        self._score = 0
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
        
    def play (self):
        pass    

    def select_word_and_position(self,matriz):
        """
        Funcion que en base a la matriz de estado del tablero y las letras en el atril de la clase busca el espacio para insertar alguna
        de las palabra generadas por el modulo genWord
        """
        def len_palabra(list_positions):
            max = -1
            positions = []
            for i in list_positions:
                if i['cant'] > max:
                    max = i['cant']
            for i in list_positions:
                if i['cant'] == max:
                    positions+= i
            return max,positions
        def serch_word(max, wordlist):
            if len(wordlist) != 0:
                if max < len(wordlist[-1]):
                    serch_word(max,wordlist[0:-1])
                else:
                    return (wordlist[-1])         
            else:
                return "Error"

        list_positions = gen_dics(matriz,len(matriz),len(matriz[0]))
        wordlist = gen_wordlist(self.get_letters())
        max,positions = len_palabra(list_positions)
        word = serch_word(max, wordlist)
        if word != "Error":
            print('ok')

        print_mat(list_positions)
        print('+'*40)
        print(self.get_letters())
        print(wordlist)
        pass

def palabra(matriz):
    palabra = 'casa'
    for i in range(len(palabra)):
        matriz[5][i+4]= palabra[i]
    return matriz

def change_matriz(matriz):
    for i in range(15):
        for j in range(15):
            if i == j:
                matriz[i][j] = 'p'
    return matriz


def print_mat (m):
    for i in m:
        print(i)
    pass
def main():
    IA = Computer()
    IA.set_letters(['c','a','v','p','a','e','t'])
    matriz = [[0 for j in range(15)]for i in range(15)]
    #print_mat(matriz)
    #print('+'*40)
    matriz = palabra(matriz)
    #print_mat(matriz)
    #print('+'*40)

    IA.serch_position(matriz)

    pass

main()


"""

['a','a','a','a','a','a','a']

['z','z','z','z','z','z','z']

['c','a','v','p','a','e','t']

['r','u','i','a','i','h','y']

['v','b','n','j','q','w','t']

"""