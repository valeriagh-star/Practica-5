COSTO_BASE = 50
PESO_LIMITE = 5
COSTO_EXCESO_POR_KG = 10

def calcular_envio(peso, tipo_envio):
    if peso <= 0:
        raise ValueError("El peso debe ser mayor que cero.")
    
    if tipo_envio not in ["estandar", "express"]:
        raise ValueError("Tipo de envío no válido.")
    
    costo_base = COSTO_BASE
    if peso > PESO_LIMITE:
        costo_base += (peso - PESO_LIMITE) * COSTO_EXCESO_POR_KG
    
    if tipo_envio == "express":
        return costo_base * 2
        
    return costo_base