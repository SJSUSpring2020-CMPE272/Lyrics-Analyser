import numpy as np
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split

def run_random_forest(training_dataset,user_data):
    features = training_dataset
    input = np.array(user_data)
    input = input.reshape(1,-1)
#    print('The shape of our features is:', features.shape)

    # Labels are the values we want to predict
    labels = np.array(features['Target'])
    # Remove the labels from the features
    # axis 1 refers to the columns
    features= features.drop('Target', axis = 1)
    # Saving feature names for later use
    feature_list = list(features.columns)
    # Convert to numpy array
    features = np.array(features)

    # Split the data into training and testing sets
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.10, random_state = 10)
#    print('Training Features Shape:', train_features.shape)
#    print('Training Labels Shape:', train_labels.shape)
#    print('Testing Features Shape:', test_features.shape)
#    print('Testing Labels Shape:', test_labels.shape)
    # Instantiate model with 100 decision trees
    rfc = RandomForestClassifier(n_estimators = 100)
    # Train the model on training data
    rfc.fit(train_features, train_labels);

    # Use the forest's predict method on the test data
    predictions1 = rfc.predict(test_features)
#    print(confusion_matrix(test_labels, predictions1))

    resp1 = rfc.predict(input)

    accuracy1 = accuracy_score(test_labels, predictions1)

    # Instantiate model with 100 decision trees
    rfr = RandomForestRegressor(n_estimators = 100)
    # Train the model on training data
    rfr.fit(train_features, train_labels);

    # Use the forest's predict method on the test data
    predictions2 = rfr.predict(test_features)
    resp2 = rfr.predict(input)

    return str(resp1) , str(resp2) , round(accuracy1,2)