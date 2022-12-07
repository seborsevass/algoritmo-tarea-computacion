import os

#Datos
nombres = []
sexos = []
edades = []
pesos = []
tipodesangre = []
dia = []
apto = []

i = 0

#Bucle para la creacion de los datos

for j in range(1000):

    print('Introduzca los datos del participante\n')

#Input nombres
    nom = input('Ingrese el nombre: ')
    print("Nombre: " + str.capitalize(nom))
    print("")
    nombres.append(nom)

#Bucle del input de sexos
    while True:
        
        sex = input("Sexo:\nm) Masculino\nf) Femenino\n\nSeleccione el sexo: ")
        if sex == "m":
            print("Masculino\n")
            break
        if sex == "f":
            print("Femenino\n")
            break

        elif sex != "m" and sex != "f":
            print("\nSeleccione una opcion valida\n")

    if sex == "m" :
        sexos.append('masculino')
    if sex == "f":
        sexos.append('femenino')

#Input de edad
    age = int(input("Ingrese la edad: "))
    print(str(age) + " años\n")
    edades.append(age)

#Input de peso
    wg = int(input("Ingrese el peso: "))
    print(str(wg) + "kg\n")
    pesos.append(wg)

#Bucle para el tipo de sangre
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

        elif sangre != "a" and sangre != "b" and sangre != "c" and sangre != "d" :
            print("\nSeleccione una opcion valida\n")

    if sangre == "a" :
        tipodesangre.append ('a')
    if sangre == "b" :
        tipodesangre.append ('b')
    if sangre == "c" :
        tipodesangre.append('c')
    if sangre == "d" :
        tipodesangre.append('ab')

#Dia de la semana en el que asistio
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

#Datos de la persona
    print("Datos introducidos del participante:\n")
    print("-Numero del participante: " + str(i))
    print("-Nombre: " + str.capitalize(nombres[i]))
    print("-Sexo: " + str.capitalize(sexos[i]))
    print("-Edad: " + str(edades[i]) + " años") 
    print("-Peso: " + str(pesos[i]) + "kg")
    print("-Tipo de sangre: " + str.capitalize(tipodesangre[i]))
    print("-Dia en el que asistio: " + str.capitalize(dia[i]))
    print('')

#Contador
    i += 1

#Agregar mas participantes
    rep1 = input("Desea agregar otra persona? Si(s) No(n): ")
    print("")
    os.system('cls')
    if rep1 == 'n':
        os.system('cls')
        break

a = 0

for j in range(i):

    if int(edades[a]) >= 18 and int(edades[a]) <= 60 and int(pesos[a]) >= 50 :
        print("Participante " + str(a) + ': ' + str(nombres[a]) + " es apto(a) para donar sangre\n")
        aptitud = 'si'
        apto.append(aptitud)
        a += 1
        
    else:
        print("Participante " + str(a) + ': ' + str(nombres[a]) + " no es apto(a) para donar sangre\n")
        aptitud  = 'no'
        apto.append(aptitud)
        a += 1
   
datos = zip(nombres, sexos, edades, pesos, tipodesangre, dia)
