
personajes=[["Susan","mujer","pelo largo","pelo blanco","canas","ojos marrones","labios gruesos","mofletes","mejillas sonrosadas","nariz pequeña","raya al lado"],
            ["Claire","mujer","gafas","sombrero","pelirrojo","ojos marrones","boca pequeña","nariz pequeña"],
            ["David","hombre","barba","pelo rubio","ojos marrones","orejas grandes","raya al lado","nariz pequeña"],
            ["Anne","mujer","pelo corto","pendientes","pelo negro","ojos marrones","boca pequeña","nariz grande"],
            ["Robert","hombre","cara triste","pelo castaño","ojos azules","orejas grandes","nariz grande","raya al lado","cara alargada","mofletes","mejillas sonrosadas"],
            ["Anita","mujer","pelo largo","pelo rubio","ojos marrones","boca pequeña","mofletes","mejillas sonrosadas","raya al medio","nariz pequeña"],
            ["Joe","hombre","gafas","pelo rubio","ojos marrones","boca pequeña","pelo corto","nariz pequeña"],
            ["George","hombre","cara triste","sombrero","pelo blanco","canas","ojos marrones","boca grande","nariz pequeña"],
            ["Bill","hombre","barba","pelirrojo","ojos marrones","orejas grandes","mofletes","mejillas sonrosadas","calva","boca pequeña","nariz pequeña"],
            ["Alfred","hombre","bigote","barba","pelirrojo","ojos azules","boca pequeña","orejas grandes","pelo largo","raya al medio","nariz pequeña"],
            ["Max","hombre","bigote","pelo negro","ojos marrones","boca grande","labios gruesos","nariz grande","orejas grandes","pelo corto"],
            ["Tom","hombre","gafas","calva","pelo negro","ojos azules","boca pequeña","cara alargada","nariz pequeña"],
            ["Alex","hombre","bigote","pelo negro","ojos marrones","boca grande","labios gruesos","orejas grandes","pelo corto","nariz pequeña"],
            ["Sam","hombre","gafas","calva","pelo blanco","canas","ojos marrones","boca pequeña","nariz pequeña"],
            ["Richard","hombre","calva","barba","ojos marrones","orejas grandes","bigote","cara alargada","nariz pequeña"],
            ["Paul","hombre","gafas","pelo blanco","canas","ojos marrones","boca pequeña","orejas grandes","cejas gruesas","raya al lado","nariz pequeña"],
            ["Maria","mujer","pelo largo","sombrero","pendientes","pelo castaño","ojos marrones","boca pequeña","cejas finas","nariz pequeña"],
            ["Frans","hombre","pelo corto","cejas gruesas","pelirrojo","ojos marrones","boca pequeña","nariz pequeña"],
            ["Herman","hombre","pelirrojo","calva","nariz grande","ojos marrones","cejas gruesas"],
            ["Bernard","hombre","pelo castaño","sombrero","ojos marrones","boca pequeña","cejas finas","nariz grande"],
            ["Philip","hombre","barba","pelo negro","ojos marrones","orejas grandes","mofletes","mejillas sonrosadas","cejas finas","pelo corto","nariz pequeña"],
            ["Eric","hombre","pelo rubio","gorra","sombrero","ojos marrones","boca grande","nariz pequeña"],
            ["Charles","hombre","bigote","pelo rubio","ojos marrones","labios gruesos","boca grande","orejas grandes","raya al lado","nariz pequeña"],
            ["Peter","hombre","canas","pelo blanco","nariz grande","ojos azules","cejas gruesas","labios gruesos","boca grande","raya al lado"]]


imagen_personaje = "Alex.jpg"
posicion = 0

def obtener_personajes(posicion):
    imagen_personaje = personajes[posicion][0] + ".jpg"
    posicion += 1
    
    return print (imagen_personaje) , posicion

obtener_personajes(posicion)