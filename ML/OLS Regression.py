import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

#"Length","Most","Average","Unique","IndexLength","IndexMost","IndexAverage","IndexUnique","IndexNormalizedLength","IndexNormalizedUnique","FinalIndex","WeightLength","WeightUnique"

dataset = pd.read_csv("featured_dataset.csv", usecols = ["IndexLength","IndexMost","IndexAverage","IndexUnique","WeightLength"])


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

X = dataset.drop('WeightLength',axis=1).values
y= dataset['WeightLength'].values
model = OrdinaryLeastSquares()
model.fit(X,y)
print(model.coefficients)
model.predict(X[0])

y_preds = []

for row in X :
  #  print(row)
    y_preds.append(model.predict(row))

correct=0
incorrect=0
for i in range(len(y_preds)):
 #   print(f'Actual : {float(y[i])} and Predicted {float(y_preds[i])}')
    if((float(y[i])-float(y_preds[i]))<10):
        correct=correct+1
    else:
        incorrect=incorrect+1

print(correct)
print(incorrect)
