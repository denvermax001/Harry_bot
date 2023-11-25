import os
from io import BytesIO
from queue import Queue
import requests
from flask import Flask, request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler, Dispatcher
from movies_scraper import search_movies, get_movie

TOKEN = os.getenv("TOKEN")
URL = os.getenv("URL")
bot = Bot(TOKEN)

def welcome_1(update, context) -> None:
    update.message.reply_text(f"Hello Dear, Welcome to NKFLIX.\n"
                              f"🔥 Download Your Favourite 🎬 Movies, Webseries & TV-Shows For 💯 Free And 🍿 Enjoy it.")
    update.message.reply_text(f"Join Our Official Channel & Discussion Group:\n"
                             f"Official Channel: @flixtvseries\n"
                             f"Discussion Group: @flixtvseriesdiscussion\n"
                             f"Join, Share & Support Us\n" 
                             f"🤗 ADMIN NKFLIX 🤗")  
    update.message.reply_text(f"Start searching using /search command.")

def welcome_2(update, context) -> None:
    update.message.reply_text("👇 Enter 🎬 Movie, Web-Series Or TV-Show Name Below 👇")

def find_movie(update, context):
    search_results = update.message.reply_text("Processing")
    query = update.message.text
    movies_list = search_movies(query)
    if movies_list:
        keyboards = []
        for movie in movies_list:
            keyboard = InlineKeyboardButton(movie["title"], callback_data=movie["id"])
            keyboards.append([keyboard])
        reply_markup = InlineKeyboardMarkup(keyboards)
        search_results.edit_text('Results', reply_markup=reply_markup)
    else:
        search_results.edit_text('Sorry 🥺, No result found!\nPlease retry Or contact admin.')

def movie_result(update, context) -> None:
    query = update.callback_query
    s = get_movie(query.data)
    response = requests.get(s["img"])
    img = BytesIO(response.content)
    query.message.reply_photo(photo=img, caption=f"🎥 {s['title']}")
    link = ""
    links = s["links"]
    for i in links:
        link += "🎬" + i + "\n" + links[i] + "\n\n"
    caption = f"Direct Download 📥 Links 🔗:\n\n{link}"
    if len(caption) > 4095:
        for x in range(0, len(caption), 4095):
            query.message.reply_text(text=caption[x:x+4095])
    else:
        query.message.reply_text(text=caption)

def setup():
    update_queue = Queue()
    dispatcher = Dispatcher(bot, update_queue, use_context=True)
    dispatcher.add_handler(CommandHandler('start', welcome_1))
    dispatcher.add_handler(CommandHandler('search', welcome_2))
    dispatcher.add_handler(MessageHandler(Filters.text, find_movie))
    dispatcher.add_handler(CallbackQueryHandler(movie_result))
    return dispatcher

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route('/{}'.format(TOKEN), methods=['GET', 'POST'])
def respond():
    update = Update.de_json(request.get_json(force=True), bot)
    setup().process_update(update)
    return 'ok'

@app.route('/setwebhook', methods=['GET', 'POST'])
def set_webhook():
    s = bot.setWebhook('{URL}/{HOOK}'.format(URL=URL, HOOK=TOKEN))
    if s:
        return "webhook setup ok"
    else:
        return "webhook setup failed"