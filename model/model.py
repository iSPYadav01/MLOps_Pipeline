from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib

def train_model():
    data = load_iris()
    model = RandomForestClassifier(n_estimators=100)
    model.fit(data.data, data.target)

    joblib.dump(model, 'model/random_forest_model.pkl')
    return model
