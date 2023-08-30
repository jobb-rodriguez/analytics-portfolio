# Rodriguez, Jobb Q.
# June 2, 2022
# Machine Learning Finals
# Import libraries
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import cross_validate
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression

# Read data
raw_data = pd.read_csv("cardio_train.csv")

# Without BMI
# Feature Scaling
scaler = StandardScaler().fit(raw_data)
# Apply the scaler
scaled_data = scaler.transform(raw_data)

scaled_data = pd.DataFrame(scaled_data, columns=raw_data.columns)
# We do not scale the target variable
y = raw_data["cardio"]
scaled_data.drop("cardio", axis=1, inplace=True)
scaled_data.drop("id", axis=1, inplace=True)

# First Configuration: Default
ann_clf = MLPClassifier()
# Fit the model to the training data without BMI
ann_clf.fit(scaled_data, y)
cv_results1 = cross_validate(ann_clf, scaled_data, y, cv=5, scoring=[
                             "accuracy"], return_train_score=True)
mean_train_cv_results1 = np.mean(cv_results1["train_accuracy"])
mean_test_cv_results1 = np.mean(cv_results1["test_accuracy"])
print(cv_results1)
print("Train Score: ", mean_train_cv_results1)
print("Test Score: ", mean_test_cv_results1)

# Second Configuration: set hidden_layer_sizes to (75,)
ann_clf = MLPClassifier(hidden_layer_sizes=(75,))
# Fit the model to the training data without BMI
ann_clf.fit(scaled_data, y)
cv_results2 = cross_validate(ann_clf, scaled_data, y, cv=5, scoring=[
                             "accuracy"], return_train_score=True)
mean_train_cv_results2 = np.mean(cv_results2["train_accuracy"])
mean_test_cv_results2 = np.mean(cv_results2["test_accuracy"])
print(cv_results2)
print("Train Score: ", mean_train_cv_results2)
print("Test Score: ", mean_test_cv_results2)

# Third Configuration: set hidden_layer_sizes to (75,), max_iter to 300, and tol to 0.00001
ann_clf = MLPClassifier(hidden_layer_sizes=(75,), max_iter=300, tol=0.00001)
ann_clf.fit(scaled_data, y)
cv_results3 = cross_validate(ann_clf, scaled_data, y, cv=5, scoring=[
                             "accuracy"], return_train_score=True)
mean_train_cv_results3 = np.mean(cv_results3["train_accuracy"])
mean_test_cv_results3 = np.mean(cv_results3["test_accuracy"])
print(cv_results3)
print("Train Score: ", mean_train_cv_results3)
print("Test Score: ", mean_test_cv_results3)

best_mean_train_result = np.max(
    [mean_train_cv_results1, mean_train_cv_results2, mean_train_cv_results3])
best_mean_test_result = np.max(
    [mean_test_cv_results1, mean_test_cv_results2, mean_test_cv_results3])
print("Best Mean Train Result: ", best_mean_train_result)
print("Best Mean Test Result: ", best_mean_test_result)

# Logistic Regression: Default
clf = LogisticRegression()
# Fit the model to the training data without BMI
clf.fit(scaled_data, y)
cv_results = cross_validate(clf, scaled_data, y, cv=5, scoring=[
                            "accuracy"], return_train_score=True)
mean_train_cv_results = np.mean(cv_results["train_accuracy"])
mean_test_cv_results = np.mean(cv_results["test_accuracy"])
print(cv_results)
print("Train Score: ", mean_train_cv_results)
print("Test Score: ", mean_test_cv_results)

# With BMI
raw_data_with_bmi = raw_data
# Drop cardio and id for X
X_bmi = raw_data_with_bmi.drop("cardio", axis=1)
X_bmi.drop("id", axis=1, inplace=True)
# Set the value of y
y_bmi = raw_data_with_bmi["cardio"]
# Add BMI as a column
X_bmi["BMI"] = X_bmi["weight"]/(X_bmi["height"]**2)

# Feature Scaling
scaler = StandardScaler().fit(X_bmi)
scaled_data = scaler.transform(X_bmi)
X_bmi = pd.DataFrame(scaled_data, columns=X_bmi.columns)

# First Configuration: Default
ann_clf = MLPClassifier()
# Fit the model to the training data without BMI
ann_clf.fit(X_bmi, y_bmi)
cv_results1 = cross_validate(ann_clf, X_bmi, y_bmi, cv=5, scoring=[
                             "accuracy"], return_train_score=True)
mean_train_cv_results1 = np.mean(cv_results1["train_accuracy"])
mean_test_cv_results1 = np.mean(cv_results1["test_accuracy"])
print(cv_results1)
print("Train Score: ", mean_train_cv_results1)
print("Test Score: ", mean_test_cv_results1)

# Second Configuration: set hidden_layer_sizes to (75,)
ann_clf = MLPClassifier(hidden_layer_sizes=(75,))
# Fit the model to the training data without BMI
ann_clf.fit(X_bmi, y_bmi)
cv_results2 = cross_validate(ann_clf, X_bmi, y_bmi, cv=5, scoring=[
                             "accuracy"], return_train_score=True)
mean_train_cv_results2 = np.mean(cv_results2["train_accuracy"])
mean_test_cv_results2 = np.mean(cv_results2["test_accuracy"])
print(cv_results2)
print("Train Score: ", mean_train_cv_results2)
print("Test Score: ", mean_test_cv_results2)

# Third Configuration: set hidden_layer_sizes to (75,), max_iter to 300, and tol to 0.00001
ann_clf = MLPClassifier(hidden_layer_sizes=(75,), max_iter=300, tol=0.00001)
ann_clf.fit(X_bmi, y_bmi)
cv_results3 = cross_validate(ann_clf, X_bmi, y_bmi, cv=5, scoring=[
                             "accuracy"], return_train_score=True)
mean_train_cv_results3 = np.mean(cv_results3["train_accuracy"])
mean_test_cv_results3 = np.mean(cv_results3["test_accuracy"])
print(cv_results3)
print("Train Score: ", mean_train_cv_results3)
print("Test Score: ", mean_test_cv_results3)

best_mean_train_result = np.max(
    [mean_train_cv_results1, mean_train_cv_results2, mean_train_cv_results3])
best_mean_test_result = np.max(
    [mean_test_cv_results1, mean_test_cv_results2, mean_test_cv_results3])
print("Best Mean Train Result: ", best_mean_train_result)
print("Best Mean Test Result: ", best_mean_test_result)

# Logistic Regression: Default
clf = LogisticRegression()
# Fit the model to the training data without BMI
clf.fit(X_bmi, y_bmi)
cv_results = cross_validate(clf, X_bmi, y_bmi, cv=5, scoring=[
                            "accuracy"], return_train_score=True)
mean_train_cv_results = np.mean(cv_results["train_accuracy"])
mean_test_cv_results = np.mean(cv_results["test_accuracy"])
print(cv_results)
print("Train Score: ", mean_train_cv_results)
print("Test Score: ", mean_test_cv_results)
