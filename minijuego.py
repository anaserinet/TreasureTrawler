                      ###TREASURE TRAWLER v 0.0.2###
#Librerías importadas -----------------------------------------------------------------
import random 
import functions as fn
import random

#Cuerpo del juego --------------------------------------------------------------------  
                      #MINIJUEGO
def mini(x): 
    counter=0
    points=0
    usadosCultura=[]
    fn.clean()
    fn.texto("\n\n\nBienvenido al minijuego " + fn.texton('MILLION DOLLAR QUESTION\n'))
    fn.clean()
    fn.texto('''Las reglas consisten en lo siguiente:
    \t- Responde una pregunta
    \t- Si contestas 2 preguntas correctamente te llevarás una cantidad de dinero aleatoria.\n''')
    fn.time.sleep(1)
    fn.clean()
    fn.texto('Pero cuidado con el monstruo de la moneda él ama el dinero\n')
    fn.time.sleep(2)
    fn.clean()
    winning=True
    while points<2:
        counter+=1
        fn.texto(fn.texton(f"\t\t\tPregunta no. {counter}"))
        fn.texto("Se tienen "+ fn.texton(str(points)+" puntos\n"))
        fn.texto("\n1. Cultura general\n\n2. Regresar al menu principal\n")
        juego=int(input("\nSeleccione el número de su opción: "))
        fn.time.sleep(1)
        if juego==1: 
            print("Escogiste 'Cultura general'")
            fn.clean()
            questionsCultura = fn.getQuestions("miniPreg/PregCG.txt") 
            fn.clean()
            fn.texto(fn.texton(f"\n\n\n\n\t\t\t Pregunta {counter}: Cultura general"))
            fn.textolento(fn.texton("..."))
            fn.clean()
            indexQuestion = fn.rand(1,len(questionsCultura)-2)
            while indexQuestion in usadosCultura:
                indexQuestion = fn.rand(1, len(questionsCultura)-2) 
            question = questionsCultura[indexQuestion].split("\n")
            usadosCultura.append(indexQuestion)
            fn.texto(question[1]+"\n")
            for i in range(2, len(question)-2):
                fn.texto(str(i-1)+".- "+question[i]+"\n")
            answer=question[len(question)-2]
            userAnswer = input("Escriba el número correspondiente a su respuesta: ")
            if(answer == userAnswer):
                points+=1
                fn.clean()
                fn.texto(fn.texton(f"\n\n\n\n\t\t\t  La opción {userAnswer} es"))
                fn.textolento(fn.texton("..."))
                fn.texto(fn.texton('\n\n\n\n\t\t\t\t\tCORRECTA\n'))
                fn.waitPress()
                fn.clean()
            else:
                fn.clean()
                fn.texto(fn.texton(f"\n\n\n\n\t\t\t\t\t  La opción {userAnswer} es"))
                fn.textolento(fn.texton("..."))
                fn.texto(fn.texton('\n\n\n\n\t\t\tINCORRECTA\n'))
                fn.texto("La respuesta correcta era "+str(answer)+"\n")
                fn.waitPress()
                fn.time.sleep(2)
                fn.clean()

        else: #Prefirió volver al menú
            return 0
            
    fn.texto('¡FELICIDADES!\n\nhas contestado las 2 preguntas correctamente\n\n')
    fn.textolento(fn.texton("..."))
    fn.clean()
    fn.texto('Es hora de que recibas tu premio\n\n')
    fn.textolento(fn.texton("..."))
    fn.clean()
    fn.texto('La ruleta rodó y cayó en')
    fn.textolento(fn.texton("..."))
    dinero=random.randint(0,101)
    print(f'{dinero}\n\n')
    fn.waitPress()
    return dinero
            
              
        