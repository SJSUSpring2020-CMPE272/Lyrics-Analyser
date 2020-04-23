import numpy as np
import pandas as pd
import warnings

from sklearn.metrics import accuracy_score

warnings.filterwarnings('ignore')

class OrdinaryLeastSquares(object):

    def __init__(self):
        self.coefficients = []

    def fit(self, X, y):
        if len(X.shape) == 1: X = self._reshape_x(X)

        X = self._concatenate_ones(X)
        self.coefficients = np.linalg.inv(X.transpose().dot(X)).dot(X.transpose()).dot(y)

    def predict(self, entry):
        b0 = self.coefficients[0]
        other_betas = self.coefficients[1:]
        prediction = b0

        for xi, bi in zip(entry, other_betas): prediction += (bi * xi)
        return prediction

    def _reshape_x(self, X):
        return X.reshape(-1, 1)

    def _concatenate_ones(self, X):
        ones = np.ones(shape=X.shape[0]).reshape(-1, 1)
        return np.concatenate((ones, X), 1)

def run_linear_regression(training_dataset,user_data):
    dataset = training_dataset
    input = np.array(user_data)
#    input = input.reshape(1,-1)
#    print(dataset.head())
    X = dataset.drop('Target',axis=1).values
    y= dataset['Target'].values
    model = OrdinaryLeastSquares()
    model.fit(X,y)
    predictions = model.predict(X)
   # accuracy = accuracy_score(X,)
    print(predictions)
    coefficient = model.coefficients
    response = model.predict(input)
    return round(response,2)

#    model.predict(X[0])
#    y_preds = []
#    for row in X :
#        y_preds.append(model.predict(row))
#    correct=0;    incorrect=0
#    for i in range(len(y_preds)):
#        print(f'Actual : {float(y[i])} and Predicted {float(y_preds[i])}')
#        if((float(y[i])-float(y_preds[i]))<0.05):
#            correct=correct+1
#        else:
#            incorrect=incorrect+1
#    print(correct);    print(incorrect)

