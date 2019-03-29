import numpy as np
from sklearn import preprocessing

def sample_random_columns(mfcc, n_columns):
    row_ix = np.arange(mfcc.shape[0])
    row_ix = row_ix[1:mfcc.shape[0]]

    col_ix = np.arange(mfcc.shape[1])
    col_ix = np.random.choice(col_ix, (1, n_columns), replace=False)

    return mfcc[np.ix_(row_ix, col_ix[0])]

def extract_mfcc(speaker): 
    mfcc = np.frombuffer(speaker[6])
    mfcc = np.reshape(mfcc,(speaker[7], speaker[8]))
    mfcc = preprocessing.scale(mfcc)

    return mfcc


def extract_mfcc_as_rows(dataset, n_frames): 
    mfcc_vectors = np.asarray(())

    for speaker in dataset:
        mfcc = extract_mfcc(speaker)
        frames = sample_random_columns(mfcc, n_frames)
        if mfcc_vectors.size == 0:
            mfcc_vectors = frames.T
        else:
            mfcc_vectors = np.vstack((mfcc_vectors, frames.T))

    return mfcc_vectors
