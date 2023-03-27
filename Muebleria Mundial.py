#SE BRINDA UN MENSAJE DE BIENVENIDA AL USUARIO
print("=================================================================================================================================")
print("Bienvenido al Programa de facturacion de Muebles Mundial")
print("================================================================================================================================= \n")

#SE DEFINE LAS FUNCION "DATETIME" PARA PODER REGISTRAR HORAS Y FECHAS EN EL PROGRAMA
import datetime

#SE DEFINEN LAS VARIABLES NECESARIAS PARA LA FUNCIONALIDAD DEL PROGRAMA INICIAL, SE PUEDEN UTILIZAR MÁS DURANTE EL DESARROLLO DE SER NECESARIO
consecutivo=0 #CONTADOR PARA EL CONSECUTIVO DE CADA FACTURA
   
while True:
   
    NombreCliente= (input("Por Favor digite el nombre al cual desea que su factura sea registrada \n"))
    Id_cliente= (input("Favor digite el numero de cedula del cliente \n"))
    Tipo_mueble= (input("1)MESA,\n2)ESCRITORIO,\n3)OTRO TIPO \nDigite el tipo de mueble segun corresponda \n"))
    Tipo_Madera= (input("Digite el tipo de madera solicitado para el mueble\n"))
    descripcion= (input("Digite la descripcion del mueble a solicitud \n"))
    Tipo_Pago= (input("Digite 1 para credito, 2 para contado, 3 para Tarjeta, 4 transferencias.\nDigite el tipo de pago\n"))
    plazo=0
    if Tipo_Pago==1:
        plazo=int(input("INDIQUE LOS DÍAS AUTORIZADOS PARA EL CREDITO"))
    else :
        plazo=0
    días_entrega=0
    #SE DEFINE LOS DÍAS DE ENTREGA SEGUN EL TIPO DE MUEBLE
    if Tipo_mueble==1:
        días_entrega=2   
    elif Tipo_mueble==2:
        días_entrega=3
    elif Tipo_mueble==3:
        días_entrega=4

    SubTotal= float(input("Digite el costo en colones de la solicitud, recuerde no incluir el I.V.A \n"))
    iva_Porcentaje=0.13
    iva=SubTotal*iva_Porcentaje
    PrecioFinal=SubTotal+iva

    print("================================================================================================================================= ")
    print("FACTURA CLIENTE")
    print("================================================================================================================================= \n")
    
    #Subparte de la factura presentada el cliente
    
    #SE MUESTRAN LOS DATOS DE LA EMPRESA
    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("COMPAÑIA DE MUEBLES MUNDIAL S.A \n""CEDULA JURIDICA: 3-101-000000 \n""TELEFONO: 800-MUNDIAL \n")
    consecutivo=consecutivo+1 #SE DEFINE UN CONSECUTIVO COMO IDENTIFICACION DEL DOCUMENTO
    Fecha_hora= datetime.datetime.now() #TOMARÁ LA FECHA Y HORA ACTUAL DEL EQUIPO 
    print("Fecha y hora de emision: ",Fecha_hora ) #MOSTRARA FECHA Y HORA ACTUAL
    print("documento Consecutivo: ", consecutivo) #NOS DARA UN NUMERO CONSECUTIVO DE LA FACTURA
    
    #SE MUESTRAN LOS DATOS DE EL CLIENTE
    print("---------------------------------------------------------------------------------------------------------------------------------")
    print("cliente: ",NombreCliente) #DATO CLIENTE "NOMBRE"
    print("Identificacion: ",Id_cliente) #DATOS CLIENTE "IDENTIFICACION FÍSICA O JURÍDICA"
    print("SU PLAZO ES DE: ",plazo, "DÍAS")
    print("---------------------------------------------------------------------------------------------------------------------------------")
    
    #SE DEFINE EL TIPO DE MUEBLE A COMPRAR PARA QUE QUEDE REGISTRADO EN LA FACTURA
    if Tipo_mueble==1:
        print("SU ORDEN POR: MESA""TIPO DE MADERA", Tipo_Madera)
    elif Tipo_mueble==2:
        print("SU ORDEN POR: ESCRITORIO""TIPO DE MADERA", Tipo_Madera)
    elif Tipo_mueble==3:
        print("SU ORDEN POR: OTRO""TIPO DE MADERA", Tipo_Madera)

    print("DÍAS DE ENTREGA A PARTIR DE LA FECHA DE EMISION DE ESTE DOCUMENTO: ",días_entrega)
    print("SUBTOTAL:", SubTotal)
    print("I.V.A: ",iva)
    print("TOTAL: ",PrecioFinal)
    print("\n================================================================================================================================= ")
    print("SIGUIENTE FACTURA \n")
    print("Bienvenido al Programa de facturacion de Muebles Mundial")
    print("================================================================================================================================= \n")