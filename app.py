from flask import Flask, render_template
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pymongo

mongodb_name = 'chatterbot'
mongodb_uri = 'mongodb://9.111.111.203'


app = Flask(__name__)

#english_bot = ChatBot("English Bot", storage_adapter="chatterbot.storage.SQLStorageAdapter")
english_bot = ChatBot("English Bot", 
                     storage_adapter = "chatterbot.storage.MongoDatabaseAdapter",
                     database = mongodb_name,
                     database_uri = mongodb_uri)

english_bot.set_trainer(ChatterBotCorpusTrainer)
english_bot.train("chatterbot.corpus.english")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get/<string:query>")
def get_raw_response(query):
    return str(english_bot.get_response(query))


if __name__ == "__main__":
    app.run()
