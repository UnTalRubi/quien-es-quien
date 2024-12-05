import pytest
from quien_es_quien.devolver_nombres import devolver_nombre

@pytest.mark.parametrize(
        "input, expected",
        [
            ("boca grande", ["Susan","David","Robert","George","Max","Alex","Philip","Eric","Charles","Peter"]),
            ("mujer", ["Susan","Claire","Anne","Anita","Maria"]),
            ("",[])
        ]
)

def test_caracteristicas(input,expected):
    
    assert devolver_nombre(input) == expected