import pandas as pd
import sys
import mlflow
from steps.load_data import load_raw_data
from steps.preprocessing import split_train_test
from steps.HP_tuning import hyperparameter_tuning
from steps.train_model import model_training


def pipeline():
    print("Pipeline started...:")
    mlflow.set_experiment("mlflow_project")
    print("Starting data load step.")
    data = load_raw_data()
    print("Data load returned the dataframe:",data.info())
    print("Starting pre-processing step.")
    X_train, X_test, y_train, y_test= split_train_test(data)
    print("Pre processing step ended.")
    print("Starting hyperparameter tuning step.")
    #hyperparameter_tuning(X_train, y_train)
    model_training(X_train,y_train)
if __name__ == "__main__":
    print("main.py started.")
    pipeline()
