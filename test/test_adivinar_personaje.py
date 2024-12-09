import pytest
from quien_es_quien.logica.adivinar_personaje import adivinar

@pytest.mark.parametrize(
        "input1, input2, expected",
        [
            ("","Tom", ""),
            ("El personaje es Susan?","Susan", "correcto"),
            ("Sam","Alex", "incorrecto"),
            ("Tiene que ser Claire o Anne","Anne", "incorrecto"),
            ("¿El personaje con gafas se trata de Philip?","Philip", "correcto"),
            ("Joe tiene canas?","Alex", "incorrecto")
        ]
)

def test_adivinar_personaje(input1,input2,expected):
    
    assert adivinar(input1,input2) == expected