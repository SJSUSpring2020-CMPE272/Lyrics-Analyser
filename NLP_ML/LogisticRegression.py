import numpy as np
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def run_logreg(training_dataset,user_data):
    features = training_dataset
    input = np.array(user_data)
    input = input.reshape(1,-1)
#    print('The shape of our features is:', features.shape)

    labels = np.array(features['Target'])
    features= features.drop('Target', axis = 1)
    feature_list = list(features.columns)
    features = np.array(features)

    # Split the data into training and testing sets
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.20, random_state = 10)
#    print('Training Features Shape:', train_features.shape)
#    print('Training Labels Shape:', train_labels.shape)
#    print('Testing Features Shape:', test_features.shape)
#    print('Testing Labels Shape:', test_labels.shape)

    logreg = LogisticRegression()
    logreg.fit(train_features, train_labels)

    predictions = logreg.predict(test_features)
#    print(confusion_matrix(test_labels, predictions))
#    print("Accuracy:", metrics.accuracy_score(test_labels, predictions))
#    print("Precision:", metrics.precision_score(test_labels, predictions))
#    print("Recall:", metrics.recall_score(test_labels, predictions))
    accuracy = accuracy_score(test_labels,predictions)
    response = logreg.predict(input)
    return round(accuracy,2), str(response)