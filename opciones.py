from time import sleep
import tpgrupalbase

def verificadorDeOpcion(opcion):
    """
    Recibe un valor numerico que representa la cantidad de opciones validas. Retorna True si la opcion es valida y False si la opcion no es valida.
    """

    if opcion == 1 or opcion == 2:
        valido = True
    else:
        valido = False
    return(valido)

def movimientos(opcion, monto, divisa, lista_mov):
    """
    Recibe un numero de opcion, un monto, la divisa que se desea y un historial de movimientos. Retorna la lista de movimientos modificada.
    """

    if opcion == 1:
        lista_mov.append(f"Retiro de: {monto} {divisa}")
    elif opcion == 2:
        lista_mov.append(f"Transferencia de: {monto} {divisa}")
    if len(lista_mov) > 10:
        lista_mov.pop(0)

    return(lista_mov)

def imprimirTicket(lista):
    """
    Recibe una lista que sera imprimida en pantalla en formato Ticket.
    """

    print("╔══════════════════════════════════════════╗")
    for element in lista:
        print(f"║{element.center(42)}║")
    print("╚══════════════════════════════════════════╝")

def consultadorSaldo(saldo, visualizar, divisa):
    """
    Recibe el saldo a mostrar, la opcion de como se visualizara y la divisa consultada y lo muestra en pantalla o en un ticket.
    """
    
    saldo_lista = ["El" , "saldo", "disponible", "es de", str(saldo), divisa,]
    if visualizar == 1:
        print(f"El saldo disponible es de: \n {saldo} {divisa}")
        sleep(3)
    elif visualizar == 2:
        print("Imprimiendo reporte...")
        sleep(1)
        imprimirTicket(saldo_lista)
        sleep(3)
    else: 
        print("Opcion de visualizar incorrecta, volviendo al menu.")
        sleep(2)

def consultas(saldo_pesos, saldo_soles, lista_mov, opcion, moneda, visualizar):
    if verificadorDeOpcion(opcion):
        if opcion == 1:
            if verificadorDeOpcion(moneda):
                    if moneda == 1:
                        print("Eligio mostrar el saldo en Soles Peruanos (./S)")
                        consultadorSaldo(saldo_soles, visualizar, "Soles Peruanos")
                    elif moneda == 2:
                        divisa = "Pesos Argentinos"
                        print("Eligio mostrar el saldo en Pesos Argentinos ($S)")
                        consultadorSaldo(saldo_pesos, visualizar, "Pesos Argentinos")
            else:
                print("\nMoneda incorrecta, volviendo al menu.")
                sleep(2)
        if opcion == 2:
            if verificadorDeOpcion(visualizar):
                if visualizar == 1:
                    print("\nMovimientos:\n")
                    for i in movimientos(0,0,0,lista_mov):
                        print(f"{i}\n")
                    sleep(3)
                elif visualizar == 2:
                    print("Imprimiendo reporte...")
                    sleep(1)
                    imprimirTicket(movimientos(0,0,0,lista_mov))
                    sleep(3)
            else: 
                print("\nOpcion incorrecta, volviendo al menu")
                sleep(2)

def retirar(saldo_pesos, saldo_soles, cont_clave,CLAVE, lista_mov):
    opcion_valida = True
    intento = 0
    while opcion_valida:
        moneda = int(input("Ingrese el tipo de moneda: [1. Soles] [2. Pesos] [3. Salir]" ))
        intento = 0
        if moneda == 1:
            monto_correcto = True
            while monto_correcto:
                if saldo_soles == 0:
                    print("No tiene saldo disponible para realizar esta operacion.")
                    monto_correcto = False
                else:
                    print(f"Saldo disponible en Soles: ./S {saldo_soles}")
                    print("Ingrese el monto a retirar: ")
                    monto = abs(int(input("\n->")))

                    if monto <= saldo_soles:
                        if tpgrupalbase.checkPassword(cont_clave, CLAVE):
                            
                            saldo_soles -= monto
                            lista_mov = movimientos(1,monto, "Soles Peruanos", lista_mov)
                            monto_correcto = False
                            opcion_valida = False
                            print("Desea imprimir voucher? \n[1] Si \n[2-9] No")
                            voucher = int(input("\n->"))
                            if voucher == 1:
                                print("Imprimiendo Voucher...")
                                sleep(2)
                            print(f"Saldo retirado con exito.\nEl saldo disponible actual en Soles es: ./S {saldo_soles}")
                            input("\nPresione [Enter] para continuar...")

                    else:
                        if intento == 0:
                            print("\nSaldo no disponible.\n\n[1] Volver a intentar. \n[2-9] Salir.")
                            sub_opcion = int(input("\n->"))
                            if sub_opcion == 1:
                                print("\nTienes un ultimo intento.")
                                intento += 1
                            else:
                                opcion_valida = False
                                monto_correcto = False
                                print("Regresando al menu.")
                                sleep(2)
                        else:
                            print("Opcion invalida. Regresando al menu.")
                            sleep(2)
                            opcion_valida = False
                            monto_correcto = False
        elif moneda == 2:
            monto_correcto = True
            while monto_correcto:
                if saldo_pesos == 0:
                    print("No tiene saldo disponible para realizar esta operacion.")
                    monto_correcto = False
                else:
                    print(f"Saldo disponible en Pesos: ${saldo_pesos}")
                    print("Ingrese el monto a retirar: ")
                    monto = abs(int(input("\n->")))
                    if monto <= saldo_pesos:
                        if tpgrupalbase.checkPassword(cont_clave, CLAVE):

                            saldo_pesos -= monto
                            lista_mov = movimientos(1,monto, "Pesos Argentinos", lista_mov)
                            monto_correcto = False
                            opcion_valida = False
                            print("Desea imprimir voucher? \n[1] Si \n[2-9] No")
                            voucher = int(input("\n->"))
                            if voucher == 1:
                                print("Imprimiendo Voucher...")
                                sleep(2)
                            print(f"Saldo retirado con exito.\nEl saldo disponible actual en Pesos es: ${saldo_pesos}")
                            input("\nPresione [Enter] para continuar...")
                    else:
                        if intento == 0:
                            print("\nSaldo no disponible.\n\n[1] Volver a intentar. \n[2-9] Salir.")
                            sub_opcion = int(input("\n->"))
                            if sub_opcion == 1:
                                print("\nTienes un ultimo intento.")
                                intento += 1
                            else:
                                opcion_valida = False
                                monto_correcto = False
                                print("Opcion invalida. Regresando al menu.")
                                sleep(2)
                        else:
                            print("Opcion invalida. Regresando al menu.")
                            sleep(2)
                            opcion_valida = False
                            monto_correcto = False
        elif moneda == 3:
            print("Regresando al menu.")
            sleep(1)
            opcion_valida = False
        else:
            print("Moneda incorrecta, ingrese una opcion valida.")

    return([saldo_pesos,saldo_soles])

def transferir(saldo_soles, saldo_pesos, cuenta_destino, lista_mov):
    '''
    Esta funcion recibe el saldo en soles, en pesos
    '''
    cuenta_mandar = int(input("Ingrese el numero de cuenta de destino: "))

    opcion_valida = True
    while opcion_valida:
        moneda = int(input("Ingrese el tipo de moneda: [1. Soles] [2. Pesos] [3. Salir]" ))
        if moneda == 1:
            monto_correcto = True
            while monto_correcto:
                if saldo_soles == 0:
                    print("No tiene saldo disponible para realizar esta operacion.")
                    monto_correcto = False
                else:
                    print(f"Saldo disponible en Soles: ./S {saldo_soles}")
                    print("Ingrese un monto valido para transferir: ")
                    monto = abs(int(input("\n->")))
                    if monto <= saldo_soles:
                        saldo_soles -= monto
                        lista_mov = movimientos(2,monto, "Soles Peruanos", lista_mov)
                        monto_correcto = False
                        opcion_valida = False

                        print(f"Saldo transferido con exito.\nEl saldo disponible actual en Soles es: ./S {saldo_soles}")
                        input("\nPresione [Enter] para continuar...")

        elif moneda == 2:
            monto_correcto = True
            
            while monto_correcto:
                if saldo_pesos == 0:
                    print("No tiene saldo disponible para realizar esta operacion.")
                    monto_correcto = False
                else:
                    print(f"Saldo disponible en Pesos: ${saldo_pesos}")
                    print("Ingrese un monto valido para transferir:")
                    monto = abs(int(input("\n->")))
                    if monto <= saldo_pesos:
                        saldo_pesos -= monto
                        lista_mov = movimientos(2,monto, "Pesos Argentinos", lista_mov)
                        monto_correcto = False
                        opcion_valida = False
                        print(f"Saldo transferido con exito.\nEl saldo disponible actual en Pesos es: ${saldo_pesos}")
                        input("Presione [Enter] para continuar")

        elif moneda == 3:
            print("Regresando al menu.")
            sleep(1)
            opcion_valida = False

        else:
            print("Moneda incorrecta, ingrese una opcion valida.")

    if cuenta_mandar != cuenta_destino and (moneda == 1 or moneda == 2):
        print("Cuenta invalida, su saldo se devolvera en 3 dias. Podra observar la devolucion en 'Movimientos'.")
        sleep(2)
    return([saldo_pesos,saldo_soles])

if __name__ == "__main__":
    consultas()
    retirar()
    transferir()
    movimientos()
    imprimirTicket()
    consultadorSaldo()