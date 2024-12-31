from model.model import SimpleModel
import numpy as np

def test_model_training():
    X = np.array([[1], [2], [3]])
    y = np.array([2, 4, 6])

    model = SimpleModel()
    model.train(X, y)
    predictions = model.predict(X)

    assert predictions[0] == y[0], "Test failed for first prediction!"

test_model_training()
