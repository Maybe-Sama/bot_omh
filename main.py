import Constants as keys
from telegram.ext import *
import Responses as R

print("El bot se ha despertado...")

def start_command(update, context):
    update.message.reply_text("Acabas de quitarle el primer lacito a tu regalo.\nAhora comienza la magia.\nAcabas de abrir el mapa que guiará al secreto de la FELICIDAD.\nQuienes hicieron este mapa no desean que nadie más pueda leerlo, es por eso que necesitaras un traductor de números a ubicaciones.\nEl mapa indica que el primer destino es donde todo empezó: 37°25\'04.9\"N 5°57\'48.6\"W\nY recuerda, cuida tu mente.")
def help_command(update, context):
    update.message.reply_text("¿Estás perdida eh? Te dejo una lista de cosas que puedes decirme:\nhola\nquien eres\nquiero empezar")

def ub1_command(update, context):
    update.message.reply_text("Expresa tu gratitud.\nSiguiente destino: 37°23\'46.5\"N 6°00\'21.0\"W")

def ub2_command(update, context):
    update.message.reply_text("Sé optimista.\nSiguiente destino: 37°23'53.4\"N 5°59\'37.0\"W")

def ub3_command(update, context):
    update.message.reply_text("Evita las comparaciones, evita pensar más allá.\nSiguiente destino: 37°23\'35.4\"N 5°59\'31.4\"W 1ª Planta")

def ub4_command(update, context):
    update.message.reply_text("Sé amable.\nSiguiente destino: 37°23\'22.9\"N 5°59\'13.3\"W")

def ub5_command(update, context):
    update.message.reply_text("Fomenta las relaciones sociales.\nSiguiente destino: 37°23\'23.9\"N 5°59\'34.9\"W")

def ub6_command(update, context):
    update.message.reply_text("Haz cosas que te apasionen.\nSiguiente destino: 37°23\'08.1\"N 5°59\'41.0\"W")

def ub7_command(update, context):
    update.message.reply_text("Perdona.\nSiguiente destino: 37°22\'56.8\"N 5°59\'24.2\"W")

def ub8_command(update, context):
    update.message.reply_text("Disfruta y saborea los placeres de la vida.\nSiguiente destino: 37°22\'37.8\"N 5°59\'11.9\"W")

def ub9_command(update, context):
    update.message.reply_text("Comprométete con tus objetivos.\nSiguiente destino: 37°24\'41.6\"N 6°02\'30.0\"W")

def ub10_command(update, context):
    update.message.reply_text("Afronta tus miedos.\nSiguiente destino: 36°58\'56.7\"N 5°56\'27.8\"W")

def ub11_command(update, context):
    update.message.reply_text("Cuida tu cuerpo.\nSiguiente destino: 36°50\'49.9\"N 6°19\'03.8\"W")

def finite_incantatum_command(update, context):
    update.message.reply_text("Has logrado desbloquear todas las ubicaciones que te guiaban a través de la felicidad, ahora el momento de crear tu propio camino.\nRecuerda estoy aquí para ayudarte")

def t1_command(update, context):
    update.message.reply_text("ESQUIAR")

def t2_command(update, context):
    update.message.reply_text("MUSICAL")

def t3_command(update, context):
    update.message.reply_text("PAINTBALL")

def t4_command(update, context):
    update.message.reply_text("HARRY POTTER EN LONDRES")

def t5_command(update, context):
    update.message.reply_text("VIA FERRATA")

def t6_command(update, context):
    update.message.reply_text("PARQUE ACUÁTICO")

def t7_command(update, context):
    update.message.reply_text("IMAGINE DRAGONS")

def t8_command(update, context):
    update.message.reply_text("BUCEAR")

def t9_command(update, context):
    update.message.reply_text("PASEO POR LOS TEJADOS DE SEVILLA + SEVILLA ENCANTADA")

def t10_command(update, context):
    update.message.reply_text("NOCHE BLANCA + DISFRASE PARTY")

def t11_command(update, context):
    update.message.reply_text("MONÓLOGO")

def t12_command(update, context):
    update.message.reply_text("CENA CON ASESINATO")

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} cause error {context.error}")


def main():
    updater = Updater(keys.API_KEY, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("first_kiss", ub1_command))
    dp.add_handler(CommandHandler("embarcadero", ub2_command))
    dp.add_handler(CommandHandler("casa_azul", ub3_command))
    dp.add_handler(CommandHandler("setas_1", ub4_command))
    dp.add_handler(CommandHandler("plaza_pilato", ub5_command))
    dp.add_handler(CommandHandler("salvador", ub6_command))
    dp.add_handler(CommandHandler("patio_agua", ub7_command))
    dp.add_handler(CommandHandler("laberinto", ub8_command))
    dp.add_handler(CommandHandler("sfdk", ub9_command))
    dp.add_handler(CommandHandler("titan_cabeza", ub10_command))
    dp.add_handler(CommandHandler("algaida", ub11_command))
    dp.add_handler(CommandHandler("finite_incantatum", finite_incantatum_command))
    dp.add_handler(CommandHandler("17", t1_command))
    dp.add_handler(CommandHandler("23", t1_command))
    dp.add_handler(CommandHandler("19", t1_command))
    dp.add_handler(CommandHandler("22", t1_command))
    dp.add_handler(CommandHandler("39", t1_command))
    dp.add_handler(CommandHandler("7", t1_command))
    dp.add_handler(CommandHandler("16", t1_command))
    dp.add_handler(CommandHandler("11", t1_command))
    dp.add_handler(CommandHandler("28", t1_command))
    dp.add_handler(CommandHandler("8", t1_command))
    dp.add_handler(CommandHandler("12", t1_command))
    dp.add_handler(CommandHandler("13", t1_command))


    
    
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)
  
    updater.start_polling(1)
    updater.idle()


main()