from flask import Flask
from flask import request
from flask import jsonify
from flask import json

import urllib.request
from urllib.parse import quote

app = Flask(__name__)

SIMSIMI_KEY = "9310aede-3367-4f88-8654-0594a43bf8f0"
SIMSIMI_URL = "http://sandbox.api.simsimi.com/request.p?key=" + SIMSIMI_KEY


def draw_line():
    line = "* = " * 20
    print(line)


def getRequest(url, data=None):
    try:
        print(url)
    except:
        pass
    finally:
        return urllib.request.Request(url=url, data=data)


@app.route("/")
def hello():
    return "Welcome to MJ's Chat Bot!"


@app.route("/keyboard")
def keyboard():
    return jsonify(type="text")
    # return jsonify(type="buttons", buttons=["KOREAN", "ENGLISH", "CHINESE"])


@app.route("/message", methods=['POST'])
def message():
    draw_line()
    parsed = json.loads(request.data)
    print("USER >> " + parsed["content"])

    text = parsed["content"]
    url = SIMSIMI_URL + '&lc=%s&ft=1.0&text=%s' % ('ko', quote(text))

    url_request = getRequest(url=url)
    response = urllib.request.urlopen(url_request)

    data = response.read().decode('utf-8', 'replace')
    res = json.loads(data)

    if res['result'] != 100:
        result = '?'
        print(res)
    else:
        if 'response' in res.keys():
            result = res['response']

    print("MJ Chat Bot >> " + result)
    draw_line()

    text = {
        "message": {
            "text": result
        }
    }
    return jsonify(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
