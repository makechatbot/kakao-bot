from flask import Flask
from flask import request
from flask import jsonify
from flask import json
from chatterbot import ChatBot

app = Flask(__name__)

chatbot = ChatBot('MJ Chat Bot')


def draw_line():
    line = "* = " * 20
    print(line)


@app.route("/")
def hello():
    return "Welcome to MJ's Chat Bot!"


@app.route("/keyboard")
def keyboard():
    return jsonify(type="text")
    # return jsonify(type="buttons", buttons=["Test1", "Test2"])


@app.route("/message", methods=['POST'])
def message():
    draw_line()
    data = request.data.decode('utf-8', 'replace')
    parsed = json.loads(request.data)
    print("USER >> " + parsed["content"])

    response = chatbot.get_response(parsed["content"])
    print("MJ Chat Bot >> " + str(response))
    draw_line()

    text = {
        "message": {
            "text": str(response)
        }
    }
    return jsonify(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')