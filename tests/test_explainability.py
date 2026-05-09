"""Tests para el módulo de explicabilidad (usando un modelo simple)."""
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from src.explainability import ExplainabilityAnalyzer

def test_analyzer_initialization():
    # Crear modelo ficticio
    X = np.random.rand(100, 5)
    y = np.random.randint(0,2,100)
    model = RandomForestClassifier(n_estimators=2, random_state=42)
    model.fit(X, y)
    # Inicializar analyzer
    analyzer = ExplainabilityAnalyzer(model, X[:50], X[50:])
    assert analyzer.model is model
    assert analyzer.X_background.shape == (50,5)
    assert analyzer.X_explain.shape == (50,5)
    assert analyzer.explainer is None

def test_explainer_initialization():
    X = np.random.rand(50, 4)
    y = np.random.randint(0,2,50)
    model = RandomForestClassifier(n_estimators=2, random_state=42)
    model.fit(X, y)
    analyzer = ExplainabilityAnalyzer(model, X[:30], X[30:])
    analyzer.initialize_explainer(model_type='tree')
    # Como RandomForest es árbol, debería inicializar TreeExplainer
    assert analyzer.explainer is not None