import os
from time import sleep
import opciones

#Pedimos la contraseña y verificamos si es correcta.
def checkPassword(cont_clave, clave_original):
    correct = True
    while cont_clave < 3:
        clave = int(input("Ingrese su clave: "))
        if clave == clave_original:
            cont_clave = 3
            correct = True
        else:
            cont_clave += 1
            print(f"Clave erronea. Lleva [{cont_clave}] intento de [3]")
            if cont_clave == 3:
                sleep(1)
                print("Clave erronea 3 veces, se retendra la tarjeta.")
                correct = False
    return(correct)

#Pedimos el DNI y verificamos si es correcto.
def checkDni(cont_dni, dni_original):
    correct = True
    while cont_dni < 3:
        dni = int(input("Ingrese su DNI: "))
        if dni == dni_original:
            cont_dni = 3
            correct = True
        else:
            cont_dni += 1
            print(f"DNI erroneo. Lleva [{cont_dni}] intento de [3]")
            if cont_dni == 3:
                sleep(1)
                print("DNI erroneo 3 veces, se retendra la tarjeta.")
                correct = False
    return(correct) 


    #Comienza el programa con la verificacion de la clave y el DNI.
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



    if checkPassword(cont_clave, CLAVE):
        if checkDni(cont_dni, DNI):
        #Si se verifico que ambos son correctos, mostramos el menu de opciones.
            while seguir:
                os.system ("cls")
                print("\nIngrese una opcion: \n\n[1] Consultas \n[2] Retiros \n[3] Transferencias \n[4] Salir" )
                opcion = int(input("\n-> "))
                if opcion == 1:
                    opciones.consultas(saldo_pesos,saldo_soles)
                elif opcion == 2:

                    os.system ("cls")
                    saldo_pesos, saldo_soles = opciones.retirar(saldo_pesos,saldo_soles,cont_clave,CLAVE)
                    
                elif opcion == 3:
                #Se modifican el saldo en soles y pesos en base al valor retornado por la funcion.
                    os.system ("cls")
                    saldo_pesos, saldo_soles = opciones.transferir(saldo_soles,saldo_pesos, CUENTA_DESTINO)
                    
                    
                elif opcion == 4:
                #Termina la ejecucion del programa.
                    os.system ("cls")
                    seguir = False
                    print("Transaccion finalizada. \nGracias por elegirnos ;)")
                    sleep(2)
                    print("Tarjeta devuelta.")
                else:
                    print("Opcion invalida.")


if __name__ == "__main__":
    program(checkPassword, checkDni)
