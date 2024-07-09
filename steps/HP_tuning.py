import pandas as pd
import numpy as np

from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

#This method is going to find optimal hyperparameters for SVC
# using GridSearchCV
def hyperparameter_tuning(X, y):
    svc_model = SVC()

    svc_parameters = {'kernel': ('linear', 'rbf'),
                      'C': [0.1, .05, 1, 3, 5, 7, 9, 10],
                      'gamma': ('scale', 'auto')
                      }
    svc_grid = GridSearchCV(svc_model, svc_parameters, n_jobs=-1, verbose=4, refit=True)
    svc_grid.fit(X, y)
    print("GridSearchCV best parameters:", svc_grid.best_params_)
    print("GridSearchCV best parameters score:", svc_grid.best_score_)
