#!/usr/bin/env python
"""
Entrenamiento completo del modelo de detección de fraudes.
Uso: python scripts/train.py
"""

import sys
import json
from pathlib import Path

# Añadir raíz del proyecto al path
sys.path.append(str(Path(__file__).parent.parent))

import joblib
from src.preprocessing import DataProcessor
from src.model import FraudDetectionModel

def main():
    print("=" * 60)
    print("🚀 Entrenamiento del modelo de detección de fraudes")
    print("=" * 60)

    # Rutas
    DATA_RAW = Path("data/raw")
    MODELS_DIR = Path("models")
    MODELS_DIR.mkdir(exist_ok=True)

    trans_path = DATA_RAW / "train_transaction.csv"
    id_path = DATA_RAW / "train_identity.csv"

    if not trans_path.exists():
        print(f"❌ No se encuentra {trans_path}")
        print("Ejecuta primero: python scripts/descargar.py")
        return

   # 1. Cargar y procesar datos (dataset completo)
    print("\n📊 Cargando y procesando datos...")
    processor = DataProcessor(test_size=0.2, random_state=42, use_smote=True)

    df = processor.load_and_merge_data(str(trans_path), str(id_path))

    # 🔻 NUEVA LÍNEA: Reducir para que quepa en memoria
    print("Reduciendo a 30% de los datos por limitaciones de memoria...")
    df = df.sample(frac=0.2, random_state=42).reset_index(drop=True)

    df = processor.select_important_columns(df)
    df = processor.handle_missing_values(df)
    df = processor.feature_engineering(df)
    df = processor.encode_categorical(df, fit=True)

    # 2. Preparar datos (SMOTE y escalado)
    X_train, X_test, y_train, y_test = processor.prepare_data(df)

    # 3. Entrenar modelo XGBoost + SMOTE
    print("\n🤖 Entrenando XGBoost + SMOTE...")
    model = FraudDetectionModel()
    model.train_xgboost_smote(X_train, y_train)

    # 4. Evaluar
    print("\n📈 Evaluando modelo...")
    metrics = model.evaluate(X_test, y_test, dataset_name='test_completo')

    print(f"\n🏆 Resultados en test (dataset completo):")
    print(f"   Precision: {metrics['precision']:.4f}")
    print(f"   Recall:    {metrics['recall']:.4f}")
    print(f"   F1-score:  {metrics['f1']:.4f}")
    print(f"   ROC-AUC:   {metrics['roc_auc']:.4f}")

    # 5. Guardar artefactos
    print("\n💾 Guardando modelo y artefactos...")
    model.save_model(str(MODELS_DIR / "fraud_model.pkl"))
    processor.save_scaler(str(MODELS_DIR / "scaler.pkl"))
    joblib.dump(processor.label_encoders, MODELS_DIR / "label_encoders.pkl")

    with open(MODELS_DIR / "metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)

    print("\n✅ Entrenamiento completado. Archivos guardados en 'models/':")
    for f in MODELS_DIR.glob("*"):
        print(f"   - {f.name}")

    print("\n🔍 Próximo paso: conectar el dashboard real (opción C).")

if __name__ == "__main__":
    main()