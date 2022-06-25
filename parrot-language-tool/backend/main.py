from flask import Flask, jsonify
from gap_text import GapText
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

gap_text = GapText()


@app.route("/gap_text", methods=["GET"])
def starting_url():
    return jsonify(
        gap_text.get_sentences()
    )


app.run(
    host="127.0.0.1",
    port=5000
)
