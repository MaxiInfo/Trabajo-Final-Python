palabra = 'lldwajhdksndrrakdjhwjkallal'
cant = 0
letras = []
while cant < len(palabra):
    if cant < len(palabra)-1 and palabra[cant]+palabra[cant+1] in ('rr','ll'):
        letras += [palabra[cant]+palabra[cant+1]]
        cant+=2
    else:
        letras += palabra[cant]
        cant += 1

print(letras)