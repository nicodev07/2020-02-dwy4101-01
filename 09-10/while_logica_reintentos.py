peticionSoap = None
reintentos = 0

while reintentos < 3:
    try:
        # Petición al SOAP, si puedo recuperar la info, necesito cortar 
        # el ciclo del while.
        if reintentos == 2:
            peticionSoap = {"rut": 19134180, "dv": 3, "nombre": "jose"}

        if peticionSoap is not None:
            break

        raise Exception('Peticion soap no es correcta')
    except Exception:
        reintentos += 1

print(reintentos, peticionSoap)
# Otro bloque de código