import pytest
from model.model import SimpleModel


@pytest.fixture
def sample_data():
    """Fixture providing sample training data."""
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    return x, y


def test_model_training(sample_data):
    """Test the model's training method."""
    model = SimpleModel()
    x, y = sample_data
    model.train(x, y)

    assert model.weights == pytest.approx(2, rel=1e-2)
    assert model.bias == pytest.approx(0, rel=1e-2)


def test_model_prediction(sample_data):
    """Test the model's prediction method."""
    model = SimpleModel()
    x, y = sample_data
    model.train(x, y)

    predictions = model.predict([6, 7])
    assert predictions == pytest.approx([12, 14], rel=1e-2)
