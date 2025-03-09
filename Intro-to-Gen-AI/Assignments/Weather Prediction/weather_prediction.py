
"""

#Get the dataset
1. Load the dataset
2. Data processing 
    - Check for null values or undefined or NaN
    - Fix that using filling ffill ( with mean, median or mode)
    - Remove  rows/columsn with missing values

Normalize numerical feature
    - Min-max sclaing or Z-score normalization
    sklearn.preprocessing - scaling and normalization

Splitting the data :
    Use sklearn.model_selection.train_test_split to split the data.

    
Traing the Decision Tree:
    Import the DecisionTreeClassifier class from sklearn.tree.
    Create an instance of the class.
    Use the fit method to train the model on the training data.

    
Debugging issue:
Test for Over splitting and Under Splitting

sklearn.metrics.accuracy_score.

Experiment with different values for max_depth and min_samples_split in the DecisionTreeClassifier.

Use techniques like SMOTE (Synthetic Minority Oversampling Technique) to balance the dataset if needed.


Evaluating the model:
Use the predict method to generate predictions on the test set.

Evaluating using the metrics:


Use sklearn.metrics to calculate accuracy, precision, recall, and confusion matrix.

Analyze the results to understand the model's strengths and weaknesses. 
"""
