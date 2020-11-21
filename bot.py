import os
from markov import Markov
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

key = open("key", encoding="utf8").readline()
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text("neurolinguistic programming.")

def markov_fn(p):
    def retfun(update, context):
        msg = ""
        if len(context.args) > 0:
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

    for f in os.listdir():
        name, ext = os.path.splitext(f)[1]
        if ext != ".txt":
            continue
        dispatcher.add_handler(
            CommandHandler(name, markov_fn(Markov(f)))
        )
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
