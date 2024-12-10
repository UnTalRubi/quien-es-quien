import pytest
from quien_es_quien.logica.personaje_random import random_pj

@pytest.mark.parametrize(
        "expected",
        [
            ['Alex', 'Alfred', 'Anita', 'Anne', 'Bernard', 'Bill', 'Charles', 'Claire', 'David', 'Eric', 'Frans', 'George', 'Herman', 'Joe', 'Maria', 'Max', 'Paul', 'Peter', 'Philip', 'Richard', 'Robert', 'Sam', 'Susan', 'Tom']
        ]
)

def test_personaje_random(expected):
    
    random_list=[]
    for _ in range(300):
        random_list.append(random_pj())

    random_list = set(random_list)
    random_list = list(random_list)
    random_list.sort()

    assert random_list == expected