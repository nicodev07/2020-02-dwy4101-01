SUMA = 'suma'
RESTA = 'resta'
MULTIPLICACION = 'multiplicacion'
DIVISION = 'division'
numero_1 = 10
numero_2 = 20

def suma(numero_1, numero_2):
    return numero_1 + numero_2

def resta(numero_1, numero_2):
    return numero_1 - numero_2

def multiplicacion(numero_1, numero_2):
    return numero_1 * numero_2

def division(numero_1, numero_2):
    return numero_1 / numero_2

def calculadora(numero_1, numero_2, operacion):
    if operacion == SUMA:
        return suma(numero_1, numero_2)

    if operacion == RESTA:
        return resta(numero_1, numero_2)

    if operacion == MULTIPLICACION:
        return multiplicacion(numero_1, numero_2)

    if operacion == DIVISION:
        return division(numero_1, numero_2)

    raise Exception('La operación '+operacion+' no está permitida.')

try:
    operacion_suma = calculadora(numero_1, numero_2, SUMA)
    operacion_resta = calculadora(numero_1, numero_2, RESTA)
    operacion_division = calculadora(numero_1, numero_2, DIVISION)
    operacion_multiplicacion = calculadora(numero_1, numero_2, MULTIPLICACION)
    operacion_potencia = calculadora(numero_1, numero_2, 'potencia')

    print("La suma de ", numero_1, " con ", numero_2, "es ", operacion_suma)
    print("La resta de ", numero_1, " con ", numero_2, "es ", operacion_resta)
    print("La multiplicación de ", numero_1, " con ",
        numero_2, "es ", operacion_multiplicacion)
    print("La division de ", numero_1, " con ",
        numero_2, "es ", operacion_division)
except Exception as e:
    print(e)
