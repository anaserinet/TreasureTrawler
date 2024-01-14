#Librerías importadas-------------------------------------------------------
import functions as fn


#Función principal---------------------------------------------------------
                            #TIENDA
def shop(money,equipment, equipment2):
    continua=False
    while continua is False:
        print(fn.amarillo(fn.texton("\t\t\t\t\tTIENDA")))
        if equipment==0.60 and equipment2==1.25:
            print(
            "\nParece que ya tienes el mejor equipo, no hay nada más que comprar.")

        elif money>=500:
            if equipment==1:
                fn.textorapido(
                "\n1. Armadura de cartón (+10% defensa)\t\t\t$150")
            if equipment>=0.90:
                fn.textorapido(
                "\n2. Armadura de caballero vieja (+25% defensa)\t\t$300")
            if equipment>=0.75:
                fn.textorapido(
                "\n3. Armadura de acero (+40% defensa)\t\t\t\t$500")
            if equipment2==1:
                fn.textorapido(
                "\n4. Espada de la suerte(+25% Ganancias)\t\t\t$300")

        elif money>=300:
            if equipment==1:
                fn.textorapido(
                "\n1. Armadura de cartón (+10% defensa)\t\t\t$150\n")
            if equipment>=0.90:
                fn.textorapido(
                "\n2. Armadura de caballero vieja (+25% defensa)\t\t$300\n")
            if equipment>=0.75:
                fn.textorapido(fn.rojo(
                "\n3. Armadura de acero (+40% defensa)\t\t\t\t$500\n"))
            if equipment2==1:
                fn.textorapido(
                "\n4. Espada de la suerte(+25% Ganancias)\t\t\t$300\n")

        elif money>=150:
            if equipment==1:
                fn.textorapido(
                "\n1. Armadura de cartón (+10% defensa)\t\t\t$150\n")
            if equipment>=0.90:
                fn.textorapido(fn.rojo(
                "\n2. Armadura de caballero vieja (+25% defensa)\t\t$300\n"))
            if equipment>=0.75:
                fn.textorapido(fn.rojo(
                "\n3. Armadura de acero (+40% defensa)\t\t\t\t$500\n"))
            if equipment2==1:
                fn.textorapido(fn.rojo(
                "\n4. Espada de la suerte(+25% Ganancias)\t\t\t$300\n"))

        else:
            if equipment==1:
                fn.textorapido(fn.rojo(
                "\n1. Armadura de cartón (+10% defensa)\t\t\t$150\n"))
            if equipment>=0.90:
                fn.textorapido(fn.rojo(
                "\n2. Armadura de caballero vieja (+25% defensa)\t\t$300\n"))
            if equipment>=0.75:
                fn.textorapido(fn.rojo(
                "\n3. Armadura de acero (+40% defensa)\t\t\t\t$500\n"))
            if equipment2==1:
                fn.textorapido(fn.rojo(
                "\n4. Espada de la suerte(+25% Ganancias)\t\t\t$300\n"))

        fn.textorapido("\n\tTu dinero: " + fn.amarillo(f"${money}"))

                      # Elegir equipo
        opcion=str(input(
        "\n\nElige una opción para comprar o presione ENTER para regresar: "))
      
        if opcion=="":
            continua=True
            return money, equipment, equipment2

        elif opcion=="1" and equipment==1:
            if money>=150:
                money-=150
                equipment=0.90
                fn.clean()
                fn.texto(fn.verde(
                "\n\tCompraste una armadura de cartón."))
                fn.time.sleep(2)
                fn.clean()

            else:
                fn.clean()
                fn.texto(fn.rojo(
                "\n\n\n\n\n\t\t\tNo tienes suficiente dinero."))
                fn.time.sleep(2)
                fn.clean()

        elif opcion== "2" and equipment>=0.90:
            if money>=300:
                money-=300
                equipment=0.75
                fn.clean()
                fn.texto(fn.verde(
                "\n\tCompraste una armadura de caballero vieja."))
                fn.time.sleep(2)
                fn.clean()
            else:
                fn.clean()
                fn.texto(fn.rojo(
                "\n\n\n\n\n\t\t\tNo tienes suficiente dinero."))
                fn.time.sleep(2)
                fn.clean()

        elif opcion== "3" and equipment>=0.75:
            if money>=500:
                money-=500
                equipment=0.60
                fn.clean()
                fn.texto(fn.verde(
                "\n\tCompraste una armadura de acero."))
                fn.time.sleep(2)
                fn.clean()
            else:
                fn.clean()
                fn.texto(fn.rojo(
                "\n\n\n\n\n\t\t\tNo tienes suficiente dinero."))
                fn.time.sleep(2)
                fn.clean()

        elif opcion== "4" and equipment2==1:
            if money>=300:
                money-=300
                fn.clean()
                fn.texto(fn.verde(
                "\n\tCompraste una espada de la suerte."))
                fn.time.sleep(2)
                fn.clean()
            else:
                fn.clean()
                fn.texto(fn.rojo(
                "\n\n\n\n\n\t\t\tNo tienes suficiente dinero."))
                fn.time.sleep(2)
                fn.clean()
        else:
            fn.clean()
            fn.texto(fn.rojo(
            "\n\n\n\n\n\t\t\tOpción inválida."))
            fn.time.sleep(2)
            fn.clean()
            continua=True
    fn.clean()
    return money, equipment, equipment2