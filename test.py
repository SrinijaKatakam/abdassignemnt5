from nltk.stem import PorterStemmer
import nltk
from nltk.tokenize import word_tokenize
import string
from nltk.corpus import stopwords



nltk.download('stopwords')
ps = PorterStemmer()


word_found = []
with open('Shakespeare.txt', 'r', encoding="utf-8-sig") as fileinput:
    for line in fileinput:
        for words in line.split():
            word_found.append(words.lower())

text = " ".join(word_found)
cleaned_text = []
text_tokens = word_tokenize(text)
for word_found in text_tokens:
    if word_found not in stopwords.words():
        cleaned_text.append(word_found)
cleaned_text = [''.join(c for c in s if c not in string.punctuation) for s in cleaned_text]
cleaned_text = list(filter(None, cleaned_text))
cleaned_text = ' '.join(cleaned_text)
with open('Shakespeareedit.txt', "w") as output:
    output.write(str(cleaned_text))
