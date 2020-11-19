from markov import Markov
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

key = open("key", encoding="utf8").readline()

chobber = Markov("chob.txt")
asa     = Markov("asar.txt")
brando  = Markov("bran.txt")
logger  = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text("neurolinguistic programming.")

def markov_fn(n, p):
    msg = ""
    try:
        msg = p.gen(int(context.args[0]))
    except:
        msg = p.gen(50)
    return msg

def chob(update, context):
    if(len(context.args) > 0):
        msg = markov_fn(context.args[0], asa)
    else:
        msg = markov_fn(50, asa)
    update.message.reply_text(msg)

def bran(update, context):
    if(len(context.args) > 0):
        msg = markov_fn(context.args[0], asa)
    else:
        msg = markov_fn(50, asa)
    update.message.reply_text(msg)

def asar(update, context):
    if(len(context.args) > 0):
        msg = markov_fn(context.args[0], asa)
    else:
        msg = markov_fn(50, asa)
    update.message.reply_text(msg)
    
def main():
    updater = Updater(key, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("chob", chob))    
    dispatcher.add_handler(CommandHandler("bran", bran))
    dispatcher.add_handler(CommandHandler("asar", asar))        
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
