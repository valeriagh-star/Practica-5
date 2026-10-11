def calcular_envio(peso, tipo_envio):
    costo = 50
    if peso > 5:
        costo += (peso - 5) * 10

    if tipo_envio == "express":
        costo *= 2

    return costo