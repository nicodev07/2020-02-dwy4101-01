contador = 0
while contador < 10:
    print("El contador va en",contador)

    if contador == 5:
        print("Cortando el ciclo...")
        break # corta la ejecución del ciclo.
    contador += 1