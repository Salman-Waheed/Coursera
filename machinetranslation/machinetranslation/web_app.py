from flask import Flask, request, jsonify
from translator import translate_french_to_english, translate_english_to_french

app = Flask(__name__)

@app.route('/translate/french-to-english', methods=['POST'])
def translate_french_to_english_endpoint():
    data = request.get_json()
    french_text = data['text']
    translated_text = translate_french_to_english(french_text)
    return jsonify({'translated_text': translated_text})

@app.route('/translate/english-to-french', methods=['POST'])
def translate_english_to_french_endpoint():
    data = request.get_json()
    english_text = data['text']
    translated_text = translate_english_to_french(english_text)
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run()
