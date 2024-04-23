import os
import scipy.sparse as sp
import numpy as np
import engine.wordParser as engine
from app.apps import AppConfig


current_path = os.path.dirname(__file__)
DictPath = os.path.join(current_path,  '..', 'files', 'dict.txt')
MatrixPath = os.path.join(current_path, '..', 'files', 'matrix.npz')
Articles = os.path.join(current_path, '..', 'files', 'articles.txt')
MatrixUS = os.path.join(current_path, '..', 'files', 'US3000.npy')
MatrixVT = os.path.join(current_path, '..', 'files', 'VT3000.npy')

def create_url(text):
    text.replace(" ","_")
    return f"https://simple.wikipedia.org/wiki/{text}"

def create_words_dict(Path):
    result = dict()
    file = open(Path,"r",encoding='utf-8')
    index = 0
    for line in file.readlines():
        word,_ = line.split()
        result[word] = index
        index += 1
    file.close()

    return result

def create_files_dict(Path):
    result = []
    file = open(Path,"r",encoding='utf-8')
    for line in file.readlines():
        result.append(line.replace("\n",""))
    file.close()
    
    return result

def words_to_vector(input,dict):
    result = np.zeros(len(dict))
    for word in input.keys():
        if word in dict:
            index = dict[word]
            result[index] = input[word]

    return result

def get_k_greatest(arr, k):
    sorted_indices = np.argsort(arr)[::-1]
    
    k_greatest_indices = sorted_indices[:k]
    k_greatest_values = arr[k_greatest_indices]
    
    return k_greatest_values, k_greatest_indices

def make_request_normal(input,k=10):
    wordsDict = AppConfig.dict
    fileDict = AppConfig.articles
    input_dict = engine.words_counter(input)
    # Matrix = sp.load_npz(MatrixPath)
    Matrix = AppConfig.Matrix

    vector = words_to_vector(input_dict,wordsDict).reshape(-1)
    vector = vector / np.linalg.norm(vector)

    result = Matrix.dot(vector)

    values, keys = get_k_greatest(result,k)
    
    res = []
    for value, key in zip(values,keys):
        title = fileDict[key].replace(".txt","")
        res.append({"title":title,"value":np.round(value*100,2),"link":create_url(title)})

    return res

def make_request_SVD(input,k=10):
    wordsDict = AppConfig.dict
    fileDict = AppConfig.articles
    input_dict = engine.words_counter(input)
    US = AppConfig.US
    VT = AppConfig.VT


    vector = words_to_vector(input_dict,wordsDict).reshape(-1)
    vector = vector / np.linalg.norm(vector)
    result = US @ (VT @ vector)
    values, keys = get_k_greatest(result,k)
    
    res = []
    for value, key in zip(values,keys):
        title = fileDict[key].replace(".txt","")
        res.append({"title":title,"value":np.round(value*100,2),"link":create_url(title)})

    return res
