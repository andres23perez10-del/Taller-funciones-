
from Funciones import calcular_subtotal, aplicar_descuento, generar_reporte

inventario = {
    "Arroz": 2500,
    "Leche": 3800,
    "Huevos": 600,
    "Pan": 2000,
    "Cafe": 5000
}

carrito_actual = []
total_acumulado = 0

while True:
    print("--- MENÚ SUPERMERCADO ---")
    print("1. Agregar producto al carrito")
    print("2. Ver productos disponibles")
    print("3. Finalizar compra y pagar")
    print("4. Salir")
    
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        prod = input("Nombre del producto: ").capitalize()
        if prod in inventario:
            try:
                cant = int(input(f"Cantidad de {prod}: "))
                sub = calcular_subtotal(prod, cant, inventario)
                carrito_actual.append((prod, cant, sub))
                total_acumulado += sub
                print(f"-> {prod} agregado.")
            except ValueError:
                print("Error: Ingrese un número entero en cantidad.")
        else:
            print("Ese producto no existe en el inventario.")

    elif opcion == "2":
        print("\n--- LISTA DE PRECIOS ---")
        for p, precio in inventario.items():
            print(f"{p}: ${precio}")
        print("")

    elif opcion == "3":
        if not carrito_actual:
            print("El carrito está vacío.")
        else:
            desc = aplicar_descuento(total_acumulado)
            total_final = total_acumulado - desc
            generar_reporte(carrito_actual, total_final, desc)
            # Limpiar datos para una nueva venta
            carrito_actual = []
            total_acumulado = 0

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida, intente de nuevo.")