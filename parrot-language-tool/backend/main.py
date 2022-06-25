from flask import Flask, jsonify
from gap_text import GapText

app = Flask(__name__)
gap_text = GapText()


@app.route("/gap_text", methods=["GET"])
def starting_url():

    data = {
        "text": gap_text.get_sentences()
    }

    return jsonify(data)


app.run(
    host="127.0.0.1",
    port=5000
)
