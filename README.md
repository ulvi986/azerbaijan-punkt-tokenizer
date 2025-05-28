# azerbaijan-punkt-tokenizer
Punkt tokenizer model for Azerbaijani language, compatible with NLTK.

# First we download custom_tokenizer.py and azerbaijani_custom.pickle 

# We use like that:
"""
import pickle

# Tokenizer-i yüklə
with open("azerbaijani_custom.pickle", "rb") as f:
    tokenizer = pickle.load(f)

texts = [
    "Sabah dərs var.Sən gələcəksən?",
    "Prof. Əli müəllim gəldi.Biz dərsə başladıq.",
    "Bu, bir testdir.Bakıdır.Gözəldir!",
    "İyul ayının 20-də getdik.Sən necə?",
]

for t in texts:
    print("\n📝 Mətndə:", t)
    print("🔍 Ayırma:", tokenizer.tokenize(t))


"""
