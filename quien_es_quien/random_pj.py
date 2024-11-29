import random

import pytest
from personajes import personajes

def random_pj():
    return random.choice(personajes)

    #personajes_nombres = ['Alex', 'Alfred', 'Anita', 'Anne', 'Bernard', 'Bill', 'Charles', 'Claire', 'David', 'Eric', 'Frans', 'George', 'Herman', 'Joe', 'Maria', 'Max', 'Paul', 'Peter', 'Philip', 'Richard', 'Robert', 'Sam', 'Susan', 'Tom']



@pytest.mark.parametrize(
    "output",
    [
        (['Alex', 'Alfred', 'Anita', 'Anne', 'Bernard', 'Bill', 'Charles', 'Claire', 'David', 'Eric', 'Frans', 'George', 'Herman', 'Joe', 'Maria', 'Max', 'Paul', 'Peter', 'Philip', 'Richard', 'Robert', 'Sam', 'Susan', 'Tom'])
    ]
    )

def test_random_pj(output):
    
    random_list=[]
    i=0
    while i < 100:
        random_list.append(random_pj())
        i+=1
    
    random_list.sort()

    assert random_pj () == output