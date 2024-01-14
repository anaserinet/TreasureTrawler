import functions as fn
import levels_end as lvl_end

def lvl1(name, extra_money):
    complete=0 #Variable que marca si se pasó o no del nivel
    fn.clean()
    life = 100 #Se declara la vida del jugador
    money = 100+extra_money #Se declara el dinero del jugador
    equipment = 1 #Se declara el daño recibido del jugador
    equipment2 = 1 #Se declara el multiplicador del jugador
    bonus = 10 # Se declara el bonus por preguntas correctas seguidas
    fn.texto("Bienvenido a 4to de Primaria " + name +"\n")
    questions = int(fn.diceRoll()) #Se obtienen la cantidad de preguntas a responder
    questionsMath = fn.getQuestions("preguntasMat/prim4.txt") #Lista de preguntas de matemáticas
    questionsSpa = fn.getQuestions("preguntasEsp/prim4.txt") #Lista de preguntas de español
    usedMath = [] #Lista donde se guardarán los índices de las preguntas anteriormente utilizadas de matemáticas
    usedSpa = [] #Lista donde se guardarán los índices de las preguntas anteriormente utilizadas de español
    fn.time.sleep(1.5)
    fn.clean()
    for i in range(questions):
        fn.clean()
        fn.texto("Tiene "+fn.rojo(str(life))+" puntos de vida y "+fn.amarillo(str(money)+" monedas\n\n"))
        subject = fn.getSubject()
        checkQuestion = 0 #Variable que checa al final si se respondió correctamente o no la regunta
        if(subject == 1): #Matemáticas
            indexQuestion = fn.rand(1,len(questionsMath)-2)
            while indexQuestion in usedMath: #En caso de ser una preguta ya respondida busca otra pregunta nueva para responder
                indexQuestion = fn.rand(1, len(questionsMath)-2)
            question = questionsMath[indexQuestion].split("\n") #Separa las preguntas por saltos de linea
            if(len(question) == 5): #Pregunta abierta matemática
                questionText, answer = fn.developMath(question[1], question[2], question[3], 1, 20) #Manda la función que devuelve la pregunta y la respuesta
                fn.texto(questionText+"\n")
                userAnswer = float(input("Escriba su respuesta: "))
                answerMin = answer-0.2 #Añade margen al usuario en caso de que involucre decimales
                answerMax = answer+0.2
                if(answerMin <= userAnswer and userAnswer <= answerMax):
                    fn.texto("¡Correcto!\n")
                    checkQuestion = 1 #Actualiza el valor del checador
                else:
                    fn.texto("Lo lamento, respuesta incorrecta...\n")
                    fn.texto("La respuesta correcta era "+str(answer)+"\n")
            else: #Pregunta de opción múltiple
                usedMath.append(indexQuestion) #Se añade a la lista de preguntas ya usadas
                fn.texto(question[1]+"\n")
                for i in range(2, len(question)-2): #Pone el número de respuesta a cada una
                    fn.texto(str(i-1)+".- "+question[i]+"\n") 
                answer=question[len(question)-2] #Selecciona la pregunta correcta
                userAnswer = input("Escriba el número correspondiente a su respuesta: ") #Se obtiene la respuesta del usuario
                if(answer == userAnswer): #Verifica que tengan las mismas repuestas
                    fn.texto("¡Correcto!\n")
                    checkQuestion = 1 #Actualiza el valor del checador
                else:
                    fn.texto("Lo lamento, respuesta incorrecta...\n")
                    fn.texto("La respuesta correcta era "+str(answer)+"\n")
        else: #Es español
            indexQuestion = fn.rand(1,len(questionsSpa)-2) #Obtiene un índice random de la lista de preguntas
            while indexQuestion in usedSpa: #Checa si la pregunta ya se usó antes, en caso de que si escoge otro índice
                indexQuestion = fn.rand(1, len(questionsSpa)-2)
            question = questionsSpa[indexQuestion].split("\n") #Se obtienen los datos de la pregunta
            usedSpa.append(indexQuestion) #Se añade a la lista de preguntas que sa se usaron
            fn.texto(question[1]+"\n")
            for i in range(2, len(question)-2): #Se van imprimiendo una por una las posibles respuestas
                fn.texto(str(i-1)+".- "+question[i]+"\n") 
            answer=question[len(question)-2] #Se obtiene cual es la respuesta correcta
            userAnswer = input("Escriba el número correspondiente a su respuesta: ") #Se obtiente la respuesta del usuario
            if(answer == userAnswer): #Verifica que las respuestas sean las mismas
                fn.texto("¡Correcto!\n")
                checkQuestion = 1 #Actualiza el valor del checador
            else:
                fn.texto("Lo lamento, respuesta incorrecta...\n")
                fn.texto("La respuesta correcta era "+str(answer)+"\n")
        if(checkQuestion==1): #La respuesta era correcta
            money += bonus #Le suma al dinero el bonus
            bonus += 10 #Le suma al bonus 10
            life+=5 #Le suma a la vida 5
        else: #La respuesta era incorrecta
            life-=30 #Le resta a la vida 30
            bonus=10 #Resetea el bonus a 10
        if(life<=0): #Si la vida es menor o igual a 0
            fn.juegoTerminado(0,name,1,life,money)
            return complete, money, equipment, equipment2, life
        fn.waitPress()
        fn.clean()
    complete=1
    money, equipment, equipment2 = lvl_end.inter(complete, money, equipment, equipment2)
    return complete, money, equipment, equipment2, life

def lvl2(money, equipment, equipment2, life, name):
    complete=0 #Variable que marca si se pasó o no del nivel
    fn.clean()
    bonus = 10 # Se declara el bonus por preguntas correctas seguidas
    fn.texto("Bienvenido a 5to de Primaria " + name +"\n")
    questions = int(fn.diceRoll()) #Se obtienen la cantidad de preguntas a responder
    questionsMath = fn.getQuestions("preguntasMat/prim5.txt") #Lista de preguntas de matemáticas
    questionsSpa = fn.getQuestions("preguntasEsp/prim5.txt") #Lista de preguntas de español
    usedMath = [] #Lista donde se guardarán los índices de las preguntas anteriormente utilizadas de matemáticas
    usedSpa = [] #Lista donde se guardarán los índices de las preguntas anteriormente utilizadas de español
    fn.time.sleep(1.5)
    fn.clean()
    for i in range(questions):
        fn.clean()
        fn.texto("Tiene "+fn.rojo(str(life))+" puntos de vida y "+fn.amarillo(str(money)+" monedas\n\n"))
        subject = fn.getSubject()
        checkQuestion = 0 #Variable que checa al final si se respondió correctamente o no la regunta
        if(subject == 1): #Matemáticas
            indexQuestion = fn.rand(1,len(questionsMath)-2)
            while indexQuestion in usedMath: #En caso de ser una preguta ya respondida busca otra pregunta nueva para responder
                indexQuestion = fn.rand(1, len(questionsMath)-2)
            question = questionsMath[indexQuestion].split("\n") #Separa las preguntas por saltos de linea
            if(len(question) == 5): #Pregunta abierta matemática
                questionText, answer = fn.developMath(question[1], question[2], question[3], 1, 20) #Manda la función que devuelve la pregunta y la respuesta
                fn.texto(questionText+"\n")
                userAnswer = float(input("Escriba su respuesta: "))
                answerMin = answer-0.2 #Añade margen al usuario en caso de que involucre decimales
                answerMax = answer+0.2
                if(answerMin <= userAnswer and userAnswer <= answerMax):
                    fn.texto("¡Correcto!\n")
                    checkQuestion = 1 #Actualiza el valor del checador
                else:
                    fn.texto("Lo lamento, respuesta incorrecta...\n")
                    fn.texto("La respuesta correcta era "+str(answer)+"\n")
            else: #Pregunta de opción múltiple
                usedMath.append(indexQuestion) #Se añade a la lista de preguntas ya usadas
                fn.texto(question[1]+"\n")
                for i in range(2, len(question)-2): #Pone el número de respuesta a cada una
                    fn.texto(str(i-1)+".- "+question[i]+"\n") 
                answer=question[len(question)-2] #Selecciona la pregunta correcta
                userAnswer = input("Escriba el número correspondiente a su respuesta: ") #Se obtiene la respuesta del usuario
                if(answer == userAnswer): #Verifica que tengan las mismas repuestas
                    fn.texto("¡Correcto!\n")
                    checkQuestion = 1 #Actualiza el valor del checador
                else:
                    fn.texto("Lo lamento, respuesta incorrecta...\n")
                    fn.texto("La respuesta correcta era "+str(answer)+"\n")
        else: #Es español
            indexQuestion = fn.rand(1,len(questionsSpa)-2) #Obtiene un índice random de la lista de preguntas
            while indexQuestion in usedSpa: #Checa si la pregunta ya se usó antes, en caso de que si escoge otro índice
                indexQuestion = fn.rand(1, len(questionsSpa)-2)
            question = questionsSpa[indexQuestion].split("\n") #Se obtienen los datos de la pregunta
            usedSpa.append(indexQuestion) #Se añade a la lista de preguntas que sa se usaron
            fn.texto(question[1]+"\n")
            for i in range(2, len(question)-2): #Se van imprimiendo una por una las posibles respuestas
                fn.texto(str(i-1)+".- "+question[i]+"\n") 
            answer=question[len(question)-2] #Se obtiene cual es la respuesta correcta
            userAnswer = input("Escriba el número correspondiente a su respuesta: ") #Se obtiente la respuesta del usuario
            if(answer == userAnswer): #Verifica que las respuestas sean las mismas
                fn.texto("¡Correcto!\n")
                checkQuestion = 1 #Actualiza el valor del checador
            else:
                fn.texto("Lo lamento, respuesta incorrecta...\n")
                fn.texto("La respuesta correcta era "+str(answer)+"\n")
        if(checkQuestion==1) and life<=95: #La respuesta era correcta
            money += bonus*equipment2 #Le suma al dinero el bonus
            bonus += 10 #Le suma al bonus 10
            life+=5 #Le suma a la vida 5
        else: #La respuesta era incorrecta
            life-=35*equipment #Le resta a la vida 35
            bonus=10 #Resetea el bonus a 10
        if(life<=0): #Si la vida es menor o igual a 0
            fn.juegoTerminado(0,name,2,life,money)
            return complete, money, equipment, equipment2, life
        fn.waitPress()
        fn.clean()
    complete=2
    money, equipment, equipment2 = lvl_end.inter(complete, money, equipment, equipment2)
    return complete, money, equipment, equipment2, life

def lvl3(money, equipment, equipment2, life, name):
    complete=0 #Variable que marca si se pasó o no del nivel
    fn.clean()
    bonus = 10 # Se declara el bonus por preguntas correctas seguidas
    fn.texto("Bienvenido a 6to de Primaria " + name +"\n")
    questions = int(fn.diceRoll()) #Se obtienen la cantidad de preguntas a responder
    questionsMath = fn.getQuestions("preguntasMat/prim6.txt") #Lista de preguntas de matemáticas
    questionsSpa = fn.getQuestions("preguntasEsp/prim6.txt") #Lista de preguntas de español
    usedMath = [] #Lista donde se guardarán los índices de las preguntas anteriormente utilizadas de matemáticas
    usedSpa = [] #Lista donde se guardarán los índices de las preguntas anteriormente utilizadas de español
    fn.time.sleep(1.5)
    fn.clean()
    for i in range(questions):
        fn.clean()
        fn.texto("Tiene "+fn.rojo(str(life))+" puntos de vida y "+fn.amarillo(str(money)+" monedas\n\n"))
        subject = fn.getSubject()
        checkQuestion = 0 #Variable que checa al final si se respondió correctamente o no la regunta
        if(subject == 1): #Matemáticas
            indexQuestion = fn.rand(1,len(questionsMath)-2)
            while indexQuestion in usedMath: #En caso de ser una preguta ya respondida busca otra pregunta nueva para responder
                indexQuestion = fn.rand(1, len(questionsMath)-2)
            question = questionsMath[indexQuestion].split("\n") #Separa las preguntas por saltos de linea
            if(len(question) == 5): #Pregunta abierta matemática
                questionText, answer = fn.developMath(question[1], question[2], question[3], 1, 20) #Manda la función que devuelve la pregunta y la respuesta
                fn.texto(questionText+"\n")
                userAnswer = float(input("Escriba su respuesta: "))
                answerMin = answer-0.2 #Añade margen al usuario en caso de que involucre decimales
                answerMax = answer+0.2
                if(answerMin <= userAnswer and userAnswer <= answerMax):
                    fn.texto("¡Correcto!\n")
                    checkQuestion = 1 #Actualiza el valor del checador
                else:
                    fn.texto("Lo lamento, respuesta incorrecta...\n")
                    fn.texto("La respuesta correcta era "+str(answer)+"\n")
            else: #Pregunta de opción múltiple
                usedMath.append(indexQuestion) #Se añade a la lista de preguntas ya usadas
                fn.texto(question[1]+"\n")
                for i in range(2, len(question)-2): #Pone el número de respuesta a cada una
                    fn.texto(str(i-1)+".- "+question[i]+"\n") 
                answer=question[len(question)-2] #Selecciona la pregunta correcta
                userAnswer = input("Escriba el número correspondiente a su respuesta: ") #Se obtiene la respuesta del usuario
                if(answer == userAnswer): #Verifica que tengan las mismas repuestas
                    fn.texto("¡Correcto!\n")
                    checkQuestion = 1 #Actualiza el valor del checador
                else:
                    fn.texto("Lo lamento, respuesta incorrecta...\n")
                    fn.texto("La respuesta correcta era "+str(answer)+"\n")
        else: #Es español
            indexQuestion = fn.rand(1,len(questionsSpa)-2) #Obtiene un índice random de la lista de preguntas
            while indexQuestion in usedSpa: #Checa si la pregunta ya se usó antes, en caso de que si escoge otro índice
                indexQuestion = fn.rand(1, len(questionsSpa)-2)
            question = questionsSpa[indexQuestion].split("\n") #Se obtienen los datos de la pregunta
            usedSpa.append(indexQuestion) #Se añade a la lista de preguntas que sa se usaron
            fn.texto(question[1]+"\n")
            for i in range(2, len(question)-2): #Se van imprimiendo una por una las posibles respuestas
                fn.texto(str(i-1)+".- "+question[i]+"\n") 
            answer=question[len(question)-2] #Se obtiene cual es la respuesta correcta
            userAnswer = input("Escriba el número correspondiente a su respuesta: ") #Se obtiente la respuesta del usuario
            if(answer == userAnswer): #Verifica que las respuestas sean las mismas
                fn.texto("¡Correcto!\n")
                checkQuestion = 1 #Actualiza el valor del checador
            else:
                fn.texto("Lo lamento, respuesta incorrecta...\n")
                fn.texto("La respuesta correcta era "+str(answer)+"\n")
        if(checkQuestion==1) and life<=95: #La respuesta era correcta
            money += bonus*equipment2 #Le suma al dinero el bonus
            bonus += 10 #Le suma al bonus 10
            life+=5 #Le suma a la vida 5
        else: #La respuesta era incorrecta
            life-=35*equipment #Le resta a la vida 35
            bonus=10 #Resetea el bonus a 10
        if(life<=0): #Si la vida es menor o igual a 0
            fn.juegoTerminado(0,name,3,life,money)
            return complete, money, equipment, equipment2, life
        fn.waitPress()
        fn.clean()
    complete=3
    money, equipment, equipment2 = lvl_end.inter(complete, money, equipment, equipment2)
    return complete, money, equipment, equipment2, life

def lvl4(money, equipment, equipment2, life, name):
    complete=0 #Variable que marca si se pasó o no del nivel
    fn.clean()
    bonus = 10 # Se declara el bonus por preguntas correctas seguidas
    fn.texto("Bienvenido a 1ro de Secundaria " + name +"\n")
    questions = int(fn.diceRoll()) #Se obtienen la cantidad de preguntas a responder
    questionsMath = fn.getQuestions("preguntasMat/secu1.txt") #Lista de preguntas de matemáticas
    questionsSpa = fn.getQuestions("preguntasEsp/secu1.txt") #Lista de preguntas de español
    usedMath = [] #Lista donde se guardarán los índices de las preguntas anteriormente utilizadas de matemáticas
    usedSpa = [] #Lista donde se guardarán los índices de las preguntas anteriormente utilizadas de español
    fn.time.sleep(1.5)
    fn.clean()
    for i in range(questions):
        fn.clean()
        fn.texto("Tiene "+fn.rojo(str(life))+" puntos de vida y "+fn.amarillo(str(money)+" monedas\n\n"))
        subject = fn.getSubject()
        checkQuestion = 0 #Variable que checa al final si se respondió correctamente o no la regunta
        if(subject == 1): #Matemáticas
            indexQuestion = fn.rand(1,len(questionsMath)-2)
            while indexQuestion in usedMath: #En caso de ser una preguta ya respondida busca otra pregunta nueva para responder
                indexQuestion = fn.rand(1, len(questionsMath)-2)
            question = questionsMath[indexQuestion].split("\n") #Separa las preguntas por saltos de linea
            if(len(question) == 5): #Pregunta abierta matemática
                questionText, answer = fn.developMath(question[1], question[2], question[3], 1, 20) #Manda la función que devuelve la pregunta y la respuesta
                fn.texto(questionText+"\n")
                userAnswer = float(input("Escriba su respuesta: "))
                answerMin = answer-0.2 #Añade margen al usuario en caso de que involucre decimales
                answerMax = answer+0.2
                if(answerMin <= userAnswer and userAnswer <= answerMax):
                    fn.texto("¡Correcto!\n")
                    checkQuestion = 1 #Actualiza el valor del checador
                else:
                    fn.texto("Lo lamento, respuesta incorrecta...\n")
                    fn.texto("La respuesta correcta era "+str(answer)+"\n")
            else: #Pregunta de opción múltiple
                usedMath.append(indexQuestion) #Se añade a la lista de preguntas ya usadas
                fn.texto(question[1]+"\n")
                for i in range(2, len(question)-2): #Pone el número de respuesta a cada una
                    fn.texto(str(i-1)+".- "+question[i]+"\n") 
                answer=question[len(question)-2] #Selecciona la pregunta correcta
                userAnswer = input("Escriba el número correspondiente a su respuesta: ") #Se obtiene la respuesta del usuario
                if(answer == userAnswer): #Verifica que tengan las mismas repuestas
                    fn.texto("¡Correcto!\n")
                    checkQuestion = 1 #Actualiza el valor del checador
                else:
                    fn.texto("Lo lamento, respuesta incorrecta...\n")
                    fn.texto("La respuesta correcta era "+str(answer)+"\n")
        else: #Es español
            indexQuestion = fn.rand(1,len(questionsSpa)-2) #Obtiene un índice random de la lista de preguntas
            while indexQuestion in usedSpa: #Checa si la pregunta ya se usó antes, en caso de que si escoge otro índice
                indexQuestion = fn.rand(1, len(questionsSpa)-2)
            question = questionsSpa[indexQuestion].split("\n") #Se obtienen los datos de la pregunta
            usedSpa.append(indexQuestion) #Se añade a la lista de preguntas que sa se usaron
            fn.texto(question[1]+"\n")
            for i in range(2, len(question)-2): #Se van imprimiendo una por una las posibles respuestas
                fn.texto(str(i-1)+".- "+question[i]+"\n") 
            answer=question[len(question)-2] #Se obtiene cual es la respuesta correcta
            userAnswer = input("Escriba el número correspondiente a su respuesta: ") #Se obtiente la respuesta del usuario
            if(answer == userAnswer): #Verifica que las respuestas sean las mismas
                fn.texto("¡Correcto!\n")
                checkQuestion = 1 #Actualiza el valor del checador
            else:
                fn.texto("Lo lamento, respuesta incorrecta...\n")
                fn.texto("La respuesta correcta era "+str(answer)+"\n")
        if(checkQuestion==1) and life<=95: #La respuesta era correcta
            money += bonus*equipment2 #Le suma al dinero el bonus
            bonus += 10 #Le suma al bonus 10
            life+=5 #Le suma a la vida 5
        else: #La respuesta era incorrecta
            life-=35*equipment #Le resta a la vida 35
            bonus=10 #Resetea el bonus a 10
        if(life<=0): #Si la vida es menor o igual a 0
            fn.juegoTerminado(0,name,4,life,money)
            return complete, money, equipment, equipment2, life
        fn.waitPress()
        fn.clean()
    complete=4
    money, equipment, equipment2 = lvl_end.inter(complete, money, equipment, equipment2)
    return complete, money, equipment, equipment2, life

def lvl5(money, equipment, equipment2, life, name):
    complete=0 #Variable que marca si se pasó o no del nivel
    fn.clean()
    bonus = 10 # Se declara el bonus por preguntas correctas seguidas
    fn.texto("Bienvenido a 2do de Secundaria " + name +"\n")
    questions = int(fn.diceRoll()) #Se obtienen la cantidad de preguntas a responder
    questionsMath = fn.getQuestions("preguntasMat/secu2.txt") #Lista de preguntas de matemáticas
    questionsSpa = fn.getQuestions("preguntasEsp/secu2.txt") #Lista de preguntas de español
    usedMath = [] #Lista donde se guardarán los índices de las preguntas anteriormente utilizadas de matemáticas
    usedSpa = [] #Lista donde se guardarán los índices de las preguntas anteriormente utilizadas de español
    fn.time.sleep(1.5)
    fn.clean()
    for i in range(questions):
        fn.clean()
        fn.texto("Tiene "+fn.rojo(str(life))+" puntos de vida y "+fn.amarillo(str(money)+" monedas\n\n"))
        subject = fn.getSubject()
        checkQuestion = 0 #Variable que checa al final si se respondió correctamente o no la regunta
        if(subject == 1): #Matemáticas
            indexQuestion = fn.rand(1,len(questionsMath)-2)
            while indexQuestion in usedMath: #En caso de ser una preguta ya respondida busca otra pregunta nueva para responder
                indexQuestion = fn.rand(1, len(questionsMath)-2)
            question = questionsMath[indexQuestion].split("\n") #Separa las preguntas por saltos de linea
            if(len(question) == 5): #Pregunta abierta matemática
                questionText, answer = fn.developMath(question[1], question[2], question[3], 1, 20) #Manda la función que devuelve la pregunta y la respuesta
                fn.texto(questionText+"\n")
                userAnswer = float(input("Escriba su respuesta: "))
                answerMin = answer-0.2 #Añade margen al usuario en caso de que involucre decimales
                answerMax = answer+0.2
                if(answerMin <= userAnswer and userAnswer <= answerMax):
                    fn.texto("¡Correcto!\n")
                    checkQuestion = 1 #Actualiza el valor del checador
                else:
                    fn.texto("Lo lamento, respuesta incorrecta...\n")
                    fn.texto("La respuesta correcta era "+str(answer)+"\n")
            else: #Pregunta de opción múltiple
                usedMath.append(indexQuestion) #Se añade a la lista de preguntas ya usadas
                fn.texto(question[1]+"\n")
                for i in range(2, len(question)-2): #Pone el número de respuesta a cada una
                    fn.texto(str(i-1)+".- "+question[i]+"\n") 
                answer=question[len(question)-2] #Selecciona la pregunta correcta
                userAnswer = input("Escriba el número correspondiente a su respuesta: ") #Se obtiene la respuesta del usuario
                if(answer == userAnswer): #Verifica que tengan las mismas repuestas
                    fn.texto("¡Correcto!\n")
                    checkQuestion = 1 #Actualiza el valor del checador
                else:
                    fn.texto("Lo lamento, respuesta incorrecta...\n")
                    fn.texto("La respuesta correcta era "+str(answer)+"\n")
        else: #Es español
            indexQuestion = fn.rand(1,len(questionsSpa)-2) #Obtiene un índice random de la lista de preguntas
            while indexQuestion in usedSpa: #Checa si la pregunta ya se usó antes, en caso de que si escoge otro índice
                indexQuestion = fn.rand(1, len(questionsSpa)-2)
            question = questionsSpa[indexQuestion].split("\n") #Se obtienen los datos de la pregunta
            usedSpa.append(indexQuestion) #Se añade a la lista de preguntas que sa se usaron
            fn.texto(question[1]+"\n")
            for i in range(2, len(question)-2): #Se van imprimiendo una por una las posibles respuestas
                fn.texto(str(i-1)+".- "+question[i]+"\n") 
            answer=question[len(question)-2] #Se obtiene cual es la respuesta correcta
            userAnswer = input("Escriba el número correspondiente a su respuesta: ") #Se obtiente la respuesta del usuario
            if(answer == userAnswer): #Verifica que las respuestas sean las mismas
                fn.texto("¡Correcto!\n")
                checkQuestion = 1 #Actualiza el valor del checador
            else:
                fn.texto("Lo lamento, respuesta incorrecta...\n")
                fn.texto("La respuesta correcta era "+str(answer)+"\n")
        if(checkQuestion==1) and life<=95: #La respuesta era correcta
            money += bonus*equipment2 #Le suma al dinero el bonus
            bonus += 10 #Le suma al bonus 10
            life+=5 #Le suma a la vida 5
        else: #La respuesta era incorrecta
            life-=35*equipment #Le resta a la vida 35
            bonus=10 #Resetea el bonus a 10
        if(life<=0): #Si la vida es menor o igual a 0
            fn.juegoTerminado(0,name,5,life,money)
            return complete, money, equipment, equipment2, life
        fn.waitPress()
        fn.clean()
    complete=5
    money, equipment, equipment2 = lvl_end.inter(complete, money, equipment, equipment2)
    return complete, money, equipment, equipment2, life