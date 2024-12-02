import pytest
from quien_es_quien.caracteristicas import extraer_palabras_clave

@pytest.mark.parametrize(
        "input, expected",
        [
            ("Tiene la boca grande?", ['boca','grande'])
        ]
)

def test_caracteristicas(input,expected):
    
    assert extraer_palabras_clave(input) == expected