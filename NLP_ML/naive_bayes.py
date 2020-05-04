import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def run_nb(training_dataset,user_data):
    features = training_dataset
    input = np.array(user_data)
    input = input.reshape(1,-1)
#    print('The shape of our features is:', features.shape)

    labels = np.array(features['Target'])
    features= features.drop('Target', axis = 1)
    feature_list = list(features.columns)
    features = np.array(features)

    # Split the data into training and testing sets
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.15)
 #   print('Training Features Shape:', train_features.shape)
 #   print('Training Labels Shape:', train_labels.shape)
 #   print('Testing Features Shape:', test_features.shape)
 #   print('Testing Labels Shape:', test_labels.shape)

    gnb = GaussianNB()
    gnb.fit(train_features, train_labels)

    predictions = gnb.predict(test_features)
#    print(confusion_matrix(test_labels, predictions))
    accuracy = accuracy_score(test_labels,predictions)
    response = gnb.predict(input)
    #print("***** NAIVE BAYES *****")
    #print(round(accuracy,2))
    #print(response)
    return round(accuracy,2), str(response)