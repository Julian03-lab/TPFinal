from time import sleep
import tpgrupalbase as tpgrupalbase

def verificadorDeOpcion(opcion:int,limite:int):
    """
    Recibe un valor numérico que representa la cantidad de opciones válidas. Retorna True si la opción es válida y False si la opción no es válida.
    """

    if opcion >= 1 and opcion <= limite:
        valido = True
    else:
        valido = False
    return(valido)

def movimientos(opcion:int, monto:float, divisa:str, lista_mov:list):
    """
    Recibe un número de opción, un monto, la divisa que se desea y un historial de movimientos. Retorna la lista de movimientos modificada.
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
    Recibe una lista que será imprimida en pantalla en formato Ticket.
    """

    print("╔══════════════════════════════════════════╗")
    for element in lista:
        print(f"║{element.center(42)}║")
    print("╚══════════════════════════════════════════╝")

def consultadorSaldo(saldo:float, visualizar:int, divisa:str):
    """
    Recibe el saldo a mostrar, la opción de cómo se visualizará y la divisa consultada y lo muestra en pantalla o en un ticket.
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
        print("Opción de visualizar incorrecta, volviendo al menú.")
        sleep(2)

def consultas(saldo_pesos:float, saldo_soles:float, lista_mov:list, opcion:int, moneda:int, visualizar:int):
    """
    Esta función recibe el saldo de cuenta en Pesos argentinos y Soles peruanos, la lista de movimientos de la cuenta, los números de opciones, la moneda a consultar y la opción de visualizar. 
    """
    if verificadorDeOpcion(opcion, 2):
        if opcion == 1:
            if verificadorDeOpcion(moneda, 2):
                    if moneda == 1:
                        print("Eligio mostrar el saldo en Soles Peruanos (./S)")
                        consultadorSaldo(saldo_soles, visualizar, "Soles Peruanos")
                    elif moneda == 2:
                        print("Eligio mostrar el saldo en Pesos Argentinos ($S)")
                        consultadorSaldo(saldo_pesos, visualizar, "Pesos Argentinos")
            else:
                print("\nMoneda incorrecta, volviendo al menú.")
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
                print("\nOpción incorrecta, volviendo al menú")
                sleep(2)

def retiradorSaldo(monto:float, saldo:str ,divisa:str, voucher:int, lista_mov:list):
    """
    Toma como atributos el monto a retirar, el saldo que se modifica, la divisa con la que se trabaja, la opción de voucher y una lista de movimientos.
    """
    saldo -= monto
    lista_mov = movimientos(1,monto, divisa, lista_mov)
    monto_correcto = False
    opcion_valida = True
    if voucher == 1:
        print("Imprimiendo Voucher...")
        sleep(1)
    print(f"Saldo retirado con éxito.\nEl saldo disponible actual en {divisa} es: {saldo}")
    sleep(3)
    return(monto_correcto, opcion_valida, saldo)

def retirar(saldo_pesos:int, saldo_soles:int, cont_clave: int,CLAVE:int, lista_mov:list, moneda:int, monto:float, voucher:int):
    '''
    Esta función recibe el saldo de cuenta en Pesos argentinos y Soles peruanos, el contador de clave y la clave válida, una lista de movimientos, las opciones de monedas y voucher, y el monto a retirar
    Retorna una lista con el saldo de cuenta en Pesos argentinos y Soles peruanos actualizado.
    '''
    opcion_valida = False
    if moneda == 1:
        monto_correcto = True
        while monto_correcto:
            if saldo_soles == 0:
                print("No tiene saldo disponible para realizar esta operación.")
                sleep(1)
                monto_correcto = False
            else:
                if monto <= saldo_soles:
                    if tpgrupalbase.checkPassword(cont_clave, CLAVE):
                        monto_correcto,opcion_valida, saldo_soles = retiradorSaldo(monto, saldo_soles,"Soles Peruanos", voucher, lista_mov)
                else:
                        print("\nSaldo incorrecto.\nRegresando al menú.")
                        opcion_valida = True
                        monto_correcto = False
                        sleep(2)
    elif moneda == 2:
        monto_correcto = True
        while monto_correcto:
            if saldo_pesos == 0:
                print("No tiene saldo disponible para realizar esta operación.")
                sleep(1)
                monto_correcto = False
            else:
                if monto <= saldo_pesos:
                    if tpgrupalbase.checkPassword(cont_clave, CLAVE):
                        monto_correcto,opcion_valida,saldo_pesos = retiradorSaldo(monto, saldo_pesos,"Pesos Argentinos", voucher, lista_mov)
                else:
                        print("\nSaldo incorrecto.\nRegresando al menú.")
                        opcion_valida = True
                        monto_correcto = False
                        sleep(2)
    elif moneda == 3:
        print("Regresando al menú.")
        sleep(1)
        opcion_valida = True

    return([saldo_pesos,saldo_soles, opcion_valida])

def transferir(saldo_soles:int, saldo_pesos:int, cuenta_destino:int, lista_mov:list,cuenta_mandar:int, moneda:int, monto:float):
    '''
    Esta función recibe el saldo de cuenta en Pesos argentinos y Soles peruanos, la cuenta de destino correcta y la lista de movimientos de la cuenta. 
    Retorna una lista con el saldo de cuenta en Pesos argentinos y Soles peruanos actualizado.
    '''
    saldo_correcto = True
    opcion_valida = True
 
    if moneda == 1:
        if saldo_soles == 0:
            print("No tiene saldo disponible para realizar esta operación.")
            sleep(1)
            saldo_correcto = False
        else:
            if monto <= saldo_soles:
                saldo_soles -= monto
                lista_mov = movimientos(2,monto, "Soles Peruanos", lista_mov)
                opcion_valida = True
                print(f"Saldo transferido con éxito.\nEl saldo disponible en Soles es: ./S {saldo_soles}")
                sleep(3)
            else:
                print("\nSaldo incorrecto.\nRegresando al menú.")
                opcion_valida = True
                saldo_correcto = False
                sleep(2)
    elif moneda == 2:   
        if saldo_pesos == 0:
            print("No tiene saldo disponible para realizar esta operación.")
            sleep(1)
            saldo_correcto = False
        else:
            if monto <= saldo_pesos:
                saldo_pesos -= monto
                lista_mov = movimientos(2,monto, "Pesos Argentinos", lista_mov)
                opcion_valida = True
                print(f"Saldo transferido con éxito.\nEl saldo disponible  en Pesos Argentinos es: ${saldo_pesos}")
                sleep(3)
            else:
                print("\nSaldo incorrecto.\nRegresando al menú.")
                opcion_valida = True
                saldo_correcto = False
                sleep(2)
    elif moneda == 3:
        print("Regresando al menú.")
        sleep(1)
        opcion_valida = True

    if cuenta_mandar != cuenta_destino and (moneda == 1 or moneda == 2) and saldo_correcto == True:
        print("Cuenta invalida, su saldo se devolverá en 3 días. Podrá observar la devolucion en 'Movimientos'.")
        sleep(2)
        opcion_valida = True
    return([saldo_pesos,saldo_soles, opcion_valida])

if __name__ == "__main__":
    consultas()
    retirar()
    transferir()
    movimientos()
    imprimirTicket()
    consultadorSaldo()
    retiradorSaldo()