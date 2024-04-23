import os
import scipy.sparse as sp
from sklearn.decomposition import TruncatedSVD
import numpy as np

MatrixPath = os.path.abspath("YourPath\\matrix.npz")
MatrixUS = os.path.abspath("YourPath\\US3000.npy")
MatrixVT = os.path.abspath("YourPath\\VT3000.npy")


def changeToSVD(k):
    Matrix = sp.load_npz(MatrixPath)

    svd = TruncatedSVD(n_components=k)
    svd.fit(Matrix)
    US = svd.transform(Matrix)
    VT = np.array(svd.components_)

    np.save(MatrixUS, US)
    np.save(MatrixVT, VT)


changeToSVD(3000)