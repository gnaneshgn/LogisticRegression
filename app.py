import numpy as np
from sklearn import datasets
from logistic_regression.logger import logging
from logistic_regression.linear_models import LogisticRegression
from sklearn.metrics import accuracy_score


X,y=datasets.make_classification(n_samples=200,n_features=5)

logging.info("Sample data sets created")
classifier=LogisticRegression()
classifier.fit(X=X,y=y)
y_pred=classifier.predict(X)
logging.info(f" accuracy score for model is [{y_pred}] ")
print(y_pred)