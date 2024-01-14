#Librerías importadas -----------------------------------------------------------------
import functions as fn

#Cuerpo del juego ---------------------------------------------------------------------


def ng():  #inicio del juego: outputs: nombre(name),
    fn.clean()
    fn.texto(fn.texton('¡Hola jugador! ') + 'Bienvenido a TREASURE TRAWLER\n')

    verificacion=False
    while verificacion is False: #Si no le contesta si o no volverá a preguntar
        fn.texto(
            "¿Estás listo para empezar tu aventura? (si o no)\n\n")
        empezar = str(input("")).lower()
        lista=empezar.split()
        for i in range(len(lista)):
            if lista[i]=="si" or lista[i]=="sí":
                fn.clean()
                fn.texto(fn.texton(
                  "¡Excelente! ") + "Me agrada tu entusiasmo\n¿Cuál es tu nombre aventurero?\n\n")
                nombre = str(input())
                verificacion=True
                break
            elif lista[i]=="no":
                fn.clean()
                fn.texto(fn.texton('No me importa lo que quieras') + ', estás sometido a las reglas del juego dictadas por ' +  fn.texton('mí') + ', tu narrador.\n\n')
                fn.texto("Dame tu nombre: ")
                nombre = str(input())
                verificacion=True
                break
            elif i==len(lista)-1:
                fn.clean()
                fn.textolento('...')
                fn.texto(' Preguntaré otra vez\n')
    fn.clean()
    fn.texto(f'Bienvenido ' +  fn.texton(nombre) + ', te contaré lo que debes hacer en esta misión.\n')
    fn.time.sleep(2)
    fn.clean()
    fn.texto("Como guerrero, tendrás que enfrentarte a múltiples mounstros los cuales te atacarán.")
    fn.time.sleep(2)
    fn.clean()
    fn.texto("Por suerte, tienes como compañero a Merlín, un mago que mediante la resolución de problemas te dará el suficiente poder para vencerlos saliendo ileso.")
    fn.time.sleep(3)
    fn.clean()
    fn.texto('¿Parece bastante simple verdad?\nYo tambien me dejé engañar a un principio. Pero este juego no es para los débiles, y como todo en el mundo, tiene limitaciones, deja te lo explico... ')
    fn.time.sleep(3)
    fn.clean()
    fn.texto(fn.texton("Primero que nada, lanzarás un dado"))
    fn.time.sleep(2)
    fn.texto(
    '''
        - El número del dado serán las preguntas que deberás de contestar para pasar el nivel.
        - Merlín te dará el tipo de pregunta para contestar.
        - Si contestas mal, tendrás que enfrentarte por tu cuenta y probablemente te harán daño en el confrontamiento.
        - Los mounstros no son muy fuertes, probablemente no te vencerán a la primera pero procura no equivocarte mucho.
        - Si tu vida llega a 0, el monstruo correspondiente a tu nivel te destruirá y regresarás varios niveles.
        -Las preguntas se pondrán más dificiles conforme avanzan los niveles.
Suficiente charla, ya tendremos tiempo para eso. Empecemos
        ''')
    return (nombre)