from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hola", "buenas","Hola", "Buenas"):
        return "Buenas! ¿Qué tal va todo Virginia?"
    
    if user_message in ("quien eres", "¿Quién eres", "Quien eres?"):
        return "Soy el ayudante de Alejandro. Existo para ayudarle a darte ilusión.\nPd: me ha programado Alejandro, perdo...Na mis posibles errores."
    
    if user_message in ("Quiero empezar"):

        return "Maravilloso, escribe /start"
    
    if user_message in ("pista"):

        return "¿Has probado a contar?"

    if user_message in ("te amo"):
        return "Yo más. Pd: Alejandro\nObviamente Alejandro no es tan buen programador como para enseñarme a amar"
        
    return "No te entiendo"