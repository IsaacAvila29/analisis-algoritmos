#Dependiendo de la edad

iterando = True
while iterando:

    try:
        edad = int(input("Introduce tu edad: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    if edad >= 0 and edad <= 5:
        print("Eres un niño pequeño")
    elif edad >= 6 and edad < 12:
        print("Eres un niño")
    elif edad >= 12 and edad < 15:
        print("Eres un puberto")
    elif edad >= 15 and edad < 18:
        print("Eres un adolescente")
    elif (edad >= 18 and edad <=35) :
        print("Eres un adulto joven")
    elif (edad >36 and edad <=65):
        print("Eres tercera edad")
    elif (edad > 65):
        print("Eres veterano")
    else:
        print("Edad no válida")
        iterando = False





