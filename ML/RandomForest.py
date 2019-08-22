import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import datetime

"""
Random Forest regression algorithm each row of feature based on full session,flow up and down
Works for both app predicting and video/non video classifying 
Need upgrade this in this section 
"""


def run_rfr(test_size, num_trees, rs_test_train, rs_regressor):

    #   only for video/no video, for app remove
    # One-hot encode the data using pandas get_dummies

    features = pd.read_csv('test1.csv')
    features = features.sample(frac=1)
    features['label'] = features['label'].astype(str)
    features = pd.get_dummies(features)

    # Labels are the values we want to predict
    labels = np.array(features[['label_ketchup', 'label_mayo', 'label_soy']])
    # Remove the labels from the features
    # axis 1 refers to the columns
    # Convert to numpy array
    features = features.drop(['label_ketchup', 'label_mayo', 'label_soy'], axis=1)

    cols = features.columns
    features = np.array(features)

    # Split the data into training and testing sets
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=test_size,
                                                                                random_state=rs_test_train)
    rf = RandomForestClassifier(n_estimators=num_trees, random_state=rs_regressor)

    # Train the model on training data
    rf.fit(train_features, train_labels)
    start_test = datetime.datetime.now()
    predictions = rf.predict(test_features)
    print("Done testing in", datetime.datetime.now() - start_test, "seconds")
    # Calculate the absolute errors

    print("Train Accuracy:", metrics.accuracy_score(train_labels, rf.predict(train_features)))
    print("Test Accuracy:", metrics.accuracy_score(predictions, test_labels))
    print(" Confusion matrix\n", confusion_matrix(test_labels.argmax(axis=1), predictions.argmax(axis=1)))

    feature_importances = pd.DataFrame(rf.feature_importances_,
                                       index=cols,
                                       columns=['importance']).sort_values('importance', ascending=False)
    print(feature_importances)


run_rfr(0.30, 1156, 49, 53)
