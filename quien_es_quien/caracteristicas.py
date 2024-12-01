
def extraer_palabras_clave(pregunta): 
    caracteristicas = ['hombre', 'mujer', 'barba', 'pelirrojo', 'marrones', 'orejas', 'grandes', 'mofletes', 'mejillas', 'sonrosadas', 'calva', 'pequeña', 'nariz', 'pequeña', 
                      'bigote', 'ojos', 'azules', 'largo', 'raya', 'medio', 'pelo', 'negro', 'boca', 'grande', 'labios', 'gruesos', 'corto', 'gafas', 'alargada', 'blanco', 
                      'canas', 'cejas', 'gruesas', 'lado', 'sombrero', 'pendientes', 'castaño', 'finas', 'rubio', 'cara', 'triste', 'gorra'] 
    pregunta = pregunta.lower() 
    caracteres_especiales = "?¿:;,.¡!" 
    for caracter in caracteres_especiales: 
        pregunta = pregunta.replace(caracter, "") 
    resultado = set()
    palabras = pregunta.split() 
    for palabra_clave in caracteristicas: 
        if palabra_clave in palabras: 
            resultado.add(palabra_clave) 
    if not resultado: 
        return f"No se encontró la característica. Intenta con las siguientes características posibles: {', '.join(caracteristicas)}" 
    return resultado


pregunta = "¿Tiene los ojos azules?"
print(extraer_palabras_clave(pregunta))
pregunta = "¿Tiene la cara triste?"
print(extraer_palabras_clave(pregunta))
pregunta = "¿Está triste?"
print(extraer_palabras_clave(pregunta)) #####
pregunta = "Tiene los ojos verdes?"
print(extraer_palabras_clave(pregunta))
pregunta = "Tiene hoyuelos?"
print(extraer_palabras_clave(pregunta))