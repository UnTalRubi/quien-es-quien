from quien_es_quien.variables.lista_personajes import PERSONAJES
from quien_es_quien.variables.lista_nombres import NOMBRES_PERSONAJES


def comprobar_respuesta(respuesta,jugador):
    nombres_no_validos=[]
    posicion_jugador = NOMBRES_PERSONAJES.index(jugador)
    
    if not respuesta:
        return []
    elif respuesta not in PERSONAJES[posicion_jugador]:
        respuesta_incorrecta(respuesta,nombres_no_validos)
    elif respuesta in PERSONAJES[posicion_jugador]:
        respuesta_correcta(respuesta,nombres_no_validos)

    return nombres_no_validos


def respuesta_incorrecta(respuesta,nombres_no_validos):
    for personaje_actual in PERSONAJES:
            if respuesta in PERSONAJES[PERSONAJES.index(personaje_actual)]:
                nombres_no_validos.append(personaje_actual[0])
    
    return nombres_no_validos


def respuesta_correcta(respuesta,nombres_no_validos):
    for personaje_actual in PERSONAJES:
        if respuesta not in PERSONAJES[PERSONAJES.index(personaje_actual)]:
            nombres_no_validos.append(personaje_actual[0])

    return nombres_no_validos