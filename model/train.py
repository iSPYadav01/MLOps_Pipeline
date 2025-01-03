import sys
import os
import pickle
import numpy as np

# Ensure the 'model' directory is part of the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))

from model import SimpleModel  # Import SimpleModel from 'model'

def generate_data():
    """Generates synthetic training data."""
    x = np.random.rand(100, 1)
    y = 3 * x + np.random.normal(0, 0.1, (100, 1))
    return x.flatten(), y.flatten()

def train_and_save_model():
    """Trains the model and saves it to a file."""
    x, y = generate_data()
    model = SimpleModel()
    model.train(x, y)

    # Save the trained model to disk
    with open('trained_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)

if __name__ == "__main__":
    train_and_save_model()
