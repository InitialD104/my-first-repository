import numpy as np
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')

from sklearn.datasets import load_diabetes
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV, train_test_split


def diabetes():
    diabetes_df = pd.read_csv(
    'http://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data',
    header=None)
    x = diabetes_df.iloc[:, :8]
    y = diabetes_df.iloc[:, 8:].values.flatten()
    X_train, X_test, Y_train, Y_test=train_test_split(X,Y,random_state=0)
    svc=SVC()
    svc.fit(X_train, Y_train)
    print('Train score: {:.3f}'.format(svc.score(X_train, Y_train)))
    print('Test score: {:.3f}'.format(svc.score(X_test, Y_test)))
    # print('x shape: {}, y shape:{}'.format(X.shape, Y.shape))


if __name__ == '__main__':
    diabetes()

# X=diabetes.data
# Y=diabetes.target
# diabetes_data = DataFrame(X, columns=("age", "sex", "bmi", "map", "tc", "ldl", "hdl", "tch", "ltg", "glu"))
