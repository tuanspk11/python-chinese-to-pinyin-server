from flask import Flask
from flask import request, jsonify
from flask_cors import CORS
from pinyin import get

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return 'Get PINYIN | OK'

@app.route('/pinyin', methods=['POST'])
def get_pinyin():
    text = request.json['text']
    result = {"pinyin": get(text, delimiter=" ")}
    return jsonify(result)

if __name__ == '__main__':
    app.run()