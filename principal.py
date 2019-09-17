import random

minNumero = 0
maxNumero = 20
intentoN = 0

numero = random.randint(minNumero, maxNumero)

while intentoN < 6:
    intentoN = intentoN + 1
    print('Ingrese un numero\n')
    intento = int(input())

    if intento < numero:
        print('El numero ' + str(intento) + ' es muy bajo\n')
    if intento > numero:
        print('El numero ' + str(intento) + ' es muy alto\n')
    if intento == numero:
        print('Adivinaste el numero, que era: ' + str(numero))
        break

if intento != numero:
    print('Perdiste, el numero era: ' + str(numero))
