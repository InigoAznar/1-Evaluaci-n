def bucle_10():
    #Suma de números pares e impares
    nfinal= input("Hasta que número quieres sumar?")
    for número in range(1,nfinal+1):
        #para cada número me pregunto si es par o impar
        if(número%2==0):
            print número," es par"
        else:
            print número," es impar"

bucle_10()
