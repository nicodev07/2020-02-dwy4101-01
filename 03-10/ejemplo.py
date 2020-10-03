# Variables
nombre = "peDro"
numero_1 = 10
numero_2 = 20
numero_3 = 10.1
valor_verdadero = True
valor_falso = False
valor_array = ["Hola", 1, 1.3, "Ejemplo"]
valor_tupla = ("Hola", 1, 1.3, "Ejemplo")

# Metodos de String
lower = nombre.lower()
upper = nombre.upper()
title = nombre.title()

#Imprimir por pantalla
print(lower,upper,title, nombre)

# Operaciones arimeticas
suma = numero_1 + numero_2 # 30
resta = numero_1 - numero_2 # -10
multiplicacion = numero_1 * numero_2 # 200
division = numero_1 / numero_2 # 0.5
division_entera = numero_1 // numero_2 # 0
resto_division = numero_1 % numero_2 # 10 
potencia = numero_1 ** numero_2 # 100000000000000000000
redondeo = round(division,1) # 0.5

print(suma,resta,multiplicacion,division,division_entera,resto_division,potencia,redondeo)

# Array de numeros
array_numeros = [1,300,45,4,5,6,7,100]
array_numeros.sort() #Ordenar numeros de forma ascendente (menor a mayor)
print(array_numeros)

array_numeros.append(500) #Agregar un valor a un array
array_numeros.sort(reverse=True) # Ordenar numeros de forma descendente (mayor a menor)

print(array_numeros)

array_numeros.remove(500) # Eliminar un array por valor.
print(array_numeros)

del array_numeros[0]
print(array_numeros)

# Total: 7 elementos en un Array
# Indices de esos 7 elementos pueden ser: 0,1,2,3,4,5,6
# Si quiero insertar un valor nuevo al array dependiendo de la cantidad total de elemento
# Debo obtener primero que todo, cuantos elementos tengo en mi array
# Después, voy a insertar un elemento nuevo en un indice que sería 7 (este indice no existe, no tiene valor)
# Corresponde a la "cantidad total" de elementos.
cantidad_elementos_array_numeros = len(array_numeros)
array_numeros.insert(cantidad_elementos_array_numeros, 450)
print(array_numeros[cantidad_elementos_array_numeros])

# Array de string
array_string = ["a","j","k","m","p","z"]
array_string.sort() # Ordenar string de forma ascendente alfabeticamente
print(array_string)
array_string.sort(reverse=True) # Ordenar string de forma descendente alfabeticamente a la inversa (primero la Z)
print(array_string)