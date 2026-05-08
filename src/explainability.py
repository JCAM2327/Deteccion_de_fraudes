"""
Módulo de explicabilidad con SHAP y otras técnicas.

Proporciona explicaciones interpretables de predicciones del modelo.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shap
from pathlib import Path


class ExplainabilityAnalyzer:
    """
    Clase para analizar y explicar predicciones con SHAP.
    
    Genera visualizaciones e interpretaciones para:
    - Importancia global de características (SHAP summary plot)
    - Explicaciones locales por muestra (SHAP force plot)
    - Dependencias entre características (SHAP dependence plot)
    """
    
    def __init__(self, model, X_background, X_explain):
    """
    Args:
        model: Puede ser un XGBClassifier entrenado O una instancia de FraudDetectionModel
        X_background: Datos de fondo para SHAP (normalmente una muestra de X_train)
        X_explain: Datos a explicar (normalmente X_test o X_sample)
    """
    # Si es un FraudDetectionModel, extraer el modelo interno
    if hasattr(model, 'model') and hasattr(model.model, 'get_booster'):
        self.model = model.model
    else:
        self.model = model
    
    self.X_background = X_background
    self.X_explain = X_explain
    self.explainer = None
        
    def initialize_explainer(self, model_type='tree'):
        """
        Inicializar el explainer de SHAP.
        
        Args:
            model_type: 'tree' para tree-based models, 'kernel' para otros
        """
        print("🔍 Inicializando SHAP explainer...")
        
        if model_type == 'tree':
            try:
                self.explainer = shap.TreeExplainer(self.model)
                print("   ✅ TreeExplainer inicializado")
            except Exception as e:
                print(f"   ⚠️ No se pudo usar TreeExplainer: {e}")
                print("   Usando KernelExplainer como alternativa...")
                self.explainer = shap.KernelExplainer(
                    self.model.predict, self.X_background
                )
        else:
            self.explainer = shap.KernelExplainer(
                self.model.predict, self.X_background
            )
            print("   ✅ KernelExplainer inicializado")
    
    def compute_shap_values(self, X):
        """
        Calcular SHAP values para un dataset.
        
        Args:
            X: Datos para los que calcular SHAP values
            
        Returns:
            SHAP values
        """
        if self.explainer is None:
            self.initialize_explainer()
        
        print("⏳ Calculando SHAP values (esto puede tomar tiempo)...")
        self.shap_values = self.explainer.shap_values(X)
        print("   ✅ SHAP values calculados")
        
        # Para clasificación binaria, tomar solo la clase positiva
        if isinstance(self.shap_values, list):
            self.shap_values = self.shap_values[1]
        
        return self.shap_values
    
    def plot_summary(self, feature_names=None, plot_type='bar', max_display=15):
        """
        Crear SHAP summary plot (importancia global).
        
        Args:
            feature_names: Nombres de características
            plot_type: 'bar' o 'violin'
            max_display: Número máximo de características a mostrar
            
        Returns:
            Figura matplotlib
        """
        if self.shap_values is None:
            raise ValueError("Primero calcular SHAP values con compute_shap_values")
        
        print(f"📊 Creando SHAP summary plot ({plot_type})...")
        
        fig = plt.figure(figsize=(12, 6))
        
        shap.summary_plot(
            self.shap_values,
            self.X_explain,
            plot_type=plot_type,
            feature_names=feature_names,
            show=False,
            max_display=max_display
        )
        
        plt.tight_layout()
        return fig
    
    def plot_dependence(self, feature_idx, feature_names=None):
        """
        Crear SHAP dependence plot para una característica.
        
        Args:
            feature_idx: Índice o nombre de la característica
            feature_names: Nombres de características
            
        Returns:
            Figura matplotlib
        """
        if self.shap_values is None:
            raise ValueError("Primero calcular SHAP values con compute_shap_values")
        
        fig = plt.figure(figsize=(10, 6))
        
        shap.dependence_plot(
            feature_idx,
            self.shap_values,
            self.X_explain,
            feature_names=feature_names,
            show=False
        )
        
        plt.tight_layout()
        return fig
    
    def plot_waterfall(self, instance_idx, feature_names=None, max_display=10):
        """
        Crear SHAP waterfall plot para una instancia específica.
        
        Args:
            instance_idx: Índice de la muestra a explicar
            feature_names: Nombres de características
            max_display: Número máximo de características a mostrar
            
        Returns:
            Figura matplotlib
        """
        if self.shap_values is None:
            raise ValueError("Primero calcular SHAP values con compute_shap_values")
        
        fig = plt.figure(figsize=(12, 6))
        
        explanation = shap.Explanation(
            values=self.shap_values[instance_idx],
            base_values=self.explainer.expected_value,
            data=self.X_explain[instance_idx],
            feature_names=feature_names
        )
        
        shap.plots.waterfall(explanation, show=False, max_display=max_display)
        
        plt.tight_layout()
        return fig
    
    def get_feature_importance_ranking(self, feature_names=None, top_n=20):
        """
        Obtener ranking de características por importancia SHAP.
        
        Args:
            feature_names: Nombres de características
            top_n: Número de características que mostrar
            
        Returns:
            DataFrame con importancia ordenada
        """
        if self.shap_values is None:
            raise ValueError("Primero calcular SHAP values con compute_shap_values")
        
        # Importancia = valor absoluto medio de SHAP para cada característica
        importance = np.abs(self.shap_values).mean(axis=0)
        
        if feature_names is None:
            feature_names = [f"Feature_{i}" for i in range(len(importance))]
        
        importance_df = pd.DataFrame({
            'Feature': feature_names,
            'SHAP_Importance': importance
        }).sort_values('SHAP_Importance', ascending=False).head(top_n)
        
        return importance_df
    
    def explain_prediction(self, instance_idx, feature_names=None, top_n=10):
        """
        Explicación detallada de una predicción.
        
        Args:
            instance_idx: Índice de la muestra
            feature_names: Nombres de características
            top_n: Número de características más importantes
            
        Returns:
            Diccionario con explicación
        """
        if self.shap_values is None:
            raise ValueError("Primero calcular SHAP values con compute_shap_values")
        
        # Obtener predicción
        prediction = self.model.predict(self.X_explain[instance_idx:instance_idx+1])[0]
        proba = self.model.predict_proba(self.X_explain[instance_idx:instance_idx+1])[0]
        
        # SHAP values para esta instancia
        shap_vals = self.shap_values[instance_idx]
        
        if feature_names is None:
            feature_names = [f"Feature_{i}" for i in range(len(shap_vals))]
        
        # Top features que contribuyen a la predicción
        top_indices = np.argsort(np.abs(shap_vals))[-top_n:][::-1]
        
        explanation = {
            'prediction': prediction,
            'fraud_probability': proba[1],
            'legitimate_probability': proba[0],
            'top_features': [
                {
                    'feature': feature_names[idx],
                    'value': self.X_explain[instance_idx, idx],
                    'shap_value': shap_vals[idx],
                    'contribution': 'aumenta riesgo' if shap_vals[idx] > 0 else 'disminuye riesgo'
                }
                for idx in top_indices
            ]
        }
        
        return explanation
    
    def save_plots(self, save_dir, feature_names=None):
        """
        Guardar todos los plots de SHAP.
        
        Args:
            save_dir: Directorio donde guardar los plots
            feature_names: Nombres de características
        """
        save_dir = Path(save_dir)
        save_dir.mkdir(parents=True, exist_ok=True)
        
        print(f"💾 Guardando plots en {save_dir}...")
        
        # Summary plot
        fig = self.plot_summary(feature_names=feature_names, plot_type='bar')
        fig.savefig(save_dir / 'shap_summary_bar.png', dpi=300, bbox_inches='tight')
        plt.close(fig)
        
        fig = self.plot_summary(feature_names=feature_names, plot_type='violin')
        fig.savefig(save_dir / 'shap_summary_violin.png', dpi=300, bbox_inches='tight')
        plt.close(fig)
        
        print("   ✅ Plots guardados")
