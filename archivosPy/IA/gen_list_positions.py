def main(matriz,cant_row,cant_col):
    '''
    gen_dics me genera una lista de diccionarios donde guarda la primera posicion  una lista de tuplas correspondientes a cada posicion
    donde se puede ingresar la palabra y la cantidad de aracteres maxima de la palabra a insertar
    '''
    row = col = 0
    list_positions = []
    #recorrido horizontal
    while row < cant_row:
        while col < cant_col:
            if (col < cant_col -1) and (matriz[row][col] == 0) and (matriz[row][col+1] == 0): #se fija si se puede ingresar una palabra de 2 caracteres
                dic = {}
                list_tup = []
                list_tup.append((row,col))
                col += 1
                while col < cant_col:
                    if matriz[row][col] == 0:
                        list_tup.append((row,col))
                    else: 
                        break
                    col += 1
                list_positions.append(list_tup)
            else:
                col+= 1
        col = 0
        row += 1
    #recorrido vertical
    row = col = 0
    while col < cant_col:
        while row < cant_row:
            if (row < cant_row -1) and (matriz[row][col] == 0) and (matriz[row+1][col] == 0): #se fija si se puede ingresar una palabra de 2 caracteres
                list_tup = []
                list_tup.append((row,col))
                row += 1
                while row < cant_row:
                    if matriz[row][col] == 0:
                        list_tup.append((row,col))
                    else: 
                        break
                    row += 1
                list_positions.append(list_tup)
            else:
                row+= 1
        row = 0
        col += 1
    return list_positions


