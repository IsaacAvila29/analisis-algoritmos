#tiendita chida
#cantidad de billete que tenemos en total
LaBolsa = 200
def vender(idProducto, cantidad):
    global LaBolsa
    for producto in LaBodega:
        if producto['id'] == idProducto:
            if producto['cantidad'] >= cantidad:
                producto['cantidad'] -= cantidad
                venta = producto['precio'] * cantidad
                LaBolsa += venta
                print(f"Se vendieron {cantidad} unidades de {producto['nombre']}")
                print(f"Ingreso de la venta: ${venta}. La bolsa ahora tiene ${LaBolsa}")
            else:
                print(f"No hay suficiente stock de {producto['nombre']}")
            return
    print("Producto no encontrado")

def comprar(idProducto, cantidad):
    global LaBolsa
    for producto in LaBodega:
        if producto['id'] == idProducto:
            costo = producto['precio'] * cantidad
            if LaBolsa >= costo:
                producto['cantidad'] += cantidad
                LaBolsa -= costo
                print(f"Se compraron {cantidad} unidades de {producto['nombre']}")
                print(f"Gasto de la compra: ${costo}. La bolsa ahora tiene ${LaBolsa}")
            else:
                print("No hay suficiente dinero en la bolsa")
            return
    print("Producto no encontrado")

def eliminar(idProducto):
    for i, producto in enumerate(LaBodega):
        if producto['id'] == idProducto:
            del LaBodega[i]
            print(f"Producto {producto['nombre']} eliminado")
            return
    print("Producto no encontrado")

def agregar(idProducto, nombre, cantidad, precio):
    nuevo_producto = {
        'id': idProducto,
        'nombre': nombre,
        'cantidad': cantidad,
        'precio': precio,
    }
    LaBodega.append(nuevo_producto)
    print(f"Producto {nombre} agregado")



LaBodega = [
    {
        'id': 1,
        'nombre': 'Cigarros Marlboro',
        'cantidad': 10,
        'precio': 100,
    },
    {
        'id': 2,
        'nombre': 'Cerveza Corona',
        'cantidad': 20,
        'precio': 50,
    },
    {
        'id': 3,
        'nombre': 'Coca-Cola',
        'cantidad': 15,
        'precio': 30,
    }

]

print("Tiendita doña petra")

while True:
    print("Que desea hacer")
    print("1. Vender")
    print("2. Comprar")
    print("3. Eliminar")
    print("4. Agregar producto")
    print("5. Mostrar productos")
    print("6. Salir")

    seleccion = int(input("Ingrese su selección: "))


    # En Python, `match` es el equivalente más cercano a `switch`.
    match seleccion:
        case 1:
            print("=====================")
            print("HA SELECCIONADO VENDER")
            print("=====================")
            print("Mostrar productos")
            idProducto = int(input('Selecciona el id del producto'))
            for producto in LaBodega:
                if producto['id'] == idProducto:
                    print(producto)
                    break
            cantidadVender = int(input('Ingrese la cantidad a vender: '))
            vender(idProducto, cantidadVender)
        case 2:
            print("=====================")
            print("HA SELECCIONADO COMPRAR")
            print("=====================")
            print("Mostrar productos")
            idProducto = int(input('Selecciona el id del producto'))
            for producto in LaBodega:
                if producto['id'] == idProducto:
                    print(producto)
                    break
            cantidadComprar = int(input('Ingrese la cantidad a comprar: '))
            comprar(idProducto, cantidadComprar)
        case 3:
            print("=====================")
            print("HA SELECCIONADO ELIMINAR")
            print("=====================")
            print("Mostrar productos")
            idProducto = int(input('Selecciona el id del producto'))
            for producto in LaBodega:
                if producto['id'] == idProducto:
                    print(producto)
                    break
            eliminar(idProducto)
        case 4:
            print("=====================")
            print("HA SELECCIONADO AGREGAR PRODUCTO")
            print("=====================")
            idProducto = int(input('Ingrese el id del producto: '))
            nombre = input('Ingrese el nombre del producto: ')
            cantidad = int(input('Ingrese la cantidad: '))
            precio = float(input('Ingrese el precio: '))
            agregar(idProducto, nombre, cantidad, precio)
        case 5:
            print("=====================")
            print("PRODUCTOS DISPONIBLES")
            print("=====================")
            for producto in LaBodega:
                print(producto)
        case 6:
            print("Hasta luego")
            break
        case _:
            print("Selección no válida")




