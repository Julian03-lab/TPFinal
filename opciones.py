from time import sleep
import tpgrupalbase

def movimientos(opcion, monto, divisa):
    ultimos_mov = ["Retiro de: 2300 Soles Peruanos.","Transferencia de: 200 Soles Peruanos","Retiro de: 182 Pesos Argentinos","Transferencia de: 1000 Pesos Argentinos"]
    if opcion == 1:
        ultimos_mov.append(f"Retiro de: {monto} {divisa}")
    elif opcion == 2:
        ultimos_mov.append(f"Transferencia de: {monto} {divisa}")
    if len(ultimos_mov) > 10:
        ultimos_mov.pop(0)

    return(ultimos_mov)

def imprimirTicket(lista):
    print("╔══════════════════════════════════════════╗")
    for element in lista:
        print(f"║{element.center(42)}║")
    print("╚══════════════════════════════════════════╝")

def consultas(saldo_pesos, saldo_soles):
    opcion_valida = True
    moneda_valida = True
    while opcion_valida:
            print("Seleccione una opcion: \n\n[1] Posicion GLOBAL \n[2] Movimientos")
            opcion = int(input("-> "))
            if opcion == 1:
                while moneda_valida:
                    moneda = int(input("Ingrese el tipo de moneda: [1. Soles] [2. Pesos] " ))
                    if moneda == 1:
                        divisa = "Soles Peruanos"
                        print("Eligio mostrar el saldo en Soles Peruanos (./S)")
                        opcion_valida = False
                        moneda_valida = False
                        visualizar_valido = True
                        while visualizar_valido:
                            visualizar_valido = saldo(saldo_soles, visualizar_valido, divisa)
                    elif moneda == 2:
                        divisa = "Pesos Argentinos"
                        print("Eligio mostrar el saldo en Pesos Argentinos ($S)")
                        opcion_valida = False
                        moneda_valida = False
                        visualizar_valido = True
                        while visualizar_valido:
                            visualizar_valido = saldo(saldo_pesos, visualizar_valido,divisa)
                    else:
                        print("Moneda incorrecta, ingrese una opcion valida.")
            if opcion == 2:
                visualizar_valido = True
                while visualizar_valido:
                    visualizar = int(input("Como desea visualizar la consulta?: \n\n[1] En pantalla \n[2] Imprimir reporte \n-> "))
                    if visualizar == 1:
                        for i in movimientos(0,0,0):
                            print(f"\n{i}")
                        visualizar_valido = False
                        input("Presiones [Enter] para continuar")
                    elif visualizar == 2:
                        print("Imprimiendo reporte...")
                        sleep(1)
                        visualizar_valido = False
                        imprimirTicket(movimientos(0,0,0))
                        input("Presiones [Enter] para continuar")

                    else: 
                        print("Opcion incorrecta.")

def saldo(saldo, visualizar_valido, divisa):
    saldo_lista = ["El" , "saldo", "disponible", "es de", str(saldo), divisa,]

    visualizar = int(input("Como desea visualizar la consulta?: \n\n[1] En pantalla \n[2] Imprimir reporte \n"))
    if visualizar == 1:
        print(f"El saldo disponible es de: \n {saldo} {divisa}")
        visualizar_valido = False
        input("Presiones [Enter] para continuar")
    elif visualizar == 2:
        print("Imprimiendo reporte...")
        sleep(1)
        imprimirTicket(saldo_lista)
        input("Presiones [Enter] para continuar")
        visualizar_valido = False
    else: 
        print("Opcion incorrecta.")
    return (visualizar_valido)

def retirar(saldo_pesos, saldo_soles, cont_clave,CLAVE):
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
                                print("Opcion invalida. Regresando al menu.")
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

def transferir(saldo_soles, saldo_pesos, cuenta_destino):
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