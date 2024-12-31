import pytest
from model.model import SimpleModel


@pytest.fixture
def model():
    """
    Fixture to initialize the SimpleModel for testing.
    """
    return SimpleModel(weight=3, bias=1)


def test_predict_positive(model):
    """
    Test prediction for positive input.
    """
    input_data = 4
    expected_output = 13  # 3 * 4 + 1
    assert model.predict(input_data) == expected_output


def test_predict_zero(model):
    """
    Test prediction for zero input.
    """
    input_data = 0
    expected_output = 1  # 3 * 0 + 1
    assert model.predict(input_data) == expected_output


def test_predict_negative(model):
    """
    Test prediction for negative input.
    """
    input_data = -2
    expected_output = -5  # 3 * -2 + 1
    assert model.predict(input_data) == expected_output
