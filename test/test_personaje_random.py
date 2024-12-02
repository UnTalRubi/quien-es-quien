import pytest
from quien_es_quien.personaje_random import random_pj

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
    
    random_list.sort()

    position = 1
    while position < len(random_list):
        if random_list[position] == random_list[position - 1]:
            random_list.pop(position)
        else:
            position += 1

    assert random_list == expected