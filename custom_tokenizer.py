# custom_tokenizer.py
import re
from nltk.tokenize.punkt import PunktSentenceTokenizer

class CustomTokenizer(PunktSentenceTokenizer):
    def __init__(self, params):
        super().__init__(params)
        self._fix_re = re.compile(r'(?<=[a-zəöüığçş])([.?!])(?=[A-ZƏÖÜİĞÇŞ])')

    def _fix_spaces(self, text: str) -> str:
        return self._fix_re.sub(r'\1 ', text)

    def tokenize(self, text: str):
        clean = self._fix_spaces(text)
        return super().tokenize(clean)
