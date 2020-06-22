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
        
    def serch_position(self,matriz):
        dic_positions = gen_dics(matriz,len(matriz),len(matriz[0]))
        wordlist = gen_wordlist(self.get_letters)
        