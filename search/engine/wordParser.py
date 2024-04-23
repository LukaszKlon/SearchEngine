import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import os
import string


def words_counter(text):
    prepare = word_tokenize(text)
    prepare = remove_punctation(prepare)
    prepare = remove_words(prepare)
    prepare = stem_words(prepare)
    return count_words(prepare)


def remove_words(text):
    words_to_remove = set(stopwords.words('english'))
    return [word for word in text if word.lower() not in words_to_remove]

def remove_punctation(text):
    punctuations = str.maketrans('',"",string.punctuation)
    words = [word.translate(punctuations) for word in text]
    return [word for word in words if word]

def stem_words(text):
    PS = PorterStemmer()
    return [PS.stem(word) for word in text]

def count_words(text):
    return dict(nltk.FreqDist(text))


