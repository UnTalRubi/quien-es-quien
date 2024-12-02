import pytest
from quien_es_quien.nombre_personaje import nombre_pj

@pytest.mark.parametrize(
        "input, expected",
        [
            (0,"Susan"),
            (5,"Anita"),
            (12,"Alex"),
            (20,"Philip")
        ]
)

def test_imagen_pj(input, expected):
    assert nombre_pj (input) == expected