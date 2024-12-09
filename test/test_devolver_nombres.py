import pytest
from quien_es_quien.logica.devolver_nombres import comprobar_respuesta

@pytest.mark.parametrize(
        "input1, input2, expected",
        [
            ("mujer", "Tom", ["Susan","Claire","Anne","Anita","Maria"]),
            ("boca grande", "Philip", ["Claire","Anne","Anita","Joe","Bill","Alfred","Tom","Sam","Richard","Paul","Maria","Frans","Herman","Bernard"]),
            ("","Anne",[])
        ]
)

def test_caracteristicas(input1,input2,expected):
    
    assert comprobar_respuesta(input1, input2) == expected