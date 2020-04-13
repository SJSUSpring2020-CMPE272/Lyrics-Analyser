import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import seaborn as sns
sns.set()
features = pd.read_csv("composite_dataset.csv")
print(features.head())
print('The shape of our features is:', features.shape)
features.describe()

y = np.array(features['Target'])
features= features.drop('Target', axis = 1)
print(features.head())

# Saving feature names for later use
feature_list = list(features.columns)
features = np.array(features)

X = features
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.10, random_state=1)
knn = KNeighborsClassifier(n_neighbors=4, metric='euclidean')
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
confusion_matrix(y_test, y_pred)
