import numpy
from sklearn import preprocessing

def sample_random_columns(mfcc, n_columns):
    row_ix = numpy.arange(mfcc.shape[0])
    row_ix = row_ix[1:mfcc.shape[0]]

    col_ix = numpy.arange(mfcc.shape[1])
    col_ix = numpy.random.choice(col_ix, (1, n_columns), replace=False)

    return mfcc[numpy.ix_(row_ix, col_ix[0])]

def extract_mfcc_vectors(dataset, n_frames): 
    mfcc_vectors = numpy.asarray(())

    for speaker in dataset:
        mfcc = numpy.frombuffer(speaker[6])
        mfcc = numpy.reshape(mfcc,(speaker[7], speaker[8]))
        mfcc = preprocessing.scale(mfcc)

        frames = sample_random_columns(mfcc, n_frames)
        if mfcc_vectors.size == 0:
            mfcc_vectors = frames
        else:
            mfcc_vectors = numpy.hstack((mfcc_vectors, frames))

    return mfcc_vectors.T
