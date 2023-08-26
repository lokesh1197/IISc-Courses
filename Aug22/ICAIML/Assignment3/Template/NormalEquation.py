import numpy as np
from LinearRegression import *

class NormalEquation(LinearRegression):
    def fit(self, X, y):
        """
        Fit model coefficients.

        Arguments:
        X: 1D or 2D numpy array 
        |x11 x12  .... x1n | 
        |x21 x22  .... x2n |
        | .   .     .   .  |
        | .   .     .   .  |
        |xm1 xm2  .... xmn |

        y: 1D numpy array
        | y1 |
        | y2 |
        | .  |
        | .  |
        | ym |
        """
        self._feature = X
        self._target = y
        
        if len(X.shape) == 1: # check if X is 1D or 2D array
            X = X.reshape(-1,1) #reshape to column vector if 1D 
            
        # add bias terms to feature matrix
        X_biased = np.c_[np.ones(X.shape[0]), X] #Adds a leading column of 1's to feature matrix to fit the intercept
        #| 1 x11 x12  .... x1n | 
        #| 1 x21 x22  .... x2n |
        #| .  .   .     .   .  |
        #| .  .   .     .   .  |
        #| 1 xm1 xm2  .... xmn |
        
        
        # closed form solution
        sol = np.linalg.inv(X_biased.transpose().dot(X_biased)).dot(X_biased.transpose()).dot(y)
        
        self._intercept = sol[0]
        self._coeff = sol[1:]
        print(f"Fit intercept: {self._intercept}\n")
        print(f"Fit coefficients: {self._coeff}\n")

        
        



       
