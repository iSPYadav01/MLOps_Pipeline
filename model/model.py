class SimpleModel:
    """
    A simple linear model with a weight and bias.
    """
    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias

    def predict(self, input_data):
        """
        Predict output using a simple linear equation.
        :param input_data: Input value
        :return: Predicted output
        """
        return self.weight * input_data + self.bias
