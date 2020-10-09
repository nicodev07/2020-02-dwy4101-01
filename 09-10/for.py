numeroArray = range(1, 11)

for valor in numeroArray:
    print(valor)

for indice, valor in enumerate(numeroArray):
    print("En el indice", indice, "del array tiene el valor", valor)

diccionario = {'a': 100, 'b': 200, 'c': 300}
print(diccionario['a'])
for key, value in diccionario.items():
    print(key, value)
