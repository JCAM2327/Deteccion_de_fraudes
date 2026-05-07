"""
Módulo de modelado para detección de fraudes.

Incluye entrenamiento, evaluación e inferencia de modelos.
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report, confusion_matrix, roc_auc_score,
    precision_recall_fscore_support, roc_curve, auc
)
from xgboost import XGBClassifier
import joblib
from pathlib import Path


class FraudDetectionModel:
    """
    Clase para entrenar y evaluar modelos de detección de fraudes.
    
    Soporta múltiples modelos:
    - XGBoost con SMOTE
    - XGBoost con scale_pos_weight
    - Random Forest con SMOTE
    """
    
    def __init__(self, model_type='xgboost', random_state=42):
        """
        Inicializar el modelo.
        
        Args:
            model_type: Tipo de modelo ('xgboost', 'random_forest')
            random_state: Semilla para reproducibilidad
        """
        self.model_type = model_type
        self.random_state = random_state
        self.model = None
        self.results = {}
        
    def train_xgboost_smote(self, X_train, y_train):
        """
        Entrenar XGBoost con datos balanceados por SMOTE.
        
        Args:
            X_train: Features de entrenamiento (ya balanceadas con SMOTE)
            y_train: Target de entrenamiento
            
        Returns:
            Modelo entrenado
        """
        print("\n🤖 Entrenando XGBoost + SMOTE...")
        
        self.model = XGBClassifier(
            n_estimators=100,
            max_depth=6,
            learning_rate=0.1,
            random_state=self.random_state,
            use_label_encoder=False,
            eval_metric='logloss',
            n_jobs=-1,
            verbosity=0
        )
        
        self.model.fit(X_train, y_train)
        print("   ✅ Modelo entrenado exitosamente")
        
        return self.model
    
    def train_xgboost_weighted(self, X_train, y_train):
        """
        Entrenar XGBoost con scale_pos_weight.
        
        Args:
            X_train: Features de entrenamiento (no balanceadas)
            y_train: Target de entrenamiento
            
        Returns:
            Modelo entrenado
        """
        print("\n🤖 Entrenando XGBoost + scale_pos_weight...")
        
        # Calcular peso de la clase positiva
        scale = (y_train == 0).sum() / (y_train == 1).sum()
        print(f"   scale_pos_weight = {scale:.2f}")
        
        self.model = XGBClassifier(
            scale_pos_weight=scale,
            n_estimators=100,
            max_depth=6,
            learning_rate=0.1,
            random_state=self.random_state,
            use_label_encoder=False,
            eval_metric='logloss',
            n_jobs=-1,
            verbosity=0
        )
        
        self.model.fit(X_train, y_train)
        print("   ✅ Modelo entrenado exitosamente")
        
        return self.model
    
    def train_random_forest(self, X_train, y_train):
        """
        Entrenar Random Forest con datos balanceados.
        
        Args:
            X_train: Features de entrenamiento (ya balanceadas con SMOTE)
            y_train: Target de entrenamiento
            
        Returns:
            Modelo entrenado
        """
        print("\n🤖 Entrenando Random Forest + SMOTE...")
        
        self.model = RandomForestClassifier(
            n_estimators=100,
            max_depth=15,
            random_state=self.random_state,
            n_jobs=-1,
            verbose=0
        )
        
        self.model.fit(X_train, y_train)
        print("   ✅ Modelo entrenado exitosamente")
        
        return self.model
    
    def predict(self, X):
        """Realizar predicciones."""
        if self.model is None:
            raise ValueError("El modelo no ha sido entrenado aún")
        return self.model.predict(X)
    
    def predict_proba(self, X):
        """Obtener probabilidades de predicción."""
        if self.model is None:
            raise ValueError("El modelo no ha sido entrenado aún")
        return self.model.predict_proba(X)
    
    def evaluate(self, X_test, y_test, dataset_name='Test'):
        """
        Evaluar el modelo en un dataset.
        
        Args:
            X_test: Features de prueba
            y_test: Target de prueba
            dataset_name: Nombre del dataset para reportes
            
        Returns:
            Diccionario con métricas
        """
        print(f"\n📊 Evaluación en {dataset_name}:")
        
        y_pred = self.predict(X_test)
        y_proba = self.predict_proba(X_test)[:, 1]
        
        # Métricas binarias
        precision, recall, f1, _ = precision_recall_fscore_support(
            y_test, y_pred, average='binary'
        )
        
        # F2-score (da más peso a recall)
        beta = 2
        f2 = ((1 + beta**2) * (precision * recall) /
              ((beta**2 * precision) + recall))
        
        # ROC-AUC
        roc_auc = roc_auc_score(y_test, y_proba)
        
        # Matriz de confusión
        cm = confusion_matrix(y_test, y_pred)
        
        # Reporte detallado
        report_dict = classification_report(
            y_test, y_pred,
            target_names=['Legítimo', 'Fraude'],
            output_dict=True
        )
        
        metrics = {
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'f2': f2,
            'roc_auc': roc_auc,
            'confusion_matrix': cm,
            'classification_report': report_dict,
            'predictions': y_pred,
            'probabilities': y_proba
        }
        
        self.results[dataset_name] = metrics
        
        # Imprimir resumen
        print(f"   Precision: {precision:.4f}")
        print(f"   Recall: {recall:.4f}")
        print(f"   F1-Score: {f1:.4f}")
        print(f"   F2-Score: {f2:.4f}")
        print(f"   ROC-AUC: {roc_auc:.4f}")
        print("\n" + classification_report(
            y_test, y_pred,
            target_names=['Legítimo', 'Fraude']
        ))
        
        return metrics
    
    def get_feature_importance(self, feature_names=None, top_n=20):
        """
        Obtener importancia de características.
        
        Args:
            feature_names: Lista de nombres de características
            top_n: Número de características que mostrar
            
        Returns:
            DataFrame con importancia ordenada
        """
        if self.model is None:
            raise ValueError("El modelo no ha sido entrenado aún")
        
        if not hasattr(self.model, 'feature_importances_'):
            raise AttributeError(
                f"El modelo {type(self.model).__name__} no tiene feature_importances_"
            )
        
        importances = self.model.feature_importances_
        
        if feature_names is None:
            feature_names = [f"Feature_{i}" for i in range(len(importances))]
        
        importance_df = pd.DataFrame({
            'Feature': feature_names,
            'Importance': importances
        }).sort_values('Importance', ascending=False).head(top_n)
        
        return importance_df
    
    def compare_models(self, results_dict):
        """
        Comparar múltiples modelos.
        
        Args:
            results_dict: Diccionario con resultados de múltiples modelos
            
        Returns:
            DataFrame comparativo
        """
        comparison = []
        
        for model_name, metrics in results_dict.items():
            comparison.append({
                'Model': model_name,
                'Precision': metrics.get('precision', np.nan),
                'Recall': metrics.get('recall', np.nan),
                'F1-Score': metrics.get('f1', np.nan),
                'F2-Score': metrics.get('f2', np.nan),
                'ROC-AUC': metrics.get('roc_auc', np.nan)
            })
        
        comparison_df = pd.DataFrame(comparison)
        
        print("\n📈 Comparación de modelos:")
        print(comparison_df.to_string(index=False))
        
        return comparison_df
    
    def save_model(self, path):
        """Guardar modelo entrenado."""
        if self.model is None:
            raise ValueError("No hay modelo entrenado para guardar")
        
        joblib.dump(self.model, path)
        print(f"✅ Modelo guardado en {path}")
    
    def load_model(self, path):
        """Cargar modelo entrenado."""
        self.model = joblib.load(path)
        print(f"✅ Modelo cargado desde {path}")
