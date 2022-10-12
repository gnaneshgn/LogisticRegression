import numpy as np
from logistic_regression.exception import LogisticRegressionException
from logistic_regression.logger import logging
import sys,os



class LogisticRegression:

    def __init__(self,learning_rate=0.01,number_of_iterations=1000):
        self.lr=learning_rate
        self.iterations=number_of_iterations
        self.weights=None
        self.bias=None
        logging.info("Intiated")

    def fit(self,X,y):
        try:
            rows,cols=X.shape
            logging.info("Initializing weights and bias")
            #initalizing weights and bias 
            self.weights=np.zeros(cols)
            self.bias=0
            logging.info("Initializing gradient descent")
            for i in range(self.iterations):
                formula=np.dot(X,self.weights)+self.bias
                y_pred=self.sigmoid(formula)

                #computing/Derviating cost function wrt weights and bias
                logging.info("Weights and bias are derivatives initiated")
                dw=(1/rows)*np.dot(X.T,(y_pred-y))
                db=(1/rows)*np.sum(y_pred-y)

                #updating weights and bias
                self.weights=self.weights-self.lr*dw
                self.bias=self.bias-self.lr*db
                logging.info("Weights and bias are updated")


        except Exception as e:
            raise LogisticRegressionException(e,sys) from e  

    def sigmoid(self,X):
        return 1/(1+np.exp(-X)) 

    def predict(self,X):
        formula=np.dot(X,self.weights)+self.bias
        y_pred=self.sigmoid(formula)
        y_pred_class=[ 1 if i >0.5 else 0 for i in y_pred]
        return np.array(y_pred_class)
