from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
import pickle
def model_training(X_train, y_train):
    print("Training SVC model with hyperparameter setting kernel=rbf, C=1, gamma=auto")
    svc_model = SVC(kernel='rbf', C=1, gamma='auto')
    mean_corss_validation_score = cross_val_score(svc_model, X_train, y_train, cv=10, scoring='accuracy').mean()
    print("Mean corss validation score for SVC model:",mean_corss_validation_score)
    # Saving model to pickle file
    with open("models/SVC_heart_classifier.pkl","wb") as file:
        pickle.dump(svc_model, file)