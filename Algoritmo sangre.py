import os

#VARIABLES QUE ALMACENAN LOS DATOS = TUPLAS
nombres = []
sexos = []
edades = []
pesos = []
tipodesangre = []
dia = []
apto = []

#CONTADOR DE LOS PARTICIPANTES
i = 0

while True:

#|===============================|#
#| PARTE '1' O 'A' DEL ALGORITMO |#
#|===============================|#

#BUCLE PARA LA CREACION DE LOS PARTICIPANTES
    for j in range(1000):

        print('Introduzca los datos del participante\n')

    #INTRODUCCION DEL NOMBRE
        nom = input('Ingrese el nombre: ')
        print("Nombre: " + str.capitalize(nom))
        print("")
        nombres.append(nom)

    #INTRODUCCION DEL SEXO
        while True:
            
            sex = input("Sexo:\nm) Masculino\nf) Femenino\n\nSeleccione el sexo: ")
            if sex == "m":
                print("Masculino\n")
                break
            if sex == "f":
                print("Femenino\n")
                break

    #SI EL USUARIO INTRODUCE ALGO QUE NO SEA M O F
            elif sex != "m" and sex != "f":
                print("\nSeleccione una opcion valida\n")

        if sex == "m" :
            sexos.append('masculino')
        if sex == "f":
            sexos.append('femenino')

    #INTRODUCCION DE LA EDAD
        age = int(input("Ingrese la edad: "))
        print(str(age) + " años\n")
        edades.append(age)

    #INTRODUCCION DEL PESO
        wg = int(input("Ingrese el peso: "))
        print(str(wg) + "kg\n")
        pesos.append(wg)

    #INTRODUCCION DEL TIPO DE SANGRE
        while True:
            sangre = input("Tipos de sangre:\na) A \nb) B \nc) O \nd) AB \n\nSeleccione el tipo de sangre: ")
            if sangre == "a":
                print("Tipo de sangre: A \n")
                break
            if sangre == "b":
                print("Tipo de sangre: B \n")
                break
            if sangre == "c":
                print("Tipo de sangre: O \n")
                break
            if sangre == "d":
                print("Tipo de sangre: AB \n")
                break

    #SI EL USUARIO INTRODUCE ALGO QUE NO SEA A, B, C, D
            elif sangre != "a" and sangre != "b" and sangre != "c" and sangre != "d" :
                print("\nSeleccione una opcion valida\n")

    #AGREGA EL TIPO DE SANGRE A LA TUPLA CORRESPONDIENTE
        if sangre == "a" :
            tipodesangre.append ('a')
        if sangre == "b" :
            tipodesangre.append ('b')
        if sangre == "c" :
            tipodesangre.append('c')
        if sangre == "d" :
            tipodesangre.append('ab')

    #SELECCION DEL DIA DE LA SEMANA
        while True:
            day = input("Dia de la semana:\na) Lunes \nb) Martes \nc) Miercoles \nd) Jueves \nf) Viernes\n\nSeleccione el dia en el que asistio: ")
            if day == "a":
                print("Asistio el dia: Lunes\n")
                break
            if day == "b":
                print("Asistio el dia: Martes\n")
                break
            if day == "c":
                print("Asistio el dia: Miercoles\n")
                break
            if day == "d":
                print("Asistio el dia: Jueves\n")
                break
            if day == "f":
                print("Asistio el dia: Viernes\n")
                break

            elif day != "a" and day != "b" and day != "c" and day != "d" :
                print("\nSeleccione una opcion valida\n")

    #AGREGA EL DIA A LA VARIABLE CORRESPONDIENTE
        if day == "a" :
            dia.append('lunes')
        if day == "b" :
            dia.append('martes')
        if day == "c" :
            dia.append('miercoles')
        if day == "d" :
            dia.append('jueves')
        if day == "f" :
            dia.append('viernes')

    #DATOS DEL PARTICIPANTE
        print("Datos introducidos del participante:\n")
        print("-Numero del participante: " + str(i))
        print("-Nombre: " + str.capitalize(nombres[i]))
        print("-Sexo: " + str.capitalize(sexos[i]))
        print("-Edad: " + str(edades[i]) + " años") 
        print("-Peso: " + str(pesos[i]) + "kg")
        print("-Tipo de sangre: " + str.capitalize(tipodesangre[i]))
        print("-Dia en el que asistio: " + str.capitalize(dia[i]))
        print('')

    #CONTADOR DE LOS PARTICIPANTES
        i += 1

    #REINTENTO 
        rep1 = input("Desea agregar otra persona? Si(s) No(n): ")
        print("")
        os.system('cls')
        if rep1 == 'n':
            os.system('cls')
            break

    #CONTADOR PARA EL BUCLE DE LA APTITUD DE DONANTE
    a = 0

    #BUCLE PARA COMPROBAR LA APTITUD DE DONANTE
    for j in range(i):

    #SI ES APTO
        if int(edades[a]) >= 18 and int(edades[a]) <= 60 and int(pesos[a]) >= 50 :
            print("Participante " + str(a) + ': ' + str(nombres[a]) + " es apto(a) para donar sangre\n")
            aptitud = 'si'
            apto.append(aptitud)
            a += 1

    #SI NO ES APTO        
        else:
            print("Participante " + str(a) + ': ' + str(nombres[a]) + " no es apto(a) para donar sangre\n")
            aptitud  = 'no'
            apto.append(aptitud)
            a += 1
    
#===============================#
# PARTE '2' O 'B' DEL ALGORITMO # 
#===============================#

    #VARIABLES DE LOS DONANTES DEL LUNES
    donlunA = 0
    donlunB = 0
    donlunO = 0
    donlunAB = 0

    #VARIABLES DE LOS DONANTES DEL MARTES
    donmarA = 0
    donmarB = 0
    donmarO = 0
    donmarAB = 0

    #VARIABLES DE LOS DONANTES DEL MIERCOLES
    donmieA = 0
    donmieB = 0
    donmieO = 0
    donmieAB = 0

    #VARIABLES DE LOS DONANTES JUEVES
    donjueA = 0
    donjueB = 0
    donjueO = 0
    donjueAB = 0

    #VARIABLES DE LOS DONANTES VIERNES
    donvieA = 0
    donvieB = 0
    donvieO = 0
    donvieAB = 0

    #BUCLE PARA CALCULAR LOS DONANTES POR DIA Y POR SU TIPO DE SANGRE
    for l in range(i):

    #TIPO DE SANGRE A    
        if  dia[l] == 'lunes' and apto[l] == 'si' and tipodesangre[l] == 'a': #A LUNES
            donlunA += 1
                
        if dia[l] == 'martes' and apto[l] == 'si' and tipodesangre[l] == 'a': #A MARTES
            donmarA += 1

        if dia[l] == 'miercoles' and apto[l] == 'si' and tipodesangre[l] == 'a': #A MIERCOLES
            donmieA += 1

        if dia[l] == 'jueves' and apto[l] == 'si' and tipodesangre[l] == 'a': #A JUEVES
            donjueA += 1

        if dia[l] == 'viernes' and apto[l] == 'si' and tipodesangre[l] == 'a': #A VIERNES
            donvieA += 1

    #TIPO DE SANGRE B
        if  dia[l] == 'lunes' and apto[l] == 'si' and tipodesangre[l] == 'b': #B LUNES
            donlunB += 1
                
        if dia[l] == 'martes' and apto[l] == 'si' and tipodesangre[l] == 'b': #B MARTES
            donmarB += 1

        if dia[l] == 'miercoles' and apto[l] == 'si' and tipodesangre[l] == 'b': #B MIERCOLES
            donmieB += 1

        if dia[l] == 'jueves' and apto[l] == 'si' and tipodesangre[l] == 'b': #B JUEVES
            donjueB += 1

        if dia[l] == 'viernes' and apto[l] == 'si' and tipodesangre[l] == 'b': #B VIERNES
            donvieB += 1

    #TIPO DE SANGRE O
        if  dia[l] == 'lunes' and apto[l] == 'si' and tipodesangre[l] == 'o': #O LUNES
            donlunO += 1
                
        if dia[l] == 'martes' and apto[l] == 'si' and tipodesangre[l] == 'o': #O MARTES
            donmarO += 1

        if dia[l] == 'miercoles' and apto[l] == 'si' and tipodesangre[l] == 'o': #O MIERCOLES
            donmieO += 1

        if dia[l] == 'jueves' and apto[l] == 'si' and tipodesangre[l] == 'o': #O JUEVES
            donjueO += 1

        if dia[l] == 'viernes' and apto[l] == 'si' and tipodesangre[l] == 'o': #O VIERNES
            donvieO += 1

    #TIPO DE SANGRE AB
        if  dia[l] == 'lunes' and apto[l] == 'si' and tipodesangre[l] == 'ab':
            donlunAB += 1
                
        if dia[l] == 'martes' and apto[l] == 'si' and tipodesangre[l] == 'ab':
            donmarAB += 1

        if dia[l] == 'miercoles' and apto[l] == 'si' and tipodesangre[l] == 'ab':
            donmieAB += 1

        if dia[l] == 'jueves' and apto[l] == 'si' and tipodesangre[l] == 'ab':
            donjueAB += 1

        if dia[l] == 'viernes' and apto[l] == 'si' and tipodesangre[l] == 'ab':
            donvieAB += 1

    #DONANTES DEL TOTALES SEGUN EL DIA
    donlun = donlunA + donlunB + donlunO + donlunAB #LUNES
    donmar = donmarA + donmarB + donmarO + donmarAB #MARTES
    donmie = donmieA + donmieB + donmieO + donmieAB #MIERCOLES
    donjue = donjueA + donjueB + donjueO + donjueAB #JUEVES
    donvie = donvieA + donvieB + donvieO + donvieAB #VIERNES

    #LITROS TOTALES DE LOS DONANTES TIPO A
    personasA = donlunA + donmarA + donmieA + donjueA + donvieA #SUMA DE LOS TIPO A
    totalA = personasA * 0.5

    #LITROS TOTALES DE LOS DONANTES TIPO B
    personasB = donlunB + donmarB + donmieB + donjueB + donvieB #SUMA DE LOS TIPO B
    totalB = personasB * 0.5

    #LITROS TOTALES DE LOS DONANTES TIPO O
    personasO = donlunO + donmarO + donmieO + donjueO + donvieO #SUMA DE LOS TIPO O
    totalO = personasO * 0.5

    #LITROS TOTALES DE LOS DONANTES TIPO AB
    personasAB = donlunAB + donmarAB + donmieAB + donjueAB + donvieAB #SUMA DE LOS TIPO AB
    totalAB = personasAB * 0.5

    totalpersonas = apto.count('si') #VARIABLE PARA VER LA CANTIDAD TOTAL DE PERSONAS APTAS (personasA + personasB + personasO + personasAB)
    totalsangre = totalpersonas * 0.5 #VARIABLES PARA LA CANTIDAD TOTAL DE TODOS LOS TIPOS DE SANGRE

    #PERSONAS DEL TIPO A DEL LUNES HASTA EL VIERNES
    print("Cantidades del tipo de sangre A:\n"
    + "-Lunes: "  + str(donlunA) + " personas donaron sangre\n"
    + "-Martes: " + str(donmarA) + " personas donaron sangre\n" 
    + "-Miercoles: " + str(donmieA) + " personas donaron sangre\n" 
    + "-Jueves: " + str(donjueA) + " personas donaron sangre\n" 
    + "-Viernes: " + str(donvieA) + " personas donaron sangre\n")
    print(str(personasA) + " Personas del tipo de sangre A donaron un total de: " + str(totalA) + " litros de sangre esta semana\n")

    #PERSONAS DEL TIPO B DEL LUNES HASTA EL VIERNES
    print("Cantidades del tipo de sangre B:\n"
    + "-Lunes: "  + str(donlunB) + " personas donaron sangre\n"
    + "-Martes: " + str(donmarB) + " personas donaron sangre\n" 
    + "-Miercoles: " + str(donmieB) + " personas donaron sangre\n" 
    + "-Jueves: " + str(donjueB) + " personas donaron sangre\n" 
    + "-Viernes: " + str(donvieB) + " personas donaron sangre\n")
    print(str(personasB) + " Personas del tipo de sangre A donaron un total de: " + str(totalB) + " litros de sangre esta semana\n")

    #PERSONAS DEL TIPO O DEL LUNES HASTA EL VIERNES
    print("Cantidades del tipo de sangre O:\n"
    + "-Lunes: "  + str(donlunO) + " personas donaron sangre\n"
    + "-Martes: " + str(donmarO) + " personas donaron sangre\n" 
    + "-Miercoles: " + str(donmieO) + " personas donaron sangre\n" 
    + "-Jueves: " + str(donjueO) + " personas donaron sangre\n" 
    + "-Viernes: " + str(donvieO) + " personas donaron sangre\n")
    print(str(personasO) + " Personas del tipo de sangre A donaron un total de: " + str(totalO) + " litros de sangre esta semana\n")

    #PERSONAS DEL TIPO AB DEL LUNES HASTA EL VIERNES
    print("Cantidades del tipo de sangre AB:\n"
    + "-Lunes: "  + str(donlunAB) + " personas donaron sangre\n"
    + "-Martes: " + str(donmarAB) + " personas donaron sangre\n" 
    + "-Miercoles: " + str(donmieAB) + " personas donaron sangre\n" 
    + "-Jueves: " + str(donjueAB) + " personas donaron sangre\n" 
    + "-Viernes: " + str(donvieAB) + " personas donaron sangre\n")
    print(str(personasAB) + " Personas del tipo de sangre A donaron un total de: " + str(totalAB) + " litros de sangre esta semana\n")

    #TOTAL DE SANGRE
    if totalpersonas == 0:
        print("Ninguna persona de ningun tipo de sangre dono sangre esta semana\n")
    else:
        print(str(totalpersonas) + " Personas en total donaron sangre esta semana")
        print(str(totalsangre) + " Litros de sangre totales fueron donados esta semana\n")

#|===============================|#
#| PARTE '3' O 'C' DEL ALGORITMO |#
#|===============================|#

    #VARIABLES DE LAS SUMAS DE LOS PESOS
    sumapesomar = 0 #SUMA DE LOS PESOS DEL MARTES
    sumapesojue = 0 #SUMA DE LOS PESOS DEL JUEVES
    sumapeso = 0 #SUMA DE LOS PESOS DEL MARTES Y JUEVES
    numper = 0 #SUMA DE LA CANTIDAD DE HOMBRES QUE DONARON EL MARTES Y JUEVES
    numpermar = 0 #SUMA DE LA CANTIDAD DE HOMBRES DEL MARTES
    numperjue = 0 #SUMA DE LA CANTIDAD DE HOMBRE DEL JUEVES

    #BUCLE PARA EL PROMEDIO DE HOMBRES QUE DONARON DESDE EL MARTES AL JUEVES
    for s in range(i):
                
        if dia[s] == 'martes' and apto[s] == 'si' and sexos[s] == 'masculino': #HOMBRES DEL MARTES
            sumapesomar += pesos[s]
            sumapeso += pesos[s]
            numper += 1
            numpermar += 1

        if dia[s] == 'jueves' and apto[s] == 'si' and sexos[s] == 'masculino': #HOMBRES DEL JUEVES
            sumapesojue += pesos[s]
            sumapeso += pesos[s]
            numper += 1
            numperjue += 1

    #VARIABLES DE LOS PROMEDIOS
    promediopesomar = sumapesomar / numpermar #PROMEDIO DE LAS PERSONAS DEL MARTES
    promediopesojue = sumapesojue / numperjue #PROMEDIO DE LAS PERSONAS DEL JUEVES
    promediopeso = sumapeso / numper #PROMEDIO DE LAS PERSONAS DEL MARTES Y JUEVES

    print('Peso promedio de los hombres que donaron el martes: ' + str(promediopesomar) + 'kg')
    print('Peso promedio de los hombres que donaron el jueves: ' + str(promediopesojue) + 'kg')

    print('Peso promedio de los hombre que donaron el martes y miercoles' + str(promediopeso) + 'kg\n')

    resetproceso = input('Desea empezar el proceso desde el principio? Si(s) o No(n): ')
    if resetproceso == 'n':
        break