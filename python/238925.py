
print("=====================================")
print(" SOMBRERO SELECCIONADOR")
print(" HOGWARTS")
print("=====================================")
print("Bienvenido a Hogwarts.")

nombre = input("¿Cuál es tu nombre? ")

print("Hola, " + nombre)
print("El sombrero Seleccionador analizará tu personalidad")

gryffindor = 0
slytherin = 0
ravenclaw = 0
hufflepuff = 0

print("PREGUNTA 1")
print("¿Qué cualidad te representa mejor?")
print("1. Valentía")
print("2. Ambicion")
print("3. Inteligencia")
print("4. Lealtad")

respuesta = int(input("Selecciona una opción: "))
if respuesta == 1:
    gryffindor = gryffindor + 1
elif respuesta == 2:
    slytherin = slytherin + 1
elif respuesta == 3:
    ravenclaw = ravenclaw + 1
elif respuesta == 4:
    hufflepuff = hufflepuff + 1
else:
    print("Opción incorrecta")

print("PREGUNTA 2")
print("Encuentras una puerta misteriosa en Hogwarts. ¿Qué haces?")
print("1. Entro inmediatamente. Quiero saber qué hay.")
print("2. Pienso cómo podría aprovechar lo que encuentre.")
print("3. Investigo primero qué existe detrás de la puerta.")
print("4. Busco a mis amigos para entrar juntos.")

respuesta = int(input("Selecciona una opción: "))
if respuesta == 1:
    gryffindor = gryffindor + 1
elif respuesta == 2:
    slytherin = slytherin + 1
elif respuesta == 3:
    ravenclaw = ravenclaw + 1
elif respuesta == 4:
    hufflepuff = hufflepuff + 1
else:
    print("Opción incorrecta")

print("PREGUNTA 3")
print("Un compañero tiene problemas con una tarea. ¿Qué haces?")
print("1. Lo ayudo aunque pueda meterme en problemas.")
print("2. Le explico cómo resolverla si también puedo obtener algo.")
print("3. Investigo hasta encontrar la mejor solución.")
print("4. Me quedo con él hasta que termine.")

respuesta = int(input("Selecciona una opción: "))
if respuesta == 1:
    gryffindor = gryffindor + 1
elif respuesta == 2:
    slytherin = slytherin + 1
elif respuesta == 3:
    ravenclaw = ravenclaw + 1
elif respuesta == 4:
    hufflepuff = hufflepuff + 1
else:
    print("Opción incorrecta")


print("PREGUNTA 4")
print("Si pudieras elegir una habilidad mágica, ¿cuál escogerías?")
print("1. Ser extremadamente valiente en cualquier situación.")
print("2. Tener el poder para alcanzar cualquier objetivo.")
print("3. Conocer la respuesta a cualquier pregunta.")
print("4. Poder proteger siempre a las personas que quiero.")

respuesta = int(input("Selecciona una opción: "))
if respuesta == 1:
    gryffindor = gryffindor + 1
elif respuesta == 2:
    slytherin = slytherin + 1
elif respuesta == 3:
    ravenclaw = ravenclaw + 1
elif respuesta == 4:
    hufflepuff = hufflepuff + 1
else:
    print("Opción incorrecta")

print("PREGUNTA 5")
print("Aparece una criatura desconocida frente a ti. ¿Qué haces?")
print("1. Me enfrento a ella.")
print("2. Busco la manera de controlarla.")
print("3. Primero trato de entender qué criatura es.")
print("4. Intento evitar que alguien resulte herido.")

respuesta = int(input("Selecciona una opción: "))
if respuesta == 1:
    gryffindor = gryffindor + 1
elif respuesta == 2:
    slytherin = slytherin + 1
elif respuesta == 3:
    ravenclaw = ravenclaw + 1
elif respuesta == 4:
    hufflepuff = hufflepuff + 1
else:
    print("Opción incorrecta")

print("================================")
print("RESULTADOS")
print("================================")

print("Gryffindor:", gryffindor)
print("Slytherin:", slytherin)
print("Ravenclaw:", ravenclaw)
print("Hufflepuff:", hufflepuff)

if(gryffindor > slytherin and gryffindor > ravenclaw and gryffindor > hufflepuff):
    print("¡Eres de Gryffindor!")
elif(slytherin > gryffindor and slytherin > ravenclaw and slytherin > hufflepuff):
    print("¡Eres de Slytherin!")
elif(ravenclaw > gryffindor and ravenclaw > slytherin and ravenclaw > hufflepuff):
    print("¡Eres de Ravenclaw!")
elif(hufflepuff > gryffindor and hufflepuff > slytherin and hufflepuff > ravenclaw):
    print("¡Eres de Hufflepuff!")
else:
    print("¡Empate entre casas!")



