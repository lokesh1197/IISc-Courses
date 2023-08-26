import numpy as np
import matplotlib.pyplot as plt


class LinearRegression:
    def __init__(self) -> None:
        self._coeff = None
        self._intercept = None
        

    def __repr__(self) -> str:
        return "Linear Regression Model from  Parent Class"

    def predict(self, X_new):
        """Output model prediction.

        Arguments:
        X_new: 1D or 2D numpy array
        """
        if len(X_new.shape) == 1: # check if X is 1D or 2D array
            X_new = X_new.reshape(-1,1) #reshape to column vector if 1D 

        
        self._predicted = np.c_[np.ones(X_new.shape[0]), X_new].dot(np.c_[self._intercept, self._coeff])
        return self._predicted
    
    
    def error_metrics(self):
        self._fit  = np.dot(self._feature,self._coeff)+self._intercept
        self._residue = self._target - self._fit

        self._sse = np.sum([r ** 2 for r in self._residue])
        print(f"Sum of squared error for best fit: {self._sse}\n")
        self._mse = self._sse / len(self._residue)
        print(f"Mean squared error for best fit: {self._mse}\n")
    
    def fit_plot(self):

        plt.scatter(self._target, self._fit)
        plt.plot(self._target, self._target, "k:")
        plt.grid()

        plt.xlabel("True values")
        plt.ylabel("Fit values")
        plt.title("True vs. fit values")

        plt.savefig("Fit_Plot.jpg")
        plt.show()

        
