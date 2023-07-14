from deep_translator import MyMemoryTranslator

def translate_english_to_french(text):
    translator = MyMemoryTranslator(source='en-US', target='fr-FR')
    translated_text = translator.translate(text)
    return translated_text

def translate_french_to_english(text):
    translator = MyMemoryTranslator(source='fr-FR', target='en-US')
    translated_text = translator.translate(text)
    return translated_text
