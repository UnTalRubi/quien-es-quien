from lista_personajes import personajes
def devolver_nombre(respuesta):
    nombres=[]
    for personaje_actual in personajes:
        if respuesta in personajes[personaje_actual]:
            nombres.append(personajes[personaje_actual][0])
        return nombres
