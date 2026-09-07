import random

numeros = []
for i in range(1, 10):
    numeros.append(random.randint(1, 100))
    print("numeroRandom en ", i, ":", numeros[-1])

numeros.sort()


print("Números ordenados:")
for numero in numeros:
    print(numero)

numeroPick = int(input("Elige un numero del i al 100: "))

for i in range(1, 10):
    if(numeroPick > numeros[i-1] and numeroPick < numeros[i]):
        print("El número elegido está entre", numeros[i-1], "y", numeros[i], "y deberia quedar en la posicion", i)
    elif(numeroPick == numeros[i-1] ):
        print("El número elegido es igual a", numeros[i-1], "y debería quedar en la posición", i-1)
    elif(numeroPick == numeros[i] ):
        print("El número elegido es igual a", numeros[i], "y debería quedar en la posición", i)

    elif(numeroPick == numeros[i-1] and numeroPick[i+1]):
        print("El número elegido es igual a", numeros[i-1], "y", numeros[i], "y debería quedar en la posición", i-1)
    else:
        print("Este numero esta por encima del ultimo o por debajo del primero... no se que hacer")
        break
