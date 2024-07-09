import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

#this step will split the dataframe to training and testing dataset
def split_train_test(heart_df):
    # split data in training and test set
    X_train, X_test, y_train, y_test = train_test_split(heart_df.drop(columns=['target']),
                                                        heart_df['target'], test_size=0.2, random_state=20)
    return X_train, X_test, y_train, y_test