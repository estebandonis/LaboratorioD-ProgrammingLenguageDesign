import time

def exec(transiciones, estado_inicial, returns, cadena, i):

    valores = ""
    error = False
    estado_actual = estado_inicial
    a = i
    while a < len(cadena) and error == False:
        cad = ord(cadena[a])
        pasa = False
        for tran in transiciones:
            if estado_actual == tran[0] and cad == tran[1]:
                estado_actual = tran[2]
                pasa = True
                valores += cadena[a]
                break
        if pasa == False:
            error = True
            break
        a += 1
    
    tempValor = valores

    for tran in transiciones:
        if estado_actual == tran[0] and type(tran[1]) == str:
            valores = tran[1]
            break
    
    for ret in returns:
        if tempValor == ret:
            valores = returns[ret]
            break

    return a, valores