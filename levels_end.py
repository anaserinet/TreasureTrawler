
import functions as fn
import tienda


def inter(complete, money, equipment, equipment2):
    fn.clean()
    print(fn.texton(
    f"\n\n\n\n\t\t¡Felicidades! Derrotaste el monstruo del nivel {complete}"))
    fn.time.sleep(3)
    fn.clean()
    continua=False
    while continua==False:
        print("\n\t1.\t  Abrir inventario")
        print("\n\t2.\t  Tienda")
        print("\n\n\t\t  Presiona ENTER para continuar\n")
        option=(input("\n"))
        if option=="1":
            fn.clean()
            print(fn.texton("\t\t\t\tInventario"))
            if equipment==1:
                fn.texto("\nNo tienes ninguna defensa equipada")
            elif equipment==0.90:
                fn.texto("\nEquipado: Armadura de cartón (10% defensa)")
            elif equipment==0.75:
                fn.texto("\nEquipado: Armadura de caballero vieja (25% defensa)")
            elif equipment==0.60:
                fn.texto("\nEquipado: Armadura de acero (40% defensa)")

            if equipment2==1.25:
                fn.texto(fn.amarillo("\nEspada de la suerte (+25% bonus)"))
            print("\n\n  Presiona ENTER para regresar\n")
            input("")
            fn.clean()
    
        if option=="2":
            fn.clean()
            money,equipment,equipment2=tienda.shop(money, equipment, equipment2)

        else:
            fn.clean()
            return money, equipment, equipment2
            continua=True
            

    return money, equipment, equipment2