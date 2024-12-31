from model.model import SimpleModel

def train():
    """
    Train a simple model using hardcoded data.
    """
    weight, bias = 2, 0.5  # Hardcoded model parameters
    model = SimpleModel(weight, bias)

    print("Training the model with sample data...")
    for data in range(1, 11):  # Fake training loop
        prediction = model.predict(data)
        print(f"Input: {data}, Prediction: {prediction}")

if __name__ == "__main__":
    train()