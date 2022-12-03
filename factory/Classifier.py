from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import Lasso
import config


class Classifier:

    def __init__(self):
        self.name = config.MODEL

    def get_model(self):
        if self.name == "svm":
            return svm.SVC(kernel='linear')
        elif self.name == "logistic_regression":
            return LogisticRegression(solver='lbfgs', max_iter=100000)
        else:
            return Lasso()

