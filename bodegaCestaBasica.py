# En una pequeña comunidad existe una bodega con venta de todos los víveres de la cesta básica, al ser el favorito de los vecinos las ventas han ido subiendo, lo que produjo una alta entrada de mercancía, se desea un programa que reciba nombre de cada producto, precio y cantidad_productos(), e imprima en pantalla la factura.
# Nota: la factura debe tener el precio unitario de cada producto, el total de cada producto por su cantidad_productos(), luego imprimir el subtotal, el impuesto y el total a pagar.
# lista_productos = dict
precio = float
subtotal = float
producto = int

def cantidad_productos():
    cantidad = int(input("¿Cuánto desea? "))
def agregar_productos():
    producto = int(input("¿Desea agregar algo más? "))

def factura():
    print("--- Factura ---")
    print("Precio: ", precio)
    print("cantidad_productos(): ", cantidad_productos())
    print("Subtotal: ", precio*cantidad_productos())
    subtotal=precio*cantidad_productos()
    print("TOTAL: ", (subtotal*0.16))
    print("Gracias por comprar con nosotros")
    print("---------------")

def bodega():
    print("La Bodega de Rex")
    print("1. Harina = 40")
    print("2. Arroz = 50")
    print("3. Frijoles = 70")
    print("4. Huevos = 2.50")

while True:
    try:
        bodega()
        opcion = int(input("¿Qué desea comprar? "))
    except ValueError:
        print("Por favor, ingrese una opción válida.")

    else:
        if opcion == 1:
            precio = 40
            print("La harina cuesta ", precio)
            cantidad_productos()

        elif opcion == 2:
            precio=50
            print("El arroz cuesta ", precio)
            cantidad_productos()

        elif opcion == 3:
            precio=70
            print("Los frijoles cuestan ", precio)
            cantidad_productos()

        elif opcion == 4:
            precio=2.50
            print("Los huevos cuestan ", precio)
            cantidad_productos()
        else:
            print("Debe ingresar un valor válido")
            print("")
            bodega()
    if opcion < 5:
        agregar_productos()
        if producto == 1:
            print("¿Qué más desea agregar?")
            bodega()
        else:
            factura()
    break
