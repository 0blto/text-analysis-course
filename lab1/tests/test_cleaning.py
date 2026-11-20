"""Проверка leet и числовых записей в реальном конвейере ноутбука."""
import json
from pathlib import Path
import re
import unittest

notebook = json.loads((Path(__file__).resolve().parents[1] / 'notebook.ipynb').read_text())
source = next(''.join(c['source']) for c in notebook['cells']
              if c['cell_type'] == 'code' and 'def clean_text(' in ''.join(c['source']))
namespace = {'re': re}
exec(source.split('demo =')[0], namespace)
clean_text = namespace['clean_text']


class CleaningTests(unittest.TestCase):
    def test_cyrillic_leet(self):
        for text, expected in [('стукач0к', 'стукачок'), ('пр1вет', 'привет'), ('сл0во', 'слово')]:
            with self.subTest(text=text):
                self.assertEqual(clean_text(text), f'<s> {expected} </s>')

    def test_numeric_expressions(self):
        for text in ['5ооо рублей', '5000 рублей', '250к рублей', '5ooo рублей']:
            with self.subTest(text=text):
                self.assertEqual(clean_text(text), '<s> [NUM] рублей </s>')

    def test_existing_special_tokens(self):
        self.assertEqual(clean_text('@vasya https://example.com !!!'),
                         '<s> [USER] [URL] [EMPH] </s>')

    def test_leet_does_not_decode_model_numbers(self):
        for word in ['т90', 'ак74м', '2ch', 'ил-112']:
            with self.subTest(word=word):
                self.assertEqual(namespace['fix_leet'](re.fullmatch(r'.+', word)), word)
