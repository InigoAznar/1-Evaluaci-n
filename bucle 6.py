def bucle_7():
    print "*****************************"
    print "*EL CONSTRUCTOR DE PIR�MIDES*"
    print "*****************************"
    print "Indica, oh fara�n, de que altura desea su pir�mide. "
    altura=input ("altura = ")
    for fil in range(1,altura+1):
        for col in range(1,fil+1):
            print "*",
        print " "


bucle_7()
