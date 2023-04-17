def main():
    #SE DEFINE LAS FUNCION "DATETIME" PARA PODER REGISTRAR HORAS Y FECHAS EN EL PROGRAMA
    #SE DEFINEN LAS VARIABLES NECESARIAS PARA LA FUNCIONALIDAD DEL PROGRAMA INICIAL, SE PUEDEN UTILIZAR MÁS DURANTE EL DESARROLLO DE SER NECESARIO
    while True:
        DatosCliente()
        
#1
def DatosCliente():
    NombreCliente=(input("Por Favor digite el nombre al cual desea que su factura sea registrada: "))
    Id_cliente=int(input("Favor digite el numero de cedula del cliente: "))
    TipoMueble()
    return NombreCliente,Id_cliente
    

#4
def PlazoPago(DiasEntrega,CostoUnidad):
    print('Seleccione el Plazo para el Pago del Articulo')
    Tipo_Plazo=int(input('Digite 1 para Contado\nDigite 2 para Credito'))
    print('Seleccione el tipo de pago')
    if Tipo_Plazo==1:
        print('Opcion de Contado tiene un descuento del 15%')
        Descuento=0.15
        PrecioDescontado=Descuento*CostoUnidad
        return PrecioDescontado
        
    elif Tipo_Plazo==2:
        PrecioDescontado=0
        DiasEntrega+=5
        print('Opcion de Credito no tiene Descuento')  
        return PrecioDescontado,DiasEntrega  
    else:
        Tipo_Plazo<1 or Tipo_Plazo>2
        print('Tipo de plazo no valido')
        main()
    FormaDePago()
#2 
def TipoMueble():
    print('Seleccione el mueble que desea comprar')
    Tipo_mueble=int(input("1)MESA \n2)ESCRITORIO \n3)MUEBLE COCINA "))
    if Tipo_mueble==1:
        CostoUnidad=50000
        DiasEntrega=2 
        Descripcion=str('Mesa')
        return CostoUnidad,DiasEntrega,Descripcion   

    elif Tipo_mueble==2:
        CostoUnidad=35000
        DiasEntrega=3
        Descripcion=str('Escritorio') 
        return CostoUnidad,DiasEntrega,Descripcion
    elif Tipo_mueble==3:
        CostoUnidad=250000
        DiasEntrega=4
        Descripcion=str("Mueble de Cocina")
        return CostoUnidad,DiasEntrega,Descripcion
    else:
        Tipo_mueble<1 or Tipo_mueble>3
        print('El Tipo de mueble no valido')
        main()
    maderas()
#3
def maderas(CostoUnidad):
    print('Ingrese la el tipo de madera')
    Tipo_Madera=int(input("1 Roble 1000 \n2 Pino 9000 \n3 Acacia 4585"))
    if Tipo_Madera==1:
        CostoUnidad+=1000
        PlazoPago()
    elif Tipo_Madera==2:
        CostoUnidad+=9000
        PlazoPago()
    elif Tipo_Madera==3:
        CostoUnidad+=4585
        PlazoPago()
    else:
        Tipo_Madera<1 or Tipo_Madera>3
        print("Tipo de madera no valido")
        main()


#5
def FormaDePago(Descuento,Descripcion,CostoUnidad,iva,CostoConIva):
    Tipo_Pago=int(input("1 Efectivo\n2 Tarjeta"))
    print('Articulo a cancelar: ',Descripcion)
    print('Total a pagar: ',CostoUnidad)
    print('Impuesto iva: ',iva)
    print('Monto Descontado', Descuento)
    CostoTotal=CostoConIva-Descuento
    print('Total a Pagar', CostoTotal)
    if Tipo_Pago==1:
        Efectivo=int(input('Ingrese el Monto Cancelado: '))
        Cambio=Efectivo-CostoTotal
        print('El cambio seria: ',Cambio)
        print("Pago Completado")
    elif Tipo_Pago==2:
        Tarjeta=int(input('Ingrese el monto a cancelar'))
        if Tarjeta!=CostoTotal:
            Tarjeta=int(input('El monto no puede ser diferente a al monto a cancelar'))
        else:
            print("Pago Completado")  
    Factura()  
#6
def ImpuestoIva(CostoUnidad):
    iva=CostoUnidad/0.13*100
    CostoConIva=CostoUnidad+iva
    return (CostoConIva,iva)
#7
def Factura():
    file=CrearFactura()    
    leerFactura(file)
#8
def CrearFactura(Consecutivo,NombreCliente,Id_cliente,DiasEntrega,Descripcion,CostoUnidad,iva,PrecioDescontado,CostoTotal):
    import datetime
    Consecutivo+=1
    Fecha_hora=datetime.datetime.now()
    Fact=str("Facuta#",Consecutivo,".txt")
    file=open(Fact,"a")
    file.write(f"====================",
               "FACTURA CLIENTE",
               "====================",
               "COMPAÑIA DE MUEBLES MUNDIAL S.A",
               "CEDULA JURIDICA: 3-101-000000",
               "TELEFONO: 800-MUNDIAL",
               "Fecha y hora de emision: ",Fecha_hora,
               "Documento Consecutivo: ",Consecutivo,
               "--------------------",
               "cliente: ",NombreCliente,
               "Identificacion: ",Id_cliente,
               "Su plazo es de: ",DiasEntrega,"Días",
               "--------------------",
               "DÍAS DE ENTREGA A PARTIR DE LA FECHA DE EMISION DE ESTE DOCUMENTO: ",DiasEntrega-1,
               "--------------------",
               "DESCRIPCION DEL MUEBLE: ",Descripcion,
               "--------------------",
               "SUBTOTAL: ",CostoUnidad,
               "DESCUENTO: ",PrecioDescontado,
               "I.V.A: ",iva,
               "TOTAL: ",CostoTotal,
               "--------------------")
    file.close
    main()
#9

def leerFactura(Fact):
    file=open(Fact,"r")
    datos=file.read()
    print(datos)
main()