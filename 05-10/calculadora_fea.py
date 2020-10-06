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
    resultado = 0
    if operacion == 'suma':
        resultado = suma(numero_1, numero_2)

    elif operacion == 'resta':
        resultado=  resta(numero_1, numero_2)

    elif operacion == 'multiplicacion':
        resultado =  multiplicacion(numero_1, numero_2)

    elif operacion == 'division':
        resultado =  division(numero_1, numero_2)

    return resultado

operacion_suma = calculadora(numero_1, numero_2, 'suma')
operacion_resta = calculadora(numero_1, numero_2, 'resta')
operacion_division = calculadora(numero_1, numero_2, 'division')
operacion_multiplicacion = calculadora(numero_1, numero_2, 'multiplicacion')

print("La suma de ", numero_1, " con ", numero_2, "es ", operacion_suma)
print("La resta de ", numero_1, " con ", numero_2, "es ", operacion_resta)
print("La multiplicación de ", numero_1, " con ",
      numero_2, "es ", operacion_multiplicacion)
print("La division de ", numero_1, " con ",
      numero_2, "es ", operacion_division)
