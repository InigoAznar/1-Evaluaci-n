def intercambio_dinero():
    euros=input("Buenos dias se�or �Cuanto dinero desea cambiar? ")
    respuesta=raw_input("�En que desea el cambio (dolares/libras)?")
    if(respuesta== "dolares"):
        moneda_nueva=euros*1.15
        unidades="dolares"
    else:
        moneda_nueva=euros*0.80
        unidades="libras"
    print "Bueno se�or, son en total"+moneda_nueva+ unidades

intercambio_dinero()
