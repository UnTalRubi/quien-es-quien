def extraer_palabras_clave(pregunta): 
    caracteristicas = ['hombre', 'mujer', 'barba', 'pelirrojo', 'marrones', 'orejas', 'grandes', 'mofletes', 'mejillas', 'sonrosadas', 'calva', 'pelirroja',
                        'bigote', 'azules', 'largo', 'raya', 'medio', 'pelo', 'negro', 'gruesos', 'corto', 'gafas', 'alargada', 'blanco', 'canas', 
                        'cejas', 'gruesas', 'lado', 'sombrero', 'pendientes', 'castaño', 'finas', 'rubio', 'triste', 'gorra', 'finos','calvo','marrón', 'rubia'] 
    atributo=['grande', 'pequeña']
    lista=['boca','nariz']
    pregunta = pregunta.lower() 
    caracteres_especiales = "?¿:;,.¡!" 
    for caracter in caracteres_especiales: 
        pregunta = pregunta.replace(caracter, "") 
    respuesta = []
    pregunta=pregunta.split()
    posicion=0
    for posicion in range(len(pregunta)): 
        if pregunta[posicion] in lista:
            respuesta.append(pregunta[posicion])
            if pregunta[posicion + 1] in atributo: 
                respuesta.append(pregunta[posicion + 1]) 
                return respuesta
        elif pregunta[posicion] in caracteristicas:
                respuesta.append(pregunta[posicion]) 
                return respuesta
    if not respuesta: 
        return f"No se encontró la característica. Intenta con las siguientes características posibles: {', '.join(caracteristicas)}" 
    return respuesta
