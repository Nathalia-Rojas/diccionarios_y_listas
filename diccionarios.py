#1. Actualizar valores en diccionarios y listas:  A continuación se presentan varias estructuras de datos. 
# Realiza los siguientes cambios directamente:
# Realiza los siguientes cambios:
# Cambia el valor 3 en matriz por 6.
# Cambia el nombre del primer cantante por "Enrique Martin Morales".
# En el diccionario ciudades, reemplaza "Cancún" por "Monterrey".
# En la lista coordenadas, cambia el valor de "latitud" por 9.9355431.
# 2. Recorrer una lista de diccionarios:  Utiliza estructuras de control para iterar la lista cantantes. Muestra el nombre y país de cada cantante.
# * BONUS: Presenta cada entrada con el siguiente formato: nombre - [Nombre del cantante], pais - [País]
# 3. Obtener valores específicos desde una lista de diccionarios:  Utilizando la lista cantantes, imprime por separado todos los valores correspondientes a la clave "nombre".
#  Luego, imprime todos los valores correspondientes a la clave "pais".

matriz = [ [10, 15, 20], [3, 7, 14] ]
matriz[1][0] = 6
print("matriz actualizada:", matriz)

cantantes = [
   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
cantantes[0]["nombre"] = "Enrique Martin Morales"
print("cantantes actualizados:", cantantes)

ciudades = {
   "México": ["Ciudad de México", "Guadalajara", "Cancún"],
   "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
ciudades["México"][2] = "Monterrey"
print("ciudades actualizadas:", ciudades)


coordenadas = [
   {"latitud": 8.2588997, "longitud": -84.9399704}
]

coordenadas[0]["latitud"] = 9.9355431
print("coordenadas actualizadas:", coordenadas)

for cantante in cantantes:
    print(f"nombre - {cantante['nombre']}, pais - {cantante['pais']}")


for cantante in cantantes:
    print(cantante["nombre"])

for cantante in cantantes:
    print(cantante["pais"])

# 4. Recorrer un diccionario con listas como valores:  Dado el siguiente diccionario:
# Realiza un recorrido del diccionario que imprima lo siguiente: 
# La cantidad de elementos en cada lista seguida del nombre de la clave en mayúsculas.
# Cada elemento de la lista correspondiente, en líneas separadas.

costa_rica = {
   "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
   "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

for clave, lista in costa_rica.items():
    print(f"{len(lista)} - {clave.upper()}")
    for elemento in lista:
        print(elemento)

