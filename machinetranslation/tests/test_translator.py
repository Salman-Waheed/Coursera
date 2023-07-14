import unittest
from machinetranslation.machinetranslation.translator import translate_french_to_english, translate_english_to_french

class TranslatorTestCase(unittest.TestCase):
    def test_french_to_english_translation(self):
        french_text = "Bonjour"
        translated_text = translate_french_to_english(french_text)
        expected_english_text = "Hi"  # Update the expected translation here
        self.assertEqual(translated_text, expected_english_text)

    def test_english_to_french_translation(self):
        english_text = "Hello"
        translated_text = translate_english_to_french(english_text)
        expected_french_text = "Bonjour"
        self.assertEqual(translated_text, expected_french_text)

if __name__ == '__main__':
    unittest.main()
