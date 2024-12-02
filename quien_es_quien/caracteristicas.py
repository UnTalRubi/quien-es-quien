def extraer_palabras_clave(pregunta): 
    caracteristicas = ['hombre', 'mujer', 'barba', 'pelirrojo', 'marrones', 'orejas', 'grandes', 'mofletes', 'mejillas', 'sonrosadas', 'calva', 'pelirroja',
                      'bigote', 'ojos', 'azules', 'largo', 'raya', 'medio', 'pelo', 'negro', 'labios', 'gruesos', 'corto', 'gafas', 'alargada', 'blanco', 'canas', 
                      'cejas', 'gruesas', 'lado', 'sombrero', 'pendientes', 'castaño', 'finas', 'rubio', 'cara', 'triste', 'gorra', 'finos','calvo','marrón', 'rubia'] 
    forma_nariz=['grande', 'pequeña']
    lista=['boca','nariz']
    pregunta = pregunta.lower() 
    caracteres_especiales = "?¿:;,.¡!" 
    for caracter in caracteres_especiales: 
        pregunta = pregunta.replace(caracter, "") 
    respuesta = []
    for palabra_clave in pregunta: 
        if palabra_clave in lista:
            respuesta.append(palabra_clave)
            if palabra_clave in forma_nariz: 
                respuesta.append(palabra_clave) 
                print(respuesta)
                return respuesta
        elif palabra_clave in caracteristicas:
                respuesta.append(palabra_clave) 
                return respuesta
    if not respuesta: 
        return f"No se encontró la característica. Intenta con las siguientes características posibles: {', '.join(caracteristicas)}" 
    return respuesta




pregunta = "¿Tiene los ojos azules?"
print(extraer_palabras_clave(pregunta))
# pregunta = "¿Tiene la cara triste?"
# print(extraer_palabras_clave(pregunta))
# pregunta = "¿Está triste?"
# print(extraer_palabras_clave(pregunta)) ####
# pregunta = "Tiene los ojos verdes?"
# print(extraer_palabras_clave(pregunta))
# pregunta = "Tiene hoyuelos?"
# print(extraer_palabras_clave(pregunta))
# pregunta = "Tiene cara?"
# print(extraer_palabras_clave(pregunta)) ####
# pregunta = "Tiene labios finos?"
# print(extraer_palabras_clave(pregunta))
# pregunta = "Tiene la boca grande?"
# print(extraer_palabras_clave(pregunta))
