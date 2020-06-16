cant_row = 15
cant_col = 15

def print_matriz(matriz):
    for i in matriz:
        print(i)
    pass

def mod_matriz(matriz):
    for i in range(cant_row):
        for j in range(cant_col):
            if j == 7:
                matriz[i][j] = 1
    pass

def gen_dics():
    row = col = 0
    list_dics = []
    #recorrido horizontal
    while row < cant_row:
        while col < cant_col:
            if (col < cant_col -1) and (matriz[row][col] == 0) and (matriz[row][col+1] == 0): #se fija si se puede ingresar una palabra de 2 caracteres
                dic = {}
                list_tup = []
                cant = 0
                dic['tupla'] = (row,col)
                list_tup.append((row,col))
                cant += 1
                col += 1
                while col < cant_col:
                    if matriz[row][col] == 0:
                        list_tup.append((row,col))
                        cant += 1
                    else: 
                        break
                    col += 1

                dic['listTuplas'] = list_tup
                dic['cant'] = cant
                dic['escritura'] = 'horizontal'
                list_dics.append(dic)
            else:
                col+= 1

        col = 0
        row += 1
        list_tup = []
    #recorrido vertical
    row = col = 0
    while col < cant_row:
        while row < cant_col:
            if (col < cant_col -1) and (matriz[row][col] == 0) and (matriz[row][col+1] == 0): #se fija si se puede ingresar una palabra de 2 caracteres
                dic = {}
                list_tup = []
                cant = 0
                dic['tupla'] = (row,col)
                list_tup.append((row,col))
                cant += 1
                row += 1
                while row < cant_row:
                    if matriz[row][col] == 0:
                        list_tup.append((row,col))
                        cant += 1
                    else: 
                        break
                    row += 1

                dic['listTuplas'] = list_tup
                dic['cant'] = cant
                dic['escritura'] = 'vertical'
                list_dics.append(dic)
            else:
                row+= 1

        row = 0
        col += 1
        list_tup = []
    return list_dics


matriz = [[0 for j in range(cant_col)] for i in range(cant_row)]

#dic = {tupla = (0,5),cant:6,lst_tuplas = [(0,6),(0,7),(0,8),(0,9),(0,10),(0,11)],esc:'hoizontal'}
dic = {}

print_matriz(matriz)
print()

mod_matriz(matriz)
print_matriz(matriz)

list_dics = []
list_dics = gen_dics()

for i in list_dics:
    print(i)

#print_matriz(matriz)
