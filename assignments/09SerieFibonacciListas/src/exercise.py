def main():
    lista = []
    n = -1
    while n<0:
        n = int(input())

    if n==0:
        print("[]")
    elif n>0:
        lista = [0,1]
        if n>2:
            for i in range(n-2):
                lista.append(lista[i]+lista[i+1])
            print(lista)
        elif n==1:
            print("[0]")
        elif n==2:
            print(lista)
    
    pass

if __name__=='__main__':
    main()
