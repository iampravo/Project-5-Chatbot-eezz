from intent_processor import get_response
from flask import Flask
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from flask import request
from flask import render_template
from flask import jsonify

app = Flask(__name__)

hello_esg = ChatBot("Hello ESG!")
trainer = ChatterBotCorpusTrainer(hello_esg)
trainer.train("chatterbot.corpus.english")

trainer.train('chatterbot.corpus.english.greetings')
trainer.train('chatterbot.corpus.english.conversations')


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/api/', methods=['POST'])
def get_bot_response_post():
    data = request.get_json()
    prediction = get_response(data)
    return jsonify(prediction)


@app.route('/get')
def get_bot_response_get():
    data = request.args.get('msg')
    prediction = get_response(data)
    return jsonify(prediction)


@app.route("/voice")
def index1():
    return render_template("index_voice_bot.html")


@app.route("/ask", methods=['POST'])
def ask():
    message = (request.form['messageText'])

    while True:
        if message == "":
            continue
        else:
            bot_response = str(get_response(message))
        return jsonify({'status': 'OK', 'answer': bot_response})


if __name__ == '__main__':
    app.run(host='MUUWDP1715', port=5002, debug='true')
