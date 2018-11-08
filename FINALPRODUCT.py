
from flask import jsonify, Flask
app = Flask(__name__)

@app.route("/luis")
def hello():
    return jsonify({
        'ghjdhsd': 'jdhkk',
    })


@app.route("/haha")
def bebe():
    return 'pokemon'
