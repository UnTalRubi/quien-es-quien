from quien_es_quien.variables.lista_nombres import NOMBRES_PERSONAJES


def adivinar(pregunta,personaje_jugador):
    pregunta = pregunta.lower() 
    personaje_jugador = personaje_jugador.lower() 
    caracteres_especiales = "?¿:;,.¡!" 

    for caracter in caracteres_especiales: 
        pregunta=pregunta.replace(caracter, "")

    pregunta=pregunta.split()
    
    for palabra in pregunta:
        if palabra.capitalize() in NOMBRES_PERSONAJES:
            if palabra == personaje_jugador:
                return "correcto"
            elif palabra != personaje_jugador:
                return "incorrecto"
    
    return ""
