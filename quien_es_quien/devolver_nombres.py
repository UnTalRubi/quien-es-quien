from quien_es_quien.lista_personajes import personajes
from quien_es_quien.lista_nombres import nombres_personajes


def devolver_nombre(respuesta,jugador):
    nombres=[]
    posicion_jugador = nombres_personajes.index(jugador)
    
    if respuesta not in personajes[posicion_jugador]:
        for personaje_actual in personajes:
            if respuesta in personajes[personajes.index(personaje_actual)]:
                nombres.append(personajes[personajes.index(personaje_actual)][0])
        return nombres