import ism_mano
from telegram.ext import *
print("Bot ishga tushiyapti....")
def start(update,context):
    update.message.reply_html("<b>Assalomu aleykum, {}</b> \nIsmingizni kiriting va ma'nosini bilib oling".format(update.message.from_user.first_name))
def help(update,context):
    update.message.reply_text(update.message.from_user.first_name,"Agar yordam kerak bo'lsa,googledan so'rang")
def mano(update,context):
    ism=str(update.message.text).lower()
    ismmano=ism_mano.ism_mano(ism)
    update.message.reply_text(ismmano)
def gl():
    updater=Updater("Token",use_context=True)
    dpp=updater.dispatcher
    dpp.add_handler(CommandHandler("start",start))
    dpp.add_handler(CommandHandler("help", help))
    dpp.add_handler(MessageHandler(Filters.text,mano))

    updater.start_polling()
    updater.idle()
    print("Botingizga xato yo'q")
gl()
