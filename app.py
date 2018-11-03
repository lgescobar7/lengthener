
from flask import jsonify, Flask
app = Flask(__name__)

@app.route("/luisisgay")
def hello():
    return jsonify({
        'ghjdhsd': 'jdhkk',
    })


@app.route("/haha")
def bebe():
    return 'pokemon'
