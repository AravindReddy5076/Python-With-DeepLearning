f = open('input.txt', 'r', encoding='utf-8')
input = f.read()

input = "This is a sentence. Not a stop word and stemmer"

import nltk

nltk.download('punkt')

stokens = nltk.sent_tokenize(input)
wtokens = nltk.word_tokenize(input)

for s in stokens:
    print(s)

print('\n')

for t in wtokens:
    print(t)

#  pos
nltk.download('averaged_perceptron_tagger')

print(nltk.pos_tag(wtokens))

# T: Stemming
from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import LancasterStemmer

ps = PorterStemmer()
sb = SnowballStemmer('english')
lc = LancasterStemmer()
for x in wtokens:
    print(ps.stem(x))
    print(sb.stem(x))
    print(lc.stem(x))

#  Lemmatization
from nltk.stem import WordNetLemmatizer

nltk.download('wordnet')

wtokens = nltk.word_tokenize(input)

lemmatizer = WordNetLemmatizer()

for x in wtokens:
    print(lemmatizer.lemmatize(x))

#  Trigram
nltk.download('maxent_ne_chunker')
nltk.download('words')

stokens = nltk.sent_tokenize(input)

for sent in stokens:
    wtokens = nltk.word_tokenize(sent)
    for j in range(len(wtokens) - 2):
        print(wtokens[j], wtokens[j + 1], wtokens[j + 2])

#  Named Entity Recognition
from nltk import wordpunct_tokenize, pos_tag, ne_chunk

stokens = nltk.sent_tokenize(input)

for i in stokens:
    print(ne_chunk(pos_tag(wordpunct_tokenize(i))))