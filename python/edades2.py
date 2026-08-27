#Dependiendo de la edad

iterando = True
while iterando:

    try:
        edad = int(input("Introduce tu edad: "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue

    match edad:
        case 0|1|2|3|4|5:
            print("Eres un niño pequeño")
        case 6|7|8|9|10|11:
            print("Eres un niño")
        case 12|13|14:
            print("Eres un puberto")
        case 15|16|17:
            print("Eres un adolescente")
        case 18|19|20|21|22|23|24|25|26|27|28|29|30|31|32|33|34|35:
            print("Eres un adulto joven")
        case 37|38|39|40|41|42|43|44|45|46|47|48|49|50|51|52|53|54|55|56|57|58|59|60|61|62|63|64|65:
            print("Eres tercera edad")
        case _ if edad > 65:
            print("Eres veterano")
        case _:
            print("Edad no válida")
            iterando = False





