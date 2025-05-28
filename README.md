# azerbaijan-punkt-tokenizer
Punkt tokenizer model for Azerbaijani language, compatible with NLTK.

# First we download custom_tokenizer.py and azerbaijani_custom.pickle 

# We use like that:

```python
import pickle

# Load AZ.pickle (trained standard Punkt model)
with open("tokenizers/punkt/AZ.pickle", "rb") as f:
    tokenizer = pickle.load(f)

text = "Ulvi kitab oxuyur.Sabah dərs var.Sən gələcəksən?"
print(tokenizer.tokenize(text))
