import pytest
import numpy as np
import pandas as pd
import steps.load_data as load_data
import steps.preprocessing as preprocessing

def test_split_train_test():
    dataset = load_data.load_raw_data()
    X_train, X_test, y_train, y_test= preprocessing.split_train_test(dataset)
    assert X_train.empty == False
    assert X_test.empty == False
    assert y_train.empty == False
    assert y_test.empty == False