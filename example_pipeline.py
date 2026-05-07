"""
Script de ejemplo: Uso completo del pipeline de detección de fraudes

Este script muestra cómo usar todos los módulos del proyecto
en un flujo de trabajo completo.
"""

import sys
from pathlib import Path

# Agregar src al path
sys.path.insert(0, str(Path(__file__).parent))

from src.preprocessing import DataProcessor
from src.model import FraudDetectionModel
from src.explainability import ExplainabilityAnalyzer
import pandas as pd
import numpy as np

def main():
    """Pipeline completo de detección de fraudes."""
    
    print("=" * 70)
    print("🔍 DETECCIÓN DE FRAUDES - PIPELINE COMPLETO".center(70))
    print("=" * 70)
    
    # ==================== PASO 1: CARGAR Y PROCESAR DATOS ====================
    print("\n[1/5] 📥 Cargando y procesando datos...")
    print("-" * 70)
    
    processor = DataProcessor(
        test_size=0.2,
        random_state=42,
        use_smote=True
    )
    
    # Cargar datos (comentar que tengas los archivos)
    try:
        df = processor.load_and_merge_data(
            'data/raw/train_transaction.csv',
            'data/raw/train_identity.csv'
        )
    except FileNotFoundError:
        print("⚠️ Datos no encontrados. Usando datos de ejemplo...")
        # Generar datos de ejemplo si no existen
        np.random.seed(42)
        n_samples = 1000
        df = pd.DataFrame({
            'TransactionID': range(n_samples),
            'isFraud': np.random.binomial(1, 0.01, n_samples),
            'TransactionAmt': np.random.exponential(100, n_samples),
            'TransactionDT': np.random.randint(0, 100000, n_samples),
            'card1': np.random.randint(1000, 9999, n_samples),
            'card2': np.random.randint(100, 999, n_samples),
            'card3': np.random.randint(100, 999, n_samples),
            'ProductCD': np.random.choice(['W', 'H', 'S', 'R', 'C'], n_samples),
            'addr1': np.random.randint(1, 500, n_samples),
            'addr2': np.random.randint(1, 100, n_samples),
        })
    
    # Procesar
    df = processor.select_important_columns(df)
    df = processor.handle_missing_values(df)
    df = processor.feature_engineering(df)
    df = processor.encode_categorical(df, fit=True)
    
    # ==================== PASO 2: PREPARAR DATOS ====================
    print("\n[2/5] 📊 Preparando datos para modelado...")
    print("-" * 70)
    
    X_train, X_test, y_train, y_test = processor.prepare_data(df)
    
    # ==================== PASO 3: ENTRENAR MODELO ====================
    print("\n[3/5] 🤖 Entrenando modelo XGBoost...")
    print("-" * 70)
    
    model = FraudDetectionModel(model_type='xgboost', random_state=42)
    
    # Entrenar con SMOTE
    model.train_xgboost_smote(X_train, y_train)
    
    # ==================== PASO 4: EVALUAR MODELO ====================
    print("\n[4/5] 📈 Evaluando rendimiento del modelo...")
    print("-" * 70)
    
    metrics = model.evaluate(X_test, y_test, dataset_name="Test Set")
    
    # ==================== PASO 5: EXPLICABILIDAD ====================
    print("\n[5/5] 🔍 Generando explicabilidad con SHAP...")
    print("-" * 70)
    
    try:
        # Usar un subconjunto para SHAP (más rápido)
        X_background = X_train[:100]
        X_explain = X_test[:50]
        
        analyzer = ExplainabilityAnalyzer(
            model=model,
            X_background=X_background,
            X_explain=X_explain
        )
        
        # Inicializar explainer
        analyzer.initialize_explainer(model_type='tree')
        
        # Calcular SHAP values (puede tomar tiempo)
        print("⏳ Esto puede tomar unos minutos...")
        shap_values = analyzer.compute_shap_values(X_explain)
        
        # Feature importance
        importance_df = analyzer.get_feature_importance_ranking(top_n=10)
        print("\n📊 Top 10 Características Más Importantes (SHAP):")
        print(importance_df.to_string(index=False))
        
        # Explicar una predicción
        idx_fraudulento = np.where(y_test[:50] == 1)[0]
        if len(idx_fraudulento) > 0:
            idx = idx_fraudulento[0]
            print(f"\n🔍 Explicación de una transacción fraudulenta (índice {idx}):")
            explanation = analyzer.explain_prediction(idx, top_n=5)
            
            print(f"\nPredicción: {'🚨 FRAUDE' if explanation['prediction'] == 1 else '✅ LEGÍTIMO'}")
            print(f"Probabilidad de Fraude: {explanation['fraud_probability']:.2%}")
            print(f"\nTop 5 características contribuyentes:")
            for i, feat in enumerate(explanation['top_features'], 1):
                print(f"  {i}. {feat['feature']:20s} | SHAP: {feat['shap_value']:8.4f} | {feat['contribution']}")
        
    except Exception as e:
        print(f"⚠️ No se pudo calcular SHAP: {e}")
        print("(Esto es normal en algunos entornos)")
    
    # ==================== RESUMEN FINAL ====================
    print("\n" + "=" * 70)
    print("✅ PIPELINE COMPLETADO EXITOSAMENTE".center(70))
    print("=" * 70)
    
    print(f"\n📊 Resumen de Resultados:")
    print(f"   • Modelo: XGBoost + SMOTE")
    print(f"   • Precision en Test: {metrics.get('precision', 0):.4f}")
    print(f"   • Recall en Test: {metrics.get('recall', 0):.4f}")
    print(f"   • F1-Score en Test: {metrics.get('f1', 0):.4f}")
    print(f"   • ROC-AUC en Test: {metrics.get('roc_auc', 0):.4f}")
    
    print(f"\n💾 Archivos generados:")
    print(f"   • Modelo entrenado: models/fraud_model.pkl (sin guardar en este ejemplo)")
    print(f"   • Scaler de features: models/scaler.pkl (sin guardar en este ejemplo)")
    
    print(f"\n🚀 Próximos pasos:")
    print(f"   1. Ejecutar el Dashboard: streamlit run dashboard/app.py")
    print(f"   2. Revisar los Notebooks: jupyter notebook notebooks/")
    print(f"   3. Desplegar en producción con FastAPI o serverless")
    
    print("\n" + "=" * 70 + "\n")


if __name__ == "__main__":
    main()
