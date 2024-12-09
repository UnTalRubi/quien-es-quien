import pytest
from quien_es_quien.logica.evaluar_respuesta import correccion

@pytest.mark.parametrize(
        "input1, input2, expected",
        [
            ("mujer", "Tom", "incorrecto"),
            ("boca grande", "Philip", "correcto"),
            ("sombrero", "Maria", "correcto"),
            ("","Anne","invalido")
        ]
)

def test_caracteristicas(input1,input2,expected):
    
    assert correccion(input1, input2) == expected