def generar_string(diccionario):
    string = 'Nombre | Puntaje | Fecha\n'
    for clave,valor in diccionario.items():
        string +=  clave + "    |    " + str(valor[0]) + "     |     " + valor[1] + "\n"  
    return string