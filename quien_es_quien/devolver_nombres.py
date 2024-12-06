from quien_es_quien.lista_personajes import personajes
from quien_es_quien.lista_nombres import nombres_personajes


def comprobar_respuesta(respuesta,jugador):
    nombres_no_validos=[]
    posicion_jugador = nombres_personajes.index(jugador)
    
    if respuesta not in personajes[posicion_jugador]:
        print(respuesta + " es Incorrecto!")
        respuesta_incorrecta(respuesta,nombres_no_validos)

    elif respuesta in personajes[posicion_jugador]:
            print(respuesta + " es Correcto!")
            respuesta_correcta(respuesta,nombres_no_validos)

    return nombres_no_validos

def respuesta_incorrecta(respuesta,nombres_no_validos):
    for personaje_actual in personajes:
            if respuesta in personajes[personajes.index(personaje_actual)]:
                nombres_no_validos.append(personaje_actual[0])
    return nombres_no_validos

def respuesta_correcta(respuesta,nombres_no_validos):
    for personaje_actual in personajes:
        if respuesta not in personajes[personajes.index(personaje_actual)]:
            nombres_no_validos.append(personaje_actual[0])

    return nombres_no_validos