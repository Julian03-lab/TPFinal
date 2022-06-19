from time import sleep
import tpgrupalbase

def verificadorDeOpcion(opcion:int,limite:int):
    """
    Recibe un valor numerico que representa la cantidad de opciones validas. Retorna True si la opcion es valida y False si la opcion no es valida.
    """

    if opcion >= 1 and opcion <= limite:
        valido = True
    else:
        valido = False
    return(valido)

def movimientos(opcion:int, monto:float, divisa:str, lista_mov:list):
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

def imprimirTicket(lista:list):
    """
    Recibe una lista que sera imprimida en pantalla en formato Ticket.
    """

    print("╔══════════════════════════════════════════╗")
    for element in lista:
        print(f"║{element.center(42)}║")
    print("╚══════════════════════════════════════════╝")

def consultadorSaldo(saldo:float, visualizar:int, divisa:str):
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

def consultas(saldo_pesos:float, saldo_soles:float, lista_mov:list, opcion:int, moneda:int, visualizar:int):
    if verificadorDeOpcion(opcion, 2):
        if opcion == 1:
            if verificadorDeOpcion(moneda, 2):
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
            if verificadorDeOpcion(visualizar, 2):
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

def retiradorSaldo(monto:float, saldo:str ,divisa:str, voucher:int, lista_mov:list):
    """
    Toma como atributos el monto a retirar, el saldo que se modifica, la divisa con la que se trabaja, la opcion de voucher y una lista de movimientos.
    """
    saldo -= monto
    lista_mov = movimientos(1,monto, divisa, lista_mov)
    monto_correcto = False
    opcion_valida = True
    if voucher == 1:
        print("Imprimiendo Voucher...")
        sleep(1)
    print(f"Saldo retirado con exito.\nEl saldo disponible actual en {divisa} es: {saldo}")
    sleep(3)
    return(monto_correcto, opcion_valida)

def retirar(saldo_pesos:int, saldo_soles:int, cont_clave: int,CLAVE:int, lista_mov:list, moneda:int, monto:float, voucher:int):
    opcion_valida = False
    intento = 0
    if moneda == 1:
        monto_correcto = True
        while monto_correcto:
            if saldo_soles == 0:
                print("No tiene saldo disponible para realizar esta operacion.")
                sleep(1)
                monto_correcto = False
            else:
                if monto <= saldo_soles:
                    if tpgrupalbase.checkPassword(cont_clave, CLAVE):
                        monto_correcto,opcion_valida = retiradorSaldo(monto, saldo_soles,"Soles Peruanos", voucher, lista_mov)
                else:
                        print("\nSaldo incorrecto.\nRegresando al menu.")
                        opcion_valida = True
                        monto_correcto = False
                        sleep(2)
    elif moneda == 2:
        monto_correcto = True
        while monto_correcto:
            if saldo_pesos == 0:
                print("No tiene saldo disponible para realizar esta operacion.")
                sleep(1)
                monto_correcto = False
            else:
                if monto <= saldo_pesos:
                    if tpgrupalbase.checkPassword(cont_clave, CLAVE):
                        monto_correcto,opcion_valida = retiradorSaldo(monto, saldo_pesos,"Pesos Argentinos", voucher, lista_mov)
                else:
                        print("\nSaldo incorrecto.\nRegresando al menu.")
                        opcion_valida = True
                        monto_correcto = False
                        sleep(2)
    elif moneda == 3:
        print("Regresando al menu.")
        sleep(1)
        opcion_valida = True

    return([saldo_pesos,saldo_soles, opcion_valida])

def transferir(saldo_soles:int, saldo_pesos:int, cuenta_destino:int, lista_mov:list):
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
    retiradorSaldo()