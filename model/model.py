class SimpleModel:
    """A simple linear regression model."""

    def __init__(self):
        """Initialize the model with weights and bias."""
        self.weights = None
        self.bias = None

    def train(self, x, y):
        """Train the model using a simple linear regression formula."""
        # Calculating weights (slope) and bias (intercept) using the least squares method
        n = len(x)
        x_mean = x.mean()
        y_mean = y.mean()

        numerator = sum((x - x_mean) * (y - y_mean))
        denominator = sum((x - x_mean) ** 2)
        self.weights = numerator / denominator
        self.bias = y_mean - (self.weights * x_mean)

    def predict(self, x):
        """Predict the output for the given input data."""
        if self.weights is None or self.bias is None:
            raise ValueError("Model is not trained yet.")
        return self.weights * x + self.bias
