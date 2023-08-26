from LinearRegression import *

class LinearRegression1D(LinearRegression):
    
    def fit(self,X,y):
        self._feature = X
        self._target = y
        m = len(X)

        X = X.reshape(X.shape[0])
        x_sum = np.sum(X)
        y_sum = np.sum(y)
        x2_sum = np.sum([x * x for x in X])
        xy_sum = X.dot(y)
        
        self._coeff = (m * xy_sum - x_sum * y_sum)/(m * x2_sum - x_sum**2)
        self._intercept = (y_sum * (x_sum**2) - x_sum * xy_sum)/(m * x2_sum - x_sum**2)
        print(f"Fit intercept: {self._intercept}\n")
        print(f"Fit coefficients: {self._coeff}\n")
        
