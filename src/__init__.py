"""
Módulo de Detección de Fraudes

Utilidades para preprocesamiento, modelado y explicabilidad
de un sistema de detección de fraudes en transacciones.
"""

from .preprocessing import DataProcessor
from .model import FraudDetectionModel
from .explainability import ExplainabilityAnalyzer

__version__ = "1.0.0"
__all__ = ["DataProcessor", "FraudDetectionModel", "ExplainabilityAnalyzer"]
