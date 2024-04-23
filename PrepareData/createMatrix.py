import os
import scipy.sparse as sp
import numpy as np

MatrixPath = os.path.abspath("YourPath\\matrix.npz")
WordsCount = os.path.abspath("YourPath\\WordsCount2")
DictPath = os.path.abspath("YourPath\\dict.txt")

def load_dict():
    Dict = dict()
    file = open(DictPath,"r",encoding='utf-8')
    index = 0
    for line in file.readlines():
        
        word,_ = line.split()
        Dict[word] = index
        index += 1
    file.close()
    return Dict


def create_matrix_vector(filename,dictionary,title):
    vector = sp.dok_matrix((1,len(dictionary)),dtype=np.float64)
    file = open(filename,"r",encoding='utf-8')
    all_words = 0
    for line in file.readlines():
        word, cnt = line.split()
        if word in dictionary:
            index = dictionary[word]
            vector[0,index] = int(cnt)
            all_words += int(cnt)
    file.close()
    
    return vector.tocsr()
    

def create_Matrix():

    files = os.listdir(WordsCount)
    dictionary = load_dict()
    vectors = []
    print("create vectors")

    for filename in files:
        vectors.append(create_matrix_vector(os.path.join(WordsCount,filename),dictionary,filename))
        
    vectors = sp.vstack(vectors)

    print("IDF prepare")
    N = vectors.shape[0]
    words_in_file = (vectors > 0).astype(np.int64)
    N_w = np.array(words_in_file.sum(axis=0))[0]
    IDF = np.log(N /N_w)
    IDF_diag = sp.diags(IDF)
    vectors = vectors.dot(IDF_diag)

    
    print("normalize")
    row_norm = sp.linalg.norm(vectors,axis=1)
    row_norm_inv = 1 / row_norm
    row_mat = sp.diags(row_norm_inv)


    vectors_IDF_normalize = row_mat.dot(vectors)
    
    sp.save_npz(MatrixPath,vectors_IDF_normalize)
    print("save")


create_Matrix()

