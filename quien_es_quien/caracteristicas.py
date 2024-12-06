def extraer_palabras_clave(pregunta): 
    caracteristicas = ["hombre","mujer","largo","corto","blanco","blanca","gris","grisaceo","canoso","canosa","canas","pelirrojo","pelirroja","rojo","roja","rubio","rubia","amarillo","amarilla",
                        "negro","negra","oscuro","oscura","castaño","castaña","calvo","calva","finas","gruesas","alargada","redonda","redondeada","alegre","contento","contenta","triste",
                        "enfadado","enfadada","marrones","azules","azulados","mejillas","sonrosadas","sombrero","gorro","gorra","pendientes","pendiente", "gafas","lentes","bigote","barba"] 
    
    atributos_especificos=['grande','gruesa','pequeña']
    rasgos_especificos=['boca','nariz']

    pregunta = pregunta.lower() 
    caracteres_especiales = "?¿:;,.¡!" 

    for caracter in caracteres_especiales: 
        pregunta=pregunta.replace(caracter, "")

    pregunta=pregunta.split()
    
    respuesta=[]
    posicion=0
    for posicion in range(len(pregunta)): 
        if pregunta[posicion] in rasgos_especificos:
            try:pregunta[posicion + 1]
            except IndexError:
                return ""
            if pregunta[posicion + 1] in atributos_especificos: 
                respuesta.append(pregunta[posicion])
                respuesta.append(pregunta[posicion + 1])
                return ' '.join(respuesta)
            else:
                return ""
        elif pregunta[posicion] in caracteristicas:
                respuesta.append(pregunta[posicion])
                return ' '.join(respuesta)
    if not respuesta: 
        return ""