def calcular_subtotal(producto, cantidad, inventario):
    if producto in inventario:
        return inventario[producto] * cantidad
    return 0

def aplicar_descuento(total):
    if total > 50000:
        return total * 0.10
    return 0

def generar_reporte(carrito, total, descuento):
    print("\n" + "="*30)
    print("      TICKET DE VENTA")
    print("="*30)
    for p, c, s in carrito:
        print(f"{p} x{c}: ${s}")
    print("-" * 30)
    if descuento > 0:
        print(f"Subtotal: ${total + descuento}")
        print(f"Descuento (10%): -${descuento}")
    print(f"TOTAL A PAGAR: ${total}")
    print("="*30 + "\n")