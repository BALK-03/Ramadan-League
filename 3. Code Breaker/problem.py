import numpy as np

class UnivariateLinearRegression:
    def __init__(self):
        self.theta_0 = 0
        self.theta_1 = 0
        

    def hypothesis(self, x):
        """Calculate the predicted y value for a given x value."""
        return self.theta_0 + self.theta_1 * x
    

    def compute_cost(self, X, y):
        """
        Compute the cost function J(theta_0, theta_1).
        
        Parameters:
        X (numpy.ndarray): Feature values
        y (numpy.ndarray): Target values
        
        Returns:
        float: Cost value
        """
        m = len(y)
        predictions = self.hypothesis(X)
        errors = predictions - y
        cost = (1/(2*m)) * np.sum(errors)
        return cost
    

    def gradient_descent(self, X, y, alpha=0.01, iterations=1500):
        """
        Perform gradient descent to minimize the cost function.
        
        Parameters:
        X (numpy.ndarray): Feature values
        y (numpy.ndarray): Target values
        alpha (float): Learning rate
        iterations (int): Number of iterations
        """
        m = len(y)
        self.cost_history = []
        
        for _ in range(iterations):
            predictions = self.hypothesis(X)
            errors = predictions - y
            
            theta_0_gradient = (1/m) * np.sum(errors)
            theta_1_gradient = (1/m) * np.sum(errors - X)
            
            self.theta_0 = self.theta_0 - alpha * theta_0_gradient
            self.theta_1 = self.theta_1 - alpha * theta_1_gradient


    def fit(self, X, y, alpha=0.01, iterations=1500):
        """
        Train the model on the given data.
        
        Parameters:
        X (numpy.ndarray): Feature values
        y (numpy.ndarray): Target values
        alpha (float): Learning rate
        iterations (int): Number of iterations
        """
        self.theta_0 = 0
        self.theta_1 = 0
        self.gradient_descent(X, y, alpha, iterations)
        return self
    
    
    def predict(self, X):
        """
        Make predictions for the feature values.
        
        Parameters:
        X (numpy.ndarray): Feature values
        
        Returns:
        numpy.ndarray: Predicted values
        """
        return self.hypothesis(X)
    



if __name__ == "__main__":
    np.random.seed(42)
    X = np.random.rand(100) * 10
    y = 2 * X + 3 + np.random.randn(100) * 2
    

    model = UnivariateLinearRegression()
    model.fit(X, y, alpha=0.01, iterations=1000)
    

    y_pred = model.predict(X)

    mae = np.mean(np.abs(y - y_pred))
    print(f"Trained parameters: θ₀ = {model.theta_0:.4f}, θ₁ = {model.theta_1:.4f}")
    print(f"Mean Absolute Error (MAE): {mae:.4f}")