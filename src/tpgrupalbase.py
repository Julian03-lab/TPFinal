import os
from time import sleep
import opciones as opciones

def checkPassword(cont_clave, clave_original):
    """
    Recibe como parámetro un contador para la clave y la clave correcta.
    Retorna un valor Booleano en relación a si la clave ingresada es correcta o incorrecta.
    """
    correct = True
    while cont_clave < 3:
        clave = int(input("Ingrese su clave.\n->"))
        if clave == clave_original:
            cont_clave = 3
            correct = True
        else:
            cont_clave += 1
            print(f"Clave errónea. Lleva [{cont_clave}] intento de [3]")
            if cont_clave == 3:
                sleep(1)
                print("Clave errónea 3 veces, se retendra la tarjeta.")
                correct = False
                print ("[Tarjeta retenida]")
                while True:
                    pass
    return(correct)

def checkDni(cont_dni, dni_original):
    """
    Recibe como parámetro un contador para el DNI y el DNI correcto.
    Retorna un valor Booleano en relación a si el DNI ingresado es correcto o incorrecto.
    """
    correct = True
    while cont_dni < 3:
        dni = int(input("Ingrese su DNI.\n-> "))
        if dni == dni_original:
            cont_dni = 3
            correct = True
        else:
            cont_dni += 1
            print(f"DNI erróneo. Lleva [{cont_dni}] intento de [3]")
            if cont_dni == 3:
                sleep(1)
                print("DNI erróneo 3 veces, se retendra la tarjeta.")
                correct = False
                print ("[Tarjeta retenida]")
                while True:
                    pass
    return(correct) 

def program(checkPassword, checkDni):
    #Declaro las constantes.
    CLAVE = 12345
    DNI = 12345678
    CUENTA_DESTINO = 98765

    #Declaro las variables que se utilizaran para el funcionamiento.
    saldo_pesos = 85000
    saldo_soles = 3564
    cont_clave = 0
    cont_dni = 0
    seguir = True

    ultimos_mov = ["Retiro de: 2300 Soles Peruanos.","Transferencia de: 200 Soles Peruanos","Retiro de: 182 Pesos Argentinos","Transferencia de: 1000 Pesos Argentinos","Transferencia de: 230 Soles Peruanos","Ingreso de: 2100 Pesos Argentinos","Retiro de: 200 Soles Peruanos","Transferencia de: 300 Pesos Argentinos","Ingreso de: 1000 Soles Peruanos"]

    if checkPassword(cont_clave, CLAVE):
        if checkDni(cont_dni, DNI):
        #Si se verifico que ambos son correctos, mostramos el menu de opciones.
            while seguir:
                os.system ("cls")
                opcion = int(input("\nIngrese una opcion: \n\n[1] Consultas \n[2] Retiros \n[3] Transferencias \n[4] Salir\n-> "))

                if opcion == 1:
                    moneda = None
                    visualizar = None
                    opcion_consulta = int(input("Seleccione una opcion: \n\n[1] Posición  GLOBAL \n[2] Movimientos\n-> "))
                    if opcion_consulta == 1:
                        moneda = int(input("Ingrese el tipo de moneda: [1. Soles] [2. Pesos]\n->" ))
                        visualizar = int(input("¿Como desea visualizar la consulta?: \n\n[1] En pantalla \n[2] Imprimir reporte \n"))
                    elif opcion_consulta == 2:
                        visualizar = int(input("¿Como desea visualizar la consulta?: \n\n[1] En pantalla \n[2] Imprimir reporte \n-> "))
                    else:
                        print("\nOpción incorrecta, regresando al menú.")
                        sleep(1)
                    opciones.consultas(saldo_pesos,saldo_soles, ultimos_mov, opcion_consulta, moneda, visualizar)
                
                elif opcion == 2:
                    monto = None
                    voucher = None
                    opcion_correcta = False
                    while opcion_correcta == False :
                        moneda = float(input("Ingrese el tipo de moneda: [1. Soles] [2. Pesos] [3. Salir]\n-> "))
                        if opciones.verificadorDeOpcion(moneda,3):
                            
                            if moneda == 1:
                                if saldo_soles > 0:
                                    print(f"Saldo disponible en Soles: ./S {saldo_soles}") 
                                    monto = abs(float(input("Ingrese el monto a retirar:\n->")))
                                    voucher = float(input("Desea imprimir voucher? \n[1] Si \n[2-9] No\n->"))
                            if moneda == 2:
                                if saldo_pesos > 0:
                                    print(f"Saldo disponible en Pesos: ${saldo_pesos}")
                                    monto = abs(float(input("Ingrese el monto a retirar:\n->")))
                                    voucher = float(input("Desea imprimir voucher? \n[1] Si \n[2-9] No\n->"))
                            os.system ("cls")
                            saldo_pesos, saldo_soles, opcion_correcta = opciones.retirar(saldo_pesos,saldo_soles,cont_clave,CLAVE, ultimos_mov, moneda, monto, voucher)
                        else:
                            print("Moneda incorrecta.")
    
                elif opcion == 3:
                #Se modifican el saldo en soles y pesos en base al valor retornado por la funcion.
                    cuenta_mandar = int(input("Ingrese el número  de cuenta de destino.\n->"))
                    monto = None
                    opcion_correcta = False
                    while opcion_correcta == False :
                        moneda = float(input("Ingrese el tipo de moneda: [1. Soles] [2. Pesos] [3. Salir]\n-> "))
                        if opciones.verificadorDeOpcion(moneda,3):
                            if moneda == 1:
                                if saldo_soles > 0:
                                    print(f"Saldo disponible en Soles: ./S {saldo_soles}") 
                                    monto = abs(float(input("Ingrese el monto a transferir:\n->")))
                            if moneda == 2:
                                if saldo_pesos > 0:
                                    print(f"Saldo disponible en Pesos: ${saldo_pesos}")
                                    monto = abs(float(input("Ingrese el monto a transferir:\n->")))
                            os.system ("cls")
                            saldo_pesos, saldo_soles, opcion_correcta = opciones.transferir(saldo_soles,saldo_pesos, CUENTA_DESTINO, ultimos_mov, cuenta_mandar, moneda, monto)
                        else:
                            print("Moneda incorrecta.")

                    
                elif opcion == 4:
                #Termina la ejecucion del programa.
                    os.system ("cls")
                    seguir = False
                    print("Transacción finalizada. \nGracias por elegirnos ;)")
                    sleep(2)
                    print("Tarjeta devuelta.")
                else:
                    print("Opción invalida.")

if __name__ == "__main__":
    program(checkPassword, checkDni)
