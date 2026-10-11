import pytest
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

# Ciclo 4: validación del peso
def test_peso_cero_lanza_error():
    with pytest.raises(ValueError):
        calcular_envio(0, "estandar")

def test_peso_negativo_lanza_error():
    with pytest.raises(ValueError):
        calcular_envio(-2, "express")

# Ciclo 5: tipo de envío inválido
def test_tipo_envio_invalido_lanza_error():
    with pytest.raises(ValueError):
        calcular_envio(3, "urgente")