from envio import calcular_envio

# Ciclo 1: envío estándar
def test_envio_estandar_hasta_5kg():
    assert calcular_envio(3, "estandar") == 50

# Ciclo 2: paquete pesado
def test_envio_estandar_mas_de_5kg():
    assert calcular_envio(7, "estandar") == 70