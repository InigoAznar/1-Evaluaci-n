def bucle_10():
    #Suma de n�meros pares e impares
    nfinal= input("Hasta que n�mero quieres sumar?")
    for n�mero in range(1,nfinal+1):
        #para cada n�mero me pregunto si es par o impar
        if(n�mero%2==0):
            print n�mero," es par"
        else:
            print n�mero," es impar"

bucle_10()
