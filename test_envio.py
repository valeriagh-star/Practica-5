from envio import calcular_envio

# Ciclo 1: envío estándar
def test_envio_estandar_hasta_5kg():
    assert calcular_envio(3, "estandar") == 50

# Ciclo 2: paquete pesado
def test_envio_estandar_mas_de_5kg():
    assert calcular_envio(7, "estandar") == 70

# Ciclo 3: envío exprés
def test_envio_express_hasta_5kg():
    assert calcular_envio(3, "express") == 100

def test_envio_express_mas_de_5kg():
    assert calcular_envio(7, "express") == 140