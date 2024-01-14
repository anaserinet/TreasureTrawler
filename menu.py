                      ###TREASURE TRAWLER v 0.0.2###
#Librerías importadas -----------------------------------------------------------------
import functions as fn
import levels as lvl
import start as st
import minijuego 
extra_money=0 #Se guardará un valor de dinero extra en caso de jugar un minijuego
#Cuerpo del juego --------------------------------------------------------------------
                            ### MENÚ PRINCIPAL ###

continua = False
while continua is False:  #Si termina el juego o si el usuario contesta algo inválido se repite la pregunta
    fn.clean()
    print(fn.amarillo(fn.subrayado(fn.texton("\t\tTREASURE TRAWLER"))))
    print("\n\t0.\t  Ver puntuaciones antiguas")
    print("\n\t1.\t  Nuevo Juego")
    print("\n\t2.\t  Minijuegos")
    print("\n\t3.\t  Créditos")
    print("\n\t4." + fn.rojo("\t  Salir"))
    opcion = int(input("\n\tElige un número: "))
     
    if opcion==0:
        fn.showPoints()
        fn.waitPress()
        fn.clean()
    
    elif opcion==1:  #Si escoge inicia un Nuevo Juego
        nombre=st.ng()  #Aquí mandamos a la función de comenzar el juego
        fn.waitPress()
        complete, money, equipment, equipment2, life = lvl.lvl1(nombre, extra_money)
        if(complete!=0):
            complete, money, equipment, equipment2, life = lvl.lvl2(money, equipment, equipment2, life, nombre) #Se obtienen las variables del jugador para pasarlas al siguiente nivel
            if(complete!=0):
                complete, money, equipment, equipment2, life = lvl.lvl3(money, equipment, equipment2, life, nombre) #Se obtienen las variables del jugador para pasarlas al siguiente nivel
                if(complete!=0):
                    complete, money, equipment, equipment2, life = lvl.lvl4(money, equipment, equipment2, life, nombre) #Se obtienen las variables del jugador para pasarlas al siguiente nivel
                    if(complete!=0):
                        complete, money, equipment, equipment2, life = lvl.lvl5(money, equipment, equipment2, life, nombre) #Se obtienen las variables del jugador para pasarlas al siguiente nivel
                        if(complete!=0):
                            fn.juegoTerminado(1,nombre,6,life,money)
    elif opcion==2: #si escoge minijuegos
        fn.clean()
        print(fn.texton("\n\n\n\n\t\t\tMinijuegos"),end="")
        fn.textolento(fn.texton("..."))
        continua2=True
        while continua2==True: #si selecciona algo mal se repite el ciclo
            fn.clean()
            continua3=int(input('MILLION DOLLAR QUESTION\n\n1. Continuar\n2. Menu principal\n\nEscriba su opción: ')) 
            if continua3==1: #si decide continuar, se manda al archivo
                continua2=False
                extra_money=minijuego.mini(continua3)
            elif continua3==2: #si quiere regresar al menu principal, se rompe el ciclo
                fn.clean()
                print(fn.texton("\n\n\n\n\t\t\tMenu principal"),end="")
                fn.textolento(fn.texton("..."))
                fn.time.sleep(2)
                fn.clean()
                break
            else: 
                fn.clean()
                print(
             '\n\n\n\nEsto no es una opcion, intente de nuevo.')  #Si la respuesta no es válida, se repite
                fn.time.sleep(2)
                fn.clean()

    elif opcion==3:  #Si escoge se muestrán los créditos
            fn.clean()
            print(fn.texton("\n\t\t\tCréditos"))
            fn.texto("""\n\tJuego elaborado por: 
    \nEdmundo Canedo Cervantes
    \nAna Clara Serinet Monteiro
    \nLuis Alfredo Carmona Martínez
    \nBraulio Fernando Antero Díaz
    """)
            fn.waitPress()
            fn.clean()

    elif opcion==4:  #Si escoge terminar el juego
        fn.clean()
        print(fn.texton("\n\n\n\n\t\t\tSaliendo"),end="")
        fn.textolento(fn.texton("..."))
        fn.clean()
        continua=True
        
  
    else:
        fn.clean()
        print(
          '\n\n\n\nEsto no es una opcion, intente de nuevo.')  #Si la respuesta no es válida, se repite
        fn.time.sleep(2)
        fn.clean()