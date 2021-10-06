def resultados(m):
    listafinal=[]
    for i in range(len(m)):
        if m[i]<10:
            listafinal.append(m[i])
    return listafinal
def datos(a,b):
    valores=[]
    matriz=[]
    listacompleta=[]
    for i in range(a):
        for i in range(b):    
            valor=int(input())
            valores.append(valor)
        matriz.append(valores)
        listacompleta=listacompleta+valores
        valores=[]
    return resultados(listacompleta)
def main():
    renglones=int(input())
    columnas=int(input())
    print (datos(renglones,columnas))
   



if __name__=='__main__':
    main()
