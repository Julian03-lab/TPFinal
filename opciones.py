from time import sleep
import tpgrupalbase

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
                        print("Eligio mostrar el saldo en Soles Peruanos (./S)")
                        opcion_valida = False
                        moneda_valida = False
                        visualizar_valido = True
                        while visualizar_valido:
                            visualizar = int(input("Como desea visualizar la consulta?: \n\n[1] En pantalla \n[2] Imprimir reporte \n"))
                            if visualizar == 1:
                                print(f"El saldo disponible es de: \n./S {saldo_soles} Soles Peruanos")
                                visualizar_valido = False
                                input("Presiones [Enter] para continuar")
                            elif visualizar == 2:
                                print("Imprimiendo reporte...")
                                sleep(1)
                                print(f"╔════════════════════╗\n║         El         ║\n║       saldo        ║\n║     disponible     ║\n║       es de        ║\n║{str(saldo_soles).center(20)}║\n║   Soles Peruanos   ║\n╚════════════════════╝")
                                input("Presiones [Enter] para continuar")
                                visualizar_valido = False
                            else: 
                                print("Opcion incorrecta.")
                    elif moneda == 2:
                        print("Eligio mostrar el saldo en Pesos Argentinos ($S)")
                        opcion_valida = False
                        moneda_valida = False
                        visualizar_valido = True
                        while visualizar_valido:
                            visualizar = int(input("Como desea visualizar la consulta?: \n\n[1] En pantalla \n[2] Imprimir reporte \n"))
                            if visualizar == 1:
                                print(f"El saldo disponible es de: \n$ {saldo_pesos} Pesos Argentinos")
                                input("Presiones [Enter] para continuar")
                                visualizar_valido = False
                            elif visualizar == 2:
                                print("Imprimiendo reporte...")
                                sleep(1)
                                print(f"╔════════════════════╗\n║         El         ║\n║       saldo        ║\n║     disponible     ║\n║       es de        ║\n║{str(saldo_pesos).center(20)}║\n║  Pesos Argentinos  ║\n╚════════════════════╝")
                                input("Presiones [Enter] para continuar")
                                visualizar_valido = False
                            else: 
                                print("Opcion incorrecta.")
                    else:
                        print("Moneda incorrecta, ingrese una opcion valida.")
            if opcion == 2:
                while moneda_valida:
                    movimiento = ["Movimientos:","Operacion Nro: 39115153.","Operacion Nro: 65158299.","Operacion Nro: 44592102.","Operacion Nro: 76424909.","Operacion Nro: 62110281.","Operacion Nro: 64438336.","Operacion Nro: 70095489.","Operacion Nro: XXXXXXXX.","Operacion Nro: XXXXXXXX.","Operacion Nro: XXXXXXXX."]
                    moneda = int(input("Ingrese el tipo de moneda: [1. Soles] [2. Pesos] " ))
                    if moneda == 1:
                        print("Eligio mostrar los movimientos en Soles Peruanos (./S)")
                        opcion_valida = False
                        moneda_valida = False
                        visualizar_valido = True
                        while visualizar_valido:
                            visualizar = int(input("Como desea visualizar la consulta?: \n\n[1] En pantalla \n[2] Imprimir reporte \n-> "))
                            if visualizar == 1:

                                for i in movimiento:
                                    print(f"\n{i}")
                                visualizar_valido = False
                                input("Presiones [Enter] para continuar")
                            elif visualizar == 2:
                                print("Imprimiendo reporte...")
                                sleep(1)
                                visualizar_valido = False
                                print(f"╔════════════════════════════════╗\n║{str(movimiento[0]).center(32)}║\n║                                ║\n║{str(movimiento[1]).center(32)}║\n║{str(movimiento[2]).center(32)}║\n║{str(movimiento[3]).center(32)}║\n║{str(movimiento[4]).center(32)}║\n║{str(movimiento[5]).center(32)}║\n║{str(movimiento[6]).center(32)}║\n║{str(movimiento[7]).center(32)}║\n║{str(movimiento[8]).center(32)}║\n║{str(movimiento[9]).center(32)}║\n║{str(movimiento[10]).center(32)}║\n║                                ║\n╚════════════════════════════════╝")
                                input("Presiones [Enter] para continuar")

                            else: 
                                print("Opcion incorrecta.")
                    elif moneda == 2:
                        print("Eligio mostrar los movimientos en Pesos Argentinos ($)")
                        opcion_valida = False
                        moneda_valida = False
                        visualizar_valido = True
                        while visualizar_valido:
                            visualizar = int(input("Como desea visualizar la consulta?: \n\n[1] En pantalla \n[2] Imprimir reporte \n-> "))
                            if visualizar == 1:
                                for i in movimiento:
                                    print(i)
                                visualizar_valido = False
                                input("Presiones [Enter] para continuar")
                            elif visualizar == 2:
                                print("Imprimiendo reporte...")
                                sleep(1)
                                visualizar_valido = False
                                print(f"╔════════════════════════════════╗\n║{str(movimiento[0]).center(32)}║\n║                                ║\n║{str(movimiento[1]).center(32)}║\n║{str(movimiento[2]).center(32)}║\n║{str(movimiento[3]).center(32)}║\n║{str(movimiento[4]).center(32)}║\n║{str(movimiento[5]).center(32)}║\n║{str(movimiento[6]).center(32)}║\n║{str(movimiento[7]).center(32)}║\n║{str(movimiento[8]).center(32)}║\n║{str(movimiento[9]).center(32)}║\n║{str(movimiento[10]).center(32)}║\n║                                ║\n╚════════════════════════════════╝")
                                input("Presiones [Enter] para continuar")

                            else: 
                                print("Opcion incorrecta.")
                    else:
                        print("Moneda incorrecta, ingrese una opcion valida.")

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