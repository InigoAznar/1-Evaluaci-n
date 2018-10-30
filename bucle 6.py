def bucle_7():
    print "*****************************"
    print "*EL CONSTRUCTOR DE PIRÁMIDES*"
    print "*****************************"
    print "Indica, oh faraón, de que altura desea su pirámide. "
    altura=input ("altura = ")
    for fil in range(1,altura+1):
        for col in range(1,fil+1):
            print "*",
        print " "


bucle_7()
