import os

#Variables o tuplas donde se almacenan respectivamente todos los tipos de datos del participante
nombres = []      #Variable donde se almacenan los nombres de los participantes.
sexos = []        #Variable donde se almacenan los nombres de los participantes.
edades = []       #Variable donde se almacenan las edades de los participantes.
pesos = []        #Variable donde se almacenan los pesos de los participantes.
tipodesangre = [] #Variable donde se almacenan los tipos de sangre.
dia = []          #Variable donde se almacenan los dias en los que los participantes asistieron.
apto = []         #Variable donde se almacena la eligibilidad del participante como donante.

i = 0 #Variable contador de los participantes.

#Bucle que abarca todo el programa.
while True:

    print('\n     /\ ')
    print('    /  \ ')
    print('   /____\   Algoritmo creado por Sebastian Ramirez: https://github.com/seborsevass')
    print('  /\    /\ ')
    print(' /  \  /  \ ')
    print('/____\/____\ \n')

#|=========================|#
#| PARTE '0' DEL ALGORITMO |#
#|=========================|#

    #Bucle para la introduccion de los participantes
    for j in range(1000):

        print('Introduzca los datos del participante\n')

        nom = input('Ingrese el nombre: ')      #Input donde el usuario introduce el nombre del participante.
        print("Nombre: " + str.capitalize(nom)) #Muestra por pantalla el nombre del participante.
        print("")
        nombres.append(nom)                     #Agrega el nombre de los participantes a la variable NOMBRES.

        #Bucle para la introduccion del sexo del participante
        while True:
            
            sex = input("Sexo:\nm) Masculino\nf) Femenino\n\nSeleccione el sexo: ") #Input donde el usuario elige su sexo
            if sex == "m":           #Si el usuario escribe 'm'
                print("Masculino\n") #muestra por pantalla 'Masculino'.
                break
            if sex == "f":           #Si el usuario escribe 'f'
                print("Femenino\n")  #muestra por pantalla 'Femenino'.
                break

            elif sex != "m" and sex != "f":               #Si el usuario no escribe ni 'm' ni 'f'
                print("\nSeleccione una opcion valida\n") #se repite el ciclo hasta que escriba 'm' o 'f'.

        if sex == "m" :               #Si el usuario escribio 'm' 
            sexos.append('masculino') #agrega 'masculino' a la variables SEXOS.
        if sex == "f":                #Si el usuario escribio 'f'
            sexos.append('femenino')  #agrega 'femenino' a la variable SEXOS.

        age = int(input("Ingrese la edad: ")) #Input donde el usuario introduce la edad del participante.
        print(str(age) + " años\n")           #Muestra por pantalla la edad del participante.
        edades.append(age)                    #Agrega la edad introducida por el usuario a la variable EDADES.

        wg = int(input("Ingrese el peso: ")) #Input donde el usuario introduce el peso del participante.
        print(str(wg) + "kg\n")              #Muestra por pantalla el peso en kilogramos del participante.
        pesos.append(wg)                     #Agrega la edad introducida por el usuario a la variables PESOS.

        #Bucle para la introduccion del tipo de sangre del participante
        while True:
            sangre = input("Tipos de sangre:\na) A \nb) B \nc) O \nd) AB \n\nSeleccione el tipo de sangre: ") #Input donde el usuario selecciona el tipo de sangre del participante
            if sangre == "a":                  #Si el usuario elige la opcion a)
                print("Tipo de sangre: A \n")  #muestra por pantalla 'Tipo de sangre A'
                break
            if sangre == "b":                  #Si el usuario elige la opcion b)
                print("Tipo de sangre: B \n")  #muestra por pantalla 'Tipo de sangre B'
                break
            if sangre == "c":                  #Si el usuario elige la opcion c)
                print("Tipo de sangre: O \n")  #muestra por pantalla 'Tipo de sangre O'
                break
            if sangre == "d":                  #Si el usuario elige la opcion d)
                print("Tipo de sangre: AB \n") #muestra por pantalla 'Tipo de sangre AB'
                break

            elif sangre != "a" and sangre != "b" and sangre != "c" and sangre != "d" : #Si el usuario no elige 'a', 'b', 'c', o 'd'
                print("\nSeleccione una opcion valida\n")                              #se repite el bucle hasta cumplirse las condiciones

        if sangre == "a" :            #Si el usuario eligio la opcion a)
            tipodesangre.append ('a') #agrega 'a' a la variable TIPODESANGRE.
        if sangre == "b" :            #Si el usuario eligio la opcion b)
            tipodesangre.append ('b') #agrega 'b' a la variable TIPODESANGRE.
        if sangre == "c" :            #Si el usuario eligio la opcion c)
            tipodesangre.append('c')  #agrega 'o' a la variable TIPODESANGRE.
        if sangre == "d" :            #Si el usuario eligio la opcion d)
            tipodesangre.append('ab') #agrega 'ab' a la variable TIPODESANGRE.

        #Bucle para la seleccion del dia de la semana en el que asistio el participante
        while True: 
            day = input("Dia de la semana:\na) Lunes \nb) Martes \nc) Miercoles \nd) Jueves \nf) Viernes\n\nSeleccione el dia en el que asistio: ") #Input donde el usuario selecciona el dia de la semana
            if day == "a":                           #Si el usuario elige 'a'
                print("Asistio el dia: Lunes\n")     #muestra por pantalla.
                break
            if day == "b":                           #Si el usuario elige 'b'
                print("Asistio el dia: Martes\n")    #muestra por pantalla.
                break
            if day == "c":                           #Si el usuario elige 'c'
                print("Asistio el dia: Miercoles\n") #muestra por pantalla.
                break
            if day == "d":                           #Si el usuario elige 'd'
                print("Asistio el dia: Jueves\n")    #muestra por pantalla.
                break
            if day == "f":                           #Si el usuario elige 'f'
                print("Asistio el dia: Viernes\n")   #muestra por pantalla.
                break

            elif day != "a" and day != "b" and day != "c" and day != "d" : #Si el usuario no elige 'a', 'b', 'c', 'd', o 'f'
                print("\nSeleccione una opcion valida\n")                  #se repite el bucle hasta cumplirse las condiciones

        if day == "a" :             #Si el usuario eligio 'a'
            dia.append('lunes')     #agrega 'lunes' a la variable DIA.
        if day == "b" :             #Si el usuario eligio 'b'
            dia.append('martes')    #agrega 'martes' a la variable DIA.
        if day == "c" :             #Si el usuario eligio 'c'
            dia.append('miercoles') #agrega 'miercoles' a la variable DIA.
        if day == "d" :             #Si el usuario eligio 'd'
            dia.append('jueves')    #agrega 'jueves' a la variable DIA.
        if day == "f" :             #Si el usuario eligio 'f'
            dia.append('viernes')   #agrega 'viernes' a la variable DIA.

    #DATOS DEL PARTICIPANTE
        print("Datos introducidos del participante:\n")
        print("-Numero del participante: " + str(i))                 #Muestra el numero del participante
        print("-Nombre: " + str.capitalize(nombres[i]))              #Muestra el nombre del participante
        print("-Sexo: " + str.capitalize(sexos[i]))                  #Muestra el sexo del participante
        print("-Edad: " + str(edades[i]) + " años")                  #Muestra la edad del participante
        print("-Peso: " + str(pesos[i]) + "kg")                      #Muestra el peso del participante en kilogramos
        print("-Tipo de sangre: " + str.capitalize(tipodesangre[i])) #Muestra el tipo de sangre del participante
        print("-Dia en el que asistio: " + str.capitalize(dia[i]))   #Muestra el dia en el que asistio el participante
        print('')

        i += 1 #Suma 1 a la variable del contador de participantes

        rep1 = input("Desea agregar otra persona? Si(s) No(n): ") #Input donde el usuario seleciona si quiere agregar otro participante o no. Si escribe 's' se reinicia el bucle
        print("")
        os.system('cls') #Comando para limpiar la consola
        if rep1 == 'n': #Si el usuario escribe 'n', sale del bucle
            os.system('cls')
            break

#|===============================|#
#| PARTE '1' O 'A' DEL ALGORITMO |#
#|===============================|#

    a = 0 #Contador para el bucle de aptitud

    #Bucle para comprobar la aptitud del participante como donante
    for j in range(i):

    #Si el participante es apto
        if int(edades[a]) >= 18 and int(edades[a]) <= 60 and int(pesos[a]) >= 50 : #Si la edad del participante es mayor o igual a 18 y menor o igual a 60, y su peso es mayor o igual a 50
            print("Participante " + str(a) + ': ' + str(nombres[a]) + " es apto(a) para donar sangre\n") #Muestra el numero y nombre del participante y si este es apto para donar 
            aptitud = 'si'       #Si es apto
            apto.append(aptitud) #agrega 'si' a la variable APTO.
            a += 1               #Suma 1 al contador de aptitud.

    #Si el participante no es apto       
        else:
            print("Participante " + str(a) + ': ' + str(nombres[a]) + " no es apto(a) para donar sangre\n") #Muestra el numero y nombre del participante y si este no es apto para donar
            aptitud  = 'no'      #Si no es apto
            apto.append(aptitud) #agrega 'no' a la variable APTO.
            a += 1               #Suma 1 al contador de aptitud.
    
#|===============================|#
#| PARTE '2' O 'B' DEL ALGORITMO |# 
#|===============================|#

    #VARIABLES DE LOS DONANTES DEL LUNES SEGUN SU TIPO DE SANGRE
    donlunA = 0  #Cantidad de donantes tipo A del lunes
    donlunB = 0  #Cantidad de donantes tipo B del lunes
    donlunO = 0  #Cantidad de donantes tipo O del lunes
    donlunAB = 0 #Cantidad de donantes tipo AB del lunes

    #VARIABLES DE LOS DONANTES DEL MARTES SEGUN SU TIPO DE SANGRE
    donmarA = 0  #Cantidad de donantes tipo A del martes
    donmarB = 0  #Cantidad de donantes tipo B del martes
    donmarO = 0  #Cantidad de donantes tipo O del martes
    donmarAB = 0 #Cantidad de donantes tipo AB del martes

    #VARIABLES DE LOS DONANTES DEL MIERCOLES SEGUN SU TIPO DE SANGRE
    donmieA = 0  #Cantidad de donantes tipo A del miercoles
    donmieB = 0  #Cantidad de donantes tipo B del miercoles
    donmieO = 0  #Cantidad de donantes tipo O del miercoles
    donmieAB = 0 #Cantidad de donantes tipo AB del miercoles

    #VARIABLES DE LOS DONANTES JUEVES SEGUN SU TIPO DE SANGRE
    donjueA = 0  #Cantidad de donantes tipo A del jueves
    donjueB = 0  #Cantidad de donantes tipo B del jueves
    donjueO = 0  #Cantidad de donantes tipo O del jueves
    donjueAB = 0 #Cantidad de donantes tipo AB del jueves

    #VARIABLES DE LOS DONANTES VIERNES SEGUN SU TIPO DE SANGRE
    donvieA = 0  #Cantidad de donantes tipo A del viernes
    donvieB = 0  #Cantidad de donantes tipo B del viernes
    donvieO = 0  #Cantidad de donantes tipo O del viernes
    donvieAB = 0 #Cantidad de donantes tipo AB del viernes

    #BUCLE PARA CALCULAR LOS DONANTES POR DIA Y POR SU TIPO DE SANGRE
    for l in range(i):

    #TIPO DE SANGRE A    
        if  dia[l] == 'lunes' and apto[l] == 'si' and tipodesangre[l] == 'a':    #Si el dia es lunes, es apto, y su tipo de sangre es A
            donlunA += 1                                                         #suma 1 a la variable de los donantes tipo A del lunes.
                
        if dia[l] == 'martes' and apto[l] == 'si' and tipodesangre[l] == 'a':    #Si el dia es martes, es apto, y su tipo de sangre es A
            donmarA += 1                                                         #suma 1 a la variable de los donantes tipo A del martes.

        if dia[l] == 'miercoles' and apto[l] == 'si' and tipodesangre[l] == 'a': #Si el dia es miercoles, es apto, y su tipo de sangre es A
            donmieA += 1                                                         #suma 1 a la variable de los donantes tipo A del miercoles.       

        if dia[l] == 'jueves' and apto[l] == 'si' and tipodesangre[l] == 'a':    #Si el dia es jueves, es apto, y su tipo de sangre es A
            donjueA += 1                                                         #suma 1 a la variable de los donantes tipo A del jueves.

        if dia[l] == 'viernes' and apto[l] == 'si' and tipodesangre[l] == 'a':   #Si el dia es viernes, es apto, y su tipo de sangre es A
            donvieA += 1                                                         #suma 1 a la variable de los donantes tipo A del viernes.

    #TIPO DE SANGRE B
        if  dia[l] == 'lunes' and apto[l] == 'si' and tipodesangre[l] == 'b':    #Si el dia es lunes, es apto, y su tipo de sangre es B
            donlunB += 1                                                         #suma 1 a la variable de los donantes tipo B del lunes.
                
        if dia[l] == 'martes' and apto[l] == 'si' and tipodesangre[l] == 'b':    #Si el dia es martes, es apto, y su tipo de sangre es B
            donmarB += 1                                                         #suma 1 a la variable de los donantes tipo B del martes.

        if dia[l] == 'miercoles' and apto[l] == 'si' and tipodesangre[l] == 'b': #Si el dia es miercoles, es apto, y su tipo de sangre es B
            donmieB += 1                                                         #suma 1 a la variable de los donantes tipo B del miercoles.

        if dia[l] == 'jueves' and apto[l] == 'si' and tipodesangre[l] == 'b':    #Si el dia es jueves, es apto, y su tipo de sangre es B
            donjueB += 1                                                         #suma 1 a la variable de los donantes tipo B del jueves.

        if dia[l] == 'viernes' and apto[l] == 'si' and tipodesangre[l] == 'b':   #Si el dia es viernes, es apto, y su tipo de sangre es B
            donvieB += 1                                                         #suma 1 a la variable de los donantes tipo B del viernes.

    #TIPO DE SANGRE O
        if  dia[l] == 'lunes' and apto[l] == 'si' and tipodesangre[l] == 'o':    #Si el dia es lunes, es apto, y su tipo de sangre es O
            donlunO += 1                                                         #suma 1 a la variable de los donantes tipo O del lunes.
                
        if dia[l] == 'martes' and apto[l] == 'si' and tipodesangre[l] == 'o':    #Si el dia es martes, es apto, y su tipo de sangre es O
            donmarO += 1                                                         #suma 1 a la variable de los donantes tipo O del martes.

        if dia[l] == 'miercoles' and apto[l] == 'si' and tipodesangre[l] == 'o': #Si el dia es miercoles, es apto, y su tipo de sangre es O
            donmieO += 1                                                         #suma 1 a la variable de los donantes tipo O del miercoles.

        if dia[l] == 'jueves' and apto[l] == 'si' and tipodesangre[l] == 'o':    #Si el dia es jueves, es apto, y su tipo de sangre es O
            donjueO += 1                                                         #suma 1 a la variable de los donantes tipo O del jueves.

        if dia[l] == 'viernes' and apto[l] == 'si' and tipodesangre[l] == 'o':   #Si el dia es viernes, es apto, y su tipo de sangre es O
            donvieO += 1                                                         #suma 1 a la variable de los donantes tipo O del viernes.

    #TIPO DE SANGRE AB
        if  dia[l] == 'lunes' and apto[l] == 'si' and tipodesangre[l] == 'ab':    #Si el dia es lunes, es apto, y su tipo de sangre es AB
            donlunAB += 1                                                         #suma 1 a la variable de los donantes tipo AB del lunes.
                
        if dia[l] == 'martes' and apto[l] == 'si' and tipodesangre[l] == 'ab':    #Si el dia es martes, es apto, y su tipo de sangre es AB
            donmarAB += 1                                                         #suma 1 a la variable de los donantes tipo AB del martes.

        if dia[l] == 'miercoles' and apto[l] == 'si' and tipodesangre[l] == 'ab': #Si el dia es miercoles, es apto, y su tipo de sangre es AB
            donmieAB += 1                                                         #suma 1 a la variable de los donantes tipo AB del miercoles.

        if dia[l] == 'jueves' and apto[l] == 'si' and tipodesangre[l] == 'ab':    #Si el dia es jueves, es apto, y su tipo de sangre es AB
            donjueAB += 1                                                         #suma 1 a la variable de los donantes tipo AB del jueves.

        if dia[l] == 'viernes' and apto[l] == 'si' and tipodesangre[l] == 'ab':   #Si el dia es viernes, es apto, y su tipo de sangre es AB
            donvieAB += 1                                                         #suma 1 a la variable de los donantes tipo AB del viernes.

    #DONANTES DEL TOTALES SEGUN EL DIA
    donlun = donlunA + donlunB + donlunO + donlunAB #Suma las variables de los donantes tipo A, B, O y AB del lunes
    donmar = donmarA + donmarB + donmarO + donmarAB #Suma las variables de los donantes tipo A, B, O y AB del martes
    donmie = donmieA + donmieB + donmieO + donmieAB #Suma las variables de los donantes tipo A, B, O y AB del miercoles
    donjue = donjueA + donjueB + donjueO + donjueAB #Suma las variables de los donantes tipo A, B, O y AB del jueves
    donvie = donvieA + donvieB + donvieO + donvieAB #Suma las variables de los donantes tipo A, B, O y AB del viernes

    #LITROS TOTALES DE LOS DONANTES TIPO A
    personasA = donlunA + donmarA + donmieA + donjueA + donvieA       #Suma de todas las variables de los donantes tipo A
    totalA = personasA * 0.5                                          #y las multiplica por 0.5 para los litros de sangre tipo A

    #LITROS TOTALES DE LOS DONANTES TIPO B
    personasB = donlunB + donmarB + donmieB + donjueB + donvieB       #Suma de todas las variables de los donantes tipo B
    totalB = personasB * 0.5                                          #y las multiplica por 0.5 para los litros de sangre tipo B

    #LITROS TOTALES DE LOS DONANTES TIPO O
    personasO = donlunO + donmarO + donmieO + donjueO + donvieO       #Suma de todas las variables de los donantes tipo O
    totalO = personasO * 0.5                                          #y las multiplica por 0.5 para los litros de sangre tipo O

    #LITROS TOTALES DE LOS DONANTES TIPO AB
    personasAB = donlunAB + donmarAB + donmieAB + donjueAB + donvieAB #Suma de todas las variables de los donantes tipo AB
    totalAB = personasAB * 0.5                                        #y las multiplica por 0.5 para los litros de sangre tipo AB

    totalpersonas = apto.count('si') #Busca cuantos 'si' hay dentro de la variable APTO y lo agrega a esta variable
    totalsangre = totalpersonas * 0.5 #Multiplica el total de personas por 0.5 para obtener los litros de sangre totales

    #PERSONAS DEL TIPO A DEL LUNES HASTA EL VIERNES
    print("Cantidades del tipo de sangre A:\n"
    + "-Lunes: "  + str(donlunA) + " personas donaron sangre\n"    #Muestra la cantidad de personas que donaron sangre tipo A el lunes
    + "-Martes: " + str(donmarA) + " personas donaron sangre\n"    #Muestra la cantidad de personas que donaron sangre tipo A el martes
    + "-Miercoles: " + str(donmieA) + " personas donaron sangre\n" #Muestra la cantidad de personas que donaron sangre tipo A el martes
    + "-Jueves: " + str(donjueA) + " personas donaron sangre\n"    #Muestra la cantidad de personas que donaron sangre tipo A el jueves
    + "-Viernes: " + str(donvieA) + " personas donaron sangre\n")  #Muestra la cantidad de personas que donaron sangre tipo A el viernes
    print(str(personasA) + " Personas del tipo de sangre A donaron un total de: " + str(totalA) + " litros de sangre esta semana\n")

    #PERSONAS DEL TIPO B DEL LUNES HASTA EL VIERNES
    print("Cantidades del tipo de sangre B:\n"
    + "-Lunes: "  + str(donlunB) + " personas donaron sangre\n"    #Muestra la cantidad de personas que donaron sangre tipo B el lunes
    + "-Martes: " + str(donmarB) + " personas donaron sangre\n"    #Muestra la cantidad de personas que donaron sangre tipo B el martes
    + "-Miercoles: " + str(donmieB) + " personas donaron sangre\n" #Muestra la cantidad de personas que donaron sangre tipo B el miercoles
    + "-Jueves: " + str(donjueB) + " personas donaron sangre\n"    #Muestra la cantidad de personas que donaron sangre tipo B el jueves
    + "-Viernes: " + str(donvieB) + " personas donaron sangre\n")  #Muestra la cantidad de personas que donaron sangre tipo B el viernes
    print(str(personasB) + " Personas del tipo de sangre B donaron un total de: " + str(totalB) + " litros de sangre esta semana\n")

    #PERSONAS DEL TIPO O DEL LUNES HASTA EL VIERNES
    print("Cantidades del tipo de sangre O:\n"
    + "-Lunes: "  + str(donlunO) + " personas donaron sangre\n"    #Muestra la cantidad de personas que donaron sangre tipo O el lunes
    + "-Martes: " + str(donmarO) + " personas donaron sangre\n"    #Muestra la cantidad de personas que donaron sangre tipo O el martes
    + "-Miercoles: " + str(donmieO) + " personas donaron sangre\n" #Muestra la cantidad de personas que donaron sangre tipo O el miercoles
    + "-Jueves: " + str(donjueO) + " personas donaron sangre\n"    #Muestra la cantidad de personas que donaron sangre tipo O el jueves
    + "-Viernes: " + str(donvieO) + " personas donaron sangre\n")  #Muestra la cantidad de personas que donaron sangre tipo O el viernes
    print(str(personasO) + " Personas del tipo de sangre O donaron un total de: " + str(totalO) + " litros de sangre esta semana\n")

    #PERSONAS DEL TIPO AB DEL LUNES HASTA EL VIERNES
    print("Cantidades del tipo de sangre AB:\n"
    + "-Lunes: "  + str(donlunAB) + " personas donaron sangre\n"    #Muestra la cantidad de personas que donaron sangre tipo AB el lunes
    + "-Martes: " + str(donmarAB) + " personas donaron sangre\n"    #Muestra la cantidad de personas que donaron sangre tipo AB el martes
    + "-Miercoles: " + str(donmieAB) + " personas donaron sangre\n" #Muestra la cantidad de personas que donaron sangre tipo AB el miercoles
    + "-Jueves: " + str(donjueAB) + " personas donaron sangre\n"    #Muestra la cantidad de personas que donaron sangre tipo AB el jueves
    + "-Viernes: " + str(donvieAB) + " personas donaron sangre\n")  #Muestra la cantidad de personas que donaron sangre tipo AB el viernes
    print(str(personasAB) + " Personas del tipo de sangre AB donaron un total de: " + str(totalAB) + " litros de sangre esta semana\n")

    #TOTAL DE PERSONAS Y LITROS DE SANGRE DONADOS
    if totalpersonas == 0:                                                                 #Si el total de personas que donaron sangre es 0
        print("Ninguna persona de ningun tipo de sangre dono sangre esta semana\n")        #muestra por pantalla.
    else:
        print(str(totalpersonas) + " Personas en total donaron sangre esta semana")        #Muestra por pantalla el total de personas que donaron sangre.
        print(str(totalsangre) + " Litros de sangre totales fueron donados esta semana\n") #Muestra por pantalla el total de litros de sangre donados.

#|===============================|#
#| PARTE '3' O 'C' DEL ALGORITMO |#
#|===============================|#

    #VARIABLES DE LAS SUMAS DE LOS PESOS DE LOS HOMBRES
    sumapesomar = 0 #Suma de los pesos del martes.
    sumapesojue = 0 #Suma de los pesos del jueves.
    sumapeso = 0    #Suma de los pesos del martes y jueves.
    numper = 0      #Suma de la cantidad de hombres del martes y jueves.
    numpermar = 0   #Suma de la cantidad de hombres del martes.
    numperjue = 0   #Suma de la cantidad de hombres del jueves

    #BUCLE PARA EL PROMEDIO DE HOMBRES QUE DONARON DESDE EL MARTES AL JUEVES
    for s in range(i):
                
        if dia[s] == 'martes' and apto[s] == 'si' and sexos[s] == 'masculino': #Si el dia es martes, es apto, y su sexo es masculino:
            sumapesomar += pesos[s]                                            #Suma el peso a la variable de la suma del martes.
            sumapeso += pesos[s]                                               #Suma el peso a la variable de la suma total de peso.
            numper += 1                                                        #Suma 1 a la cantidad de hombres totales.
            numpermar += 1                                                     #Suma 1 a la cantidad de hombres del martes.

        if dia[s] == 'jueves' and apto[s] == 'si' and sexos[s] == 'masculino': #Si el dia es jueves, es apto, y su sexo es masculino:
            sumapesojue += pesos[s]                                            #Suma el peso a la variable de la suma del jueves.
            sumapeso += pesos[s]                                               #Suma el peso a la variable de la suma total de peso.
            numper += 1                                                        #Suma 1 a la cantidad de hombres totales.
            numperjue += 1                                                     #Suma 1 a la cantidad de hombres del jueves.

    #VARIABLES DE LOS PROMEDIOS
    if sumapesomar == 0 and numpermar == 0:
        promediopesomar = 0
    else:
        promediopesomar = sumapesomar / numpermar #PROMEDIO DE LAS PERSONAS DEL MARTES

    if sumapesojue == 0 and numperjue == 0:    
        promediopesojue = 0
    else:
        promediopesojue = sumapesojue / numperjue #PROMEDIO DE LAS PERSONAS DEL JUEVES

    if sumapeso == 0 and numper == 0:
        promediopeso = 0
    else:    
        promediopeso = sumapeso / numper #PROMEDIO DE LAS PERSONAS DEL MARTES Y JUEVES

    print('Peso promedio de los hombres que donaron el martes: ' + str(promediopesomar) + 'kg')
    print('Peso promedio de los hombres que donaron el jueves: ' + str(promediopesojue) + 'kg')

    print('\nPeso promedio de los hombres que donaron el martes y miercoles: ' + str(promediopeso) + 'kg\n')

#|===============================|#
#| PARTE '4' O 'D' DEL ALGORITMO |#
#|===============================|#

    mujeres = [] #TUPLA DONDE SE ALMACENAN

    for g in range(i):
        if  sexos[g] == 'femenino' and apto[g] == 'si' and tipodesangre[l] == 'ab':
            pe = pesos[g]
            mujeres.append(pe)
            pesomenor = min(mujeres)
        else:
            pesomenor = 0

    print('El menor peso de las mujeres que donaron sangre del tipo AB es de: ' + str(pesomenor) + 'kg\n')

    resetproceso = input('Desea empezar el proceso desde el principio? Si(s) o No(n): ')
    os.system('cls')
    if resetproceso == 'n':
        break