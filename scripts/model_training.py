# model_training.py
# Utility functions for training and evaluating ML models for SpaceX prediction.

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score

def split_data(df, target_col, test_size=0.2, random_state=42):
    """Split dataset into X_train, X_test, y_train, y_test."""
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def evaluate_model(model, X_test, y_test):
    """Return the accuracy of a trained model."""
    predictions = model.predict(X_test)
    return accuracy_score(y_test, predictions)

def tune_hyperparameters(model, param_grid, X_train, y_train, cv=5):
    """Perform hyperparameter tuning and return the best estimator."""
    grid = GridSearchCV(model, param_grid, cv=cv)
    grid.fit(X_train, y_train)
    return grid.best_estimator_, grid.best_params_
