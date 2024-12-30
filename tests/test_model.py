import pytest
from sklearn.datasets import load_iris
from model import train_model
import joblib

def test_model_training():
    model = train_model()
    assert model is not None
    # Load model and check if it's a RandomForestClassifier
    model = joblib.load("model/random_forest_model.pkl")
    assert isinstance(model, RandomForestClassifier)
