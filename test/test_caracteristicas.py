import pytest
from quien_es_quien.caracteristicas import extraer_palabras_clave

@pytest.mark.parametrize(
        "input, expected",
        [
            ("¿Tiene la boca grande?", "boca grande"),
            ("Es una mujer?", "mujer"),
            ("¿Tiene boca?", ""),
            ("Tiene el pelo negro y corto?", "negro"),
            ("¿Lleva GaFa:s?", "gafas"),
            ("¿Tiene la nariz pequeña?", "nariz pequeña"),
            ("¿Tiene pequeña la nariz?", ""),
            ("¿Está ConTenta?", "contenta")
        ]
)

def test_caracteristicas(input,expected):
    
    assert extraer_palabras_clave(input) == expected