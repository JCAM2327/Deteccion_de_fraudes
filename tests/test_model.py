"""Tests para el módulo de modelado (usando datos sintéticos)."""
import numpy as np
from sklearn.datasets import make_classification
from src.model import FraudDetectionModel

def test_model_initialization():
    model = FraudDetectionModel(model_type='xgboost')
    assert model.model_type == 'xgboost'
    assert model.model is None

def test_train_and_predict():
    """Entrenar en datos sintéticos y verificar que produce predicciones."""
    X, y = make_classification(n_samples=100, n_features=20, n_classes=2,
                                weights=[0.95, 0.05], random_state=42)
    model = FraudDetectionModel()
    model.train_xgboost_smote(X, y)
    # Verificar que el modelo existe
    assert model.model is not None
    # Predecir
    preds = model.predict(X[:5])
    assert len(preds) == 5
    assert set(preds).issubset({0,1})
    # Probabilidades
    probs = model.predict_proba(X[:5])
    assert probs.shape == (5,2)

def test_evaluate_returns_metrics():
    X, y = make_classification(n_samples=100, n_features=10, n_classes=2,
                                weights=[0.9, 0.1], random_state=42)
    model = FraudDetectionModel()
    model.train_xgboost_smote(X, y)
    metrics = model.evaluate(X, y, dataset_name='test')
    expected_keys = {'precision', 'recall', 'f1', 'f2', 'roc_auc', 'confusion_matrix', 'classification_report'}
    assert expected_keys.issubset(metrics.keys())