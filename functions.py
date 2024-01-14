import os
import random
import time

from colorama import Fore as color

espera = time.sleep
frase = ""  #Aquí va el texto a imprimir con delay


def put(caracteres):  #ESCIRITURA PROGRESIVA
    print(caracteres, end='', flush=True)


def texto(caracteres):
    if 'TREASURE TRAWLER' in caracteres:
        caracteres = caracteres.replace('TREASURE TRAWLER', texton(amarillo('TREASURE TRAWLER')))
    if 'Merlín' in caracteres:
        caracteres = caracteres.replace('Merlín', texton(azul('Merlín')))
    if 'mounstros' in caracteres:
        caracteres = caracteres.replace('mounstros',texton(verde('mounstros')))
    if ' vida ' in caracteres:
        caracteres = caracteres.replace('vida', texton(rojo('vida')))
    for c in caracteres:
        largo = len(caracteres)
        put(c)
        espera(0.05-(min(largo, 1499)/1500)*0.05)
        largo = largo-1


def textorapido(caracteres):
    for c in caracteres:
        len(caracteres)
        put(c)
        espera(0.008)


def textolento(caracteres):
    for c in caracteres:
        len(caracteres)
        put(c)
        espera(0.5)


def texton(text):  ##TEXTO NEGRITAS
    bstart = "\033[1m"
    bend = "\033[0m"
    return bstart + text + bend


def subrayado(text):  ##SUBRAYADO
    bstart = "\033[4m"
    bend = "\033[0m"
    return bstart + text + bend


def amarillo(text):  ##COLOR AMARILLO
    bstart = color.LIGHTYELLOW_EX
    bend = color.RESET
    return bstart + text + bend


def verde(text):  ##COLOR VERDE
    bstart = color.GREEN
    bend = color.RESET
    return bstart + text + bend


def rojo(text):  ##COLOR ROJO
    bstart = color.RED
    bend = color.RESET
    return bstart + text + bend

def azul(text):  ##COLOR AZUL
    bstart = color.BLUE
    bend = color.RESET
    return bstart + text + bend


def rand(a, b): #Envés de obtener random de a...b-1 lo obtiene de a...b
    return random.randrange(a, b + 1)


def waitPress(): #Espera al usuario para continuar
    texto("Presione ENTER para continuar: ")
    input()


def clean(): #Limpia la consola
    os.system("clear")


def diceRoll(): #Se obtiene el valor del dado
    texto("Se va a rodar su dado\n")
    waitPress()
    r = rand(1, 6) #Genera el numero aleatorio
    texto("Su dado rodó " + str(r))
    texto(", por lo que tendrá que responder " + str(r) + " preguntas\n") #Indica al usuario la cantidad de preguntas a responder
    return r


def getQuestions(adress): #Devuelve los datos de las preguntas
    a = [] #Arreglo donde se guaran los datos
    f = open(adress, "r")
    txt = f.read()
    a = txt.split("##") #Se separa cada pregunta
    f.close()
    return a

def getSubject(): #Para no hacer tan repetitivo el juego marca si se escogió español o matemáticas de una forma más dinámica
    texto("Se le pidió al mago Merlín que escoja el tema de la pregunta\n")
    textolento("...\n")
    x = rand(1,2)
    excitement = rand(1, 5)
    time.sleep(1.5)
    clean()
    match excitement:
        case 1:
            texto("Pasó una mosca...\n")
            texto("Se sentó en un papelito...\n")
            texto("La mosca terminó decidiendo\n")
            texto("No pues... nada\n")
            if x == 1:
                texto("Salió mate, que chafa\n")
            else:
                texto("Salió español, que chafa\n")
        case 2:
            texto("Merlín trató y trató\n")
            texto("Y nomás no lo consiguió\n")
            texto("Se frustró mucho y se rindió\n")
            texto("Y a la suerte lo dejó\n")
            texto("Terminó tirando un dado . _.\n")
            if x == 1:
                texto("El dado mágico de Merlín dice que vayas con mates\n")
            else:
                texto("El dado mágico de Merlín dice que vayas con español\n")
        case 3:
            texto("Merlín pensó un rato y dijo: \n")
            texto("No pues..\n")
            if x == 1:
                textorapido("Las mates serán mijo, no hay de otra\n")
            else:
                textorapido("Español será mijo, no hay de otra\n")
        case 4:
            texto("Merlín caminó un rato\n")
            texto("Merlín se metió a una biblioteca\n")
            texto("Merlín agarró el primer libro que vió\n")
            texto("El libro decía...\n")
            if x == 1:
                textorapido("El destino habló y dijo, matemáticas serán\n")
            else:
                textorapido("El destino habló y dijo, español será\n")
            texto("Y si... todo eso dijo el libro\n")

        case 5:
            texto("Merlín, el mago más poderoso del reino, intentó crear un hechizo para facilitar la elección.\n")
            texto("Sin embargo, algo salió mal...\n")
            texto("En su intento de mejorar su magia, creó un portal a otra dimensión y se encontró dentro de un videojuego mágico.\n")
            texto("Para su sorpresa, se vio a sí mismo en el juego, luchando contra dragones y resolviendo enigmas mágicos.\n")
            texto("Merlín se quedó boquiabierto al encontrarse dentro del juego. Intentó regresar a casa, pero cruzó en el tiempo equivocado.\n")
            texto("De repente, se encontró en un mundo medieval, donde se enamoró perdidamente de una misteriosa dama del castillo.\n")
            texto("Juntos, tuvieron varios hijos y Merlín vivió una vida llena de alegría y amor.\n")
            texto("Sin embargo, con el tiempo, Merlín se dio cuenta de algo inquietante: ¡él era su propio nieto!\n")
            texto("La paradoja causada por su viaje en el tiempo lo atormentó, y se lamentó por su intento fallido de crear el hechizo perfecto.\n")
            texto("Se dió cuenta que nada de esto hubiese pasado si hubiera simplemente:\n")
            if x == 1:
                texto("Escogido matemáticas\n")
            else:
                texto("Escogido español\n")
        
        case 6:
            texto("Merlín se cansó de escoger...\n")
            texto("Se cansó de decidir...\n")
            texto("Llamó a su primo ayer...\n")
            texto("Para lo siguiente decir: nada\n")
            if x == 1:
                texto("Pues matemáticas\n")
            else:
                texto("Pues español\n")
    waitPress()    
    clean()
    return x

def developMath(question, answerPack, variables, r1, r2): #Desarrolla la ecuación en las preguntas matemáticas abiertas
    answerPack = answerPack.replace("$", "")
    variables = variables.split(" ") #Se obtienen las variables a utilizar
    for i in variables:
        xn = str(rand(r1,r2)) #Generación aleatorio de la variable
        question = question.replace(i,xn) #Se cambian los datos en la pregunta
        answerPack = answerPack.replace(i,xn) #Se cambian los datos en la ecuación a evaluar
    answer=eval(answerPack) #Se evalua la función
    return question, answer #Se regresa la función con la pregunta ya con las variables junto con la respuesta esperada

def juegoTerminado(completed, name, level, life, money): #Muestra los datos finales del usuario y los guarda
    print()
    if completed != 0: #Checa si el usuario ganó o no
        texto("Felicidades, has ganado el juego!\n")
    else:
        texto("Perdiste :c, el monstruo te mató\n")
    texto("Tu nombre es: "+name+"\n") #Imprime los datos del usuario
    texto("El nivel al que llegaste: "+str(level)+"\n")
    texto("Tu vida es: "+str(max(life,0))+"\n")
    texto("Tu dinero es: "+str(money)+"\n")
    f=open("puntuaciones.txt") #Se guardan los datos antiguos en una variable para escribir primero los nuevos y luego los viejso
    s=f.read()
    f.close()
    f=open("puntuaciones.txt","wt")
    f.write(name+"|"+str(level)+"|"+str(max(life,0))+"|"+str(money)+"\n")
    f.write(s)
    f.close()
    texto("Registrando datos y volviendo al menú principal: \n")
    waitPress()

def showPoints():
    clean()
    f=open("puntuaciones.txt")
    t=f.read()
    f.close()
    a=t.split("\n") #Se guarda una lista con los datos de los usuarios pasados
    m=[]
    for i in range(len(a)):
        vt=a[i].split("|") 
        m.append(vt) #se guarda la matriz dato por dato de los usaurios
    for i in range(len(m)):
        texto(m[i][0]+" ")
        if m[i][2]=="0": #Dependiendo si ganó o perdió se imprime un mensaje u otro
            texto("perdió")
        else:
            texto("ganó")
        texto(", llegó al nivel "+str(m[i][1])+" con $"+str(m[i][3])+"\n\n")