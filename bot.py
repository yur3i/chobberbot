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

def markov_fn(p):
    def retfun(update, context):
        msg = ""
        if(len(context.args) > 0):
            try:
                msg = p.gen(int(context.args[0]))
            except:
                msg = p.gen(50)
        else:
            msg = p.gen(50)
        update.message.reply_text(msg)
    return retfun

def main():
    updater = Updater(key, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("chob", markov_fn(chobber)))    
    dispatcher.add_handler(CommandHandler("bran", markov_fn(brando)))
    dispatcher.add_handler(CommandHandler("asar", markov_fn(asa)))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
