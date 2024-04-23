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

# Path = "./WordsCount"
# Path2 = "./WikipediaArticle/"

def change_file_to_words_count(filename,Path,Path2):
    try:
        file = open(os.path.join(Path2,filename),"r",encoding='utf-8')
    except FileNotFoundError as e:
        return
    text = file.read()
    word_counts = words_counter(text)
    filepath = os.path.join(Path,filename)
    file2 = open(filepath,'w',encoding='utf-8')

    for word, count in word_counts.items():
        if word.isascii():
            file2.write(word + " " + str(count) + "\n")

    file.close()


def all_change_file_to_words_count(path1,path2):
    path1 = os.path.abspath(path1)
    path2 = os.path.abspath(path2)
    input_files = set(os.listdir(path1))
    # output_files = set(os.listdir(path2))
    output_files = set()
    
    i = 1
    for file in input_files:
        if file not in output_files:
            change_file_to_words_count(file,path2,path1)
            print(i)
            i+=1


p2 = "YourPath\\WikipediaArticles"
p1 = "YourPath\\WordsCount2"
all_change_file_to_words_count(p2,p1)

