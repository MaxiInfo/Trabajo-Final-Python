def gen_dics(matriz,cant_row,cant_col):
    '''
    gen_dics me genera una lista de diccionarios donde guarda la primera posicion donde se puede insertar una palabra en la clave "tupla"
    tambien guarda una lista de tuplas correspondientes a cada posicion donde se puede ingresar la palabra y la cantidad de aracteres maxima
    de la palabra a insertar
    '''
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
            if (col < cant_col -1) and (matriz[row][col] == 0) and (matriz[row+1][col] == 0): #se fija si se puede ingresar una palabra de 2 caracteres
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
