import pickle
import numpy as np
from model.model import SimpleModel  # Ensure this import is correct

def generate_data():
    """Generates synthetic training data."""
    try:
        x = np.random.rand(100, 1)  # 100 random values for x
        y = 3 * x + np.random.normal(0, 0.1, (100, 1))  # Linear relationship with noise for y
        return x.flatten(), y.flatten()  # Return as flattened arrays for simplicity
    except Exception as e:
        print(f"Error generating data: {e}")
        raise

def train_and_save_model():
    """Trains the model and saves it to a file."""
    try:
        x, y = generate_data()  # Get the synthetic training data
        model = SimpleModel()  # Create the model instance
        model.train(x, y)  # Train the model with the data

        # Save the trained model to disk using pickle
        with open('trained_model.pkl', 'wb') as model_file:
            pickle.dump(model, model_file)
        print("Model saved successfully to 'trained_model.pkl'")
    except Exception as e:
        print(f"Error in training and saving model: {e}")
        raise

if __name__ == "__main__":
    train_and_save_model()
