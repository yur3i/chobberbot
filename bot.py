import os
from markov import Markov
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import pandas

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

def add_chess(update, context):
    add_game(context.args)
    update.message.reply_text("Added game")

def print_board(update, context):
    if context.args is not None and len(context.args) > 1:
        league = context.args[0]
    else:
        league = ""
    df = pandas.read_csv("{}chess.csv".format(league))
    update.message.reply_text(df.sort_values(by=['p'], ascending=False).to_string())

def main():
    updater = Updater(key, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    for f in os.listdir():
        name, ext = os.path.splitext(f)
        if ext != ".txt":
            continue
        dispatcher.add_handler(
            CommandHandler(name, markov_fn(Markov(f)))
        )
    
    dispatcher.add_handler(CommandHandler("league", print_board))
    dispatcher.add_handler(CommandHandler("addgame", add_chess))

    updater.start_polling()
    updater.idle()
if __name__ == '__main__':
    main()
