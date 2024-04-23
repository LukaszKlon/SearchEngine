import scipy.sparse as sp
import numpy as np
from engine import request
import os

current_path = os.path.dirname(__file__)
DictPath = os.path.join(current_path,  '..', 'files', 'dict.txt')
MatrixPath = os.path.join(current_path, '..', 'files', 'matrix.npz')
Articles = os.path.join(current_path, '..', 'files', 'articles.txt')
MatrixUS = os.path.join(current_path, '..', 'files', 'US3000.npy')
MatrixVT = os.path.join(current_path, '..', 'files', 'VT3000.npy')

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

def load_files():
    WordsDict = create_words_dict(DictPath)
    FilesDict = create_files_dict(Articles)
    Matrix = sp.load_npz(MatrixPath)
    US = np.load(MatrixUS)
    VT = np.load(MatrixVT)

    return WordsDict,FilesDict,Matrix,US,VT