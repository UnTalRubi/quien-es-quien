from quien_es_quien.lista_personajes import personajes
from quien_es_quien.lista_nombres import nombres_personajes


def correccion(respuesta,jugador):
    posicion_jugador = nombres_personajes.index(jugador)
    
    if not respuesta:
        print ("invalido")
        return "invalido"
    elif respuesta not in personajes[posicion_jugador]:
        print ("incorrecto")
        return "incorrecto"
    elif respuesta in personajes[posicion_jugador]:
        print ("correcto")
        return "correcto"