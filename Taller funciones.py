#Calculadora de notas 
def obtener_promedio(lista):
    return sum(lista) / len(lista) if lista else 0

def obtener_maxima(lista):
    return max(lista) if lista else 0

def obtener_minima(lista):
    return min(lista) if lista else 0

notas=[4.0,2.5,5.0,3.0,2.7,4.5]
reporte = {
    "Promedio": obtener_promedio(notas),
    "Nota más alta": obtener_maxima(notas),
    "Nota más baja": obtener_minima(notas)
}
print("NOTAS")
for clave, valor in reporte.items():
    print(f"{clave}: {valor}")

#Notas de estudiantes 

registro_estudiantes = [
    ("Ana García", 4.5),
    ("Juan Gómez", 3.0),
    ("Martin Ruiz",2.0) ,
    ("Nicolas Ramirez",5.0),
    ("Jhon Rojas",3.5) ,
    ("Juliana Montoya", 4.8),
    ("Roman Fuentes",1.4), 

]
def filtrar_aprobados(lista_estudiantes):

    aprobados = []
    
    for nombre, nota in lista_estudiantes:
        if nota >= 3.0:
            
            aprobados.append((nombre, nota))
            
    return aprobados

estudiantes_aprobados = filtrar_aprobados(registro_estudiantes)

print(" ESTUDIANTES APROBADOS")
for nombre, nota in estudiantes_aprobados:
    print(f"Estudiante: {nombre} | Nota: {nota}")

#Organizar Agenda 
agenda = {}

def agregar_contacto(nombre, telefono):
  
    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' guardado con éxito.")

def buscar_contacto(nombre):
   
    if nombre in agenda:
        print(f"Resultado de búsqueda: {nombre} -> {agenda[nombre]}")
    else:
        print(f"El contacto '{nombre}' no existe en la agenda.")

def eliminar_contacto(nombre):
    if nombre in agenda:
        del agenda[nombre]
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print(f"No se pudo eliminar: '{nombre}' no encontrado.")

def mostrar_agenda():

    if not agenda:
        print("La agenda está vacía.")
    else:
        print("\n LISTA DE CONTACTOS")
        for nombre, telefono in agenda.items():
            print(f"- {nombre}: {telefono}")
agregar_contacto("Jhoan", "301276917")
agregar_contacto("Maria","315679321")
agregar_contacto("Mateo","3054317789")
buscar_contacto("Jhoan")
eliminar_contacto("Maria")
mostrar_agenda()

#Inventario 

inventario = [
    {"nombre": "Laptop", "precio":12500000, "cantidad": 5},
    {"nombre": "Mouse", "precio":750000,"cantidad": 20},
    {"nombre": "Teclado", "precio": 120000, "cantidad": 10}
]

def calcular_valor_total(lista_productos):
    total = 0
    for p in lista_productos:
        total += p["precio"] * p["cantidad"]
    return total

print(f"Valor total del inventario: ${calcular_valor_total(inventario)}")

#Fracuencia de palabras 

def contar_frecuencias(texto):
    palabras = texto.lower().split()
    frecuencias = {}
    for p in palabras:
        frecuencias[p] = frecuencias.get(p, 0) + 1
    return frecuencias

frase = "Ojala volver a dormir ocho horas, no vuelvo a procrastinar"
print(contar_frecuencias(frase))

#Temperaturas Registradas 

clima = {
    "Bogotá": [12, 15, 14, 13, 16, 12, 11],
    "Medellín": [22, 25, 24, 23, 26, 22, 21]
}

def analizar_clima(datos_ciudades):
    for ciudad, temps in datos_ciudades.items():
        print(f"{ciudad}: Max {max(temps)}°C, Min {min(temps)}°C")

analizar_clima(clima)

#Conversion de notas 

escala = (("A", 4.5, 5.0), ("B", 3.5, 4.4), ("C", 3.0, 3.4), ("D", 2.0, 2.9), ("F", 0.0, 1.9))

def convertir_a_letras(estudiantes):
    reporte = {}
    for nombre, nota in estudiantes:
        for letra, min_n, max_n in escala:
            if min_n <= nota <= max_n:
                reporte[nombre] = letra
                break
    return reporte

estudiantes_notas = [("Hernesto",3.7), ("Pepe", 2.5), ("Juan", 3.2)]
print(convertir_a_letras(estudiantes_notas))

#Carrito 

carrito = []

def agregar_al_carrito(nombre, precio):
    carrito.append({"nombre": nombre, "precio": precio})

def calcular_pago(descuento_porcentaje=0):
    subtotal = sum(item["precio"] for item in carrito)
    total = subtotal * (1 - descuento_porcentaje / 100)
    return total

agregar_al_carrito("Zapatos",250000)
agregar_al_carrito("Jean", 120000)
print(f"Total con 10% de descuento: ${calcular_pago(10)}")

#Agrupar productos

productos = [("Manzana", "Frutas"), ("Leche", "Lácteos"), ("Pera", "Frutas"), ("Queso", "Lácteos")]

def agrupar_por_categoria(lista):
    categorias = {}
    for prod, cat in lista:
        if cat not in categorias:
            categorias[cat] = []
        categorias[cat].append(prod)
    return categorias

print(agrupar_por_categoria(productos))

#Votos 

votos_recibidos = ["Ana", "Luis", "Ana", "Invalido", "Ana", "Luis", "Pedro"]
candidatos_validos = ["Ana", "Luis", "Pedro"]

def procesar_votos(votos):
    conteo = {}
    total_validos = 0
    
    for v in votos:
        if v in candidatos_validos:
            conteo[v] = conteo.get(v, 0) + 1
            total_validos += 1
            
    ganador = max(conteo, key=conteo.get)
    porcentaje = (conteo[ganador] / total_validos) * 100
    
    return f"Ganador: {ganador} con {porcentaje:.1f}% de los votos válidos."

print(procesar_votos(votos_recibidos))


