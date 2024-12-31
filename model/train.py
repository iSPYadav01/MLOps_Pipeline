from model.model import SimpleModel
import numpy as np

def main():
    # Generate dummy data
    X = np.array([[1], [2], [3], [4], [5]])
    y = np.array([2, 4, 6, 8, 10])

    # Train and predict
    model = SimpleModel()
    model.train(X, y)
    predictions = model.predict(X)

    print("Predictions:", predictions)

if __name__ == "__main__":
    main()
