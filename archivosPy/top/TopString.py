def generar_string(diccionario):
    nombres = ''
    puntajes = ''
    fechas = ''
    for clave,valor in diccionario.items():
        nombres += clave + "\n"
        puntajes += str(valor[0]) + "\n"
        fechas += (valor[1]) + "\n"
    lista = [nombres,puntajes,fechas] 
    return lista