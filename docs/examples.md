---
layout: default
title: Ejemplos
---

# 💡 Ejemplos de Uso

Casos prácticos y ejemplos de código.

## Ejemplo 1: Pipeline Completo

```python
from src.preprocessing import DataProcessor
from src.model import FraudDetectionModel
from src.explainability import ExplainabilityAnalyzer

# Procesar datos
processor = DataProcessor(test_size=0.2, use_smote=True)
df = processor.load_and_merge_data(
    'data/raw/train_transaction.csv',
    'data/raw/train_identity.csv'
)

# Limpieza y preprocesamiento
df = processor.select_important_columns(df)
df = processor.handle_missing_values(df)
df = processor.feature_engineering(df)

# Preparar para modelado
X_train, X_test, y_train, y_test = processor.prepare_data(df)

# Entrenar modelo
model = FraudDetectionModel(model_type='xgboost')
model.train_xgboost_smote(X_train, y_train)

# Evaluar
metrics = model.evaluate(X_test, y_test)
print(f"Precision: {metrics['precision']:.4f}")
print(f"Recall: {metrics['recall']:.4f}")
print(f"ROC-AUC: {metrics['roc_auc']:.4f}")

# Explicabilidad
analyzer = ExplainabilityAnalyzer(model, X_train[:100], X_test)
analyzer.initialize_explainer()
shap_values = analyzer.compute_shap_values(X_test)
```

---

## Ejemplo 2: Comparar Múltiples Modelos

```python
from src.model import FraudDetectionModel

# XGBoost + SMOTE
model1 = FraudDetectionModel()
model1.train_xgboost_smote(X_train, y_train)
metrics1 = model1.evaluate(X_test, y_test)

# XGBoost + scale_pos_weight
model2 = FraudDetectionModel()
model2.train_xgboost_weighted(X_train, y_train)
metrics2 = model2.evaluate(X_test, y_test)

# Random Forest + SMOTE
model3 = FraudDetectionModel()
model3.train_random_forest(X_train, y_train)
metrics3 = model3.evaluate(X_test, y_test)

# Comparar
comparison = model1.compare_models({
    'XGBoost + SMOTE': metrics1,
    'XGBoost + Weight': metrics2,
    'Random Forest + SMOTE': metrics3
})
```

---

## Ejemplo 3: Feature Importance

```python
# Importancia del modelo
importance = model.get_feature_importance(top_n=10)
print(importance)

# Importancia SHAP
analyzer = ExplainabilityAnalyzer(model, X_train[:100], X_test)
analyzer.initialize_explainer()
shap_values = analyzer.compute_shap_values(X_test)

shap_importance = analyzer.get_feature_importance_ranking(top_n=10)
print(shap_importance)
```

---

## Ejemplo 4: Explicar una Predicción

```python
import numpy as np

# Encontrar una transacción fraudulenta
fraud_indices = np.where(y_test == 1)[0]

if len(fraud_indices) > 0:
    idx = fraud_indices[0]
    
    # Explicación
    explanation = analyzer.explain_prediction(idx, top_n=5)
    
    print(f"Predicción: {'FRAUDE' if explanation['prediction'] == 1 else 'LEGÍTIMO'}")
    print(f"Probabilidad: {explanation['fraud_probability']:.2%}")
    print("\nTop features:")
    
    for feature in explanation['top_features']:
        print(f"  {feature['feature']:20s} | SHAP: {feature['shap_value']:8.4f}")
```

---

## Ejemplo 5: Predicción en Tiempo Real

```python
import numpy as np

# Datos de una nueva transacción
transaction = np.array([
    [150.50, 12345, 5432, 100.0, 1, 50.0, ...]  # Features
])

# Predecir
prediction = model.predict(transaction)[0]
probability = model.predict_proba(transaction)[0, 1]

if probability > 0.7:
    print(f"⚠️ ALTO RIESGO DE FRAUDE ({probability:.2%})")
    print("Acción: BLOQUEAR TRANSACCIÓN")
elif probability > 0.4:
    print(f"⚠️ RIESGO MEDIO ({probability:.2%})")
    print("Acción: REVISAR MANUALMENTE")
else:
    print(f"✅ TRANSACCIÓN LEGÍTIMA ({(1-probability):.2%})")
    print("Acción: APROBAR")

# Explicación automática
explanation = analyzer.explain_prediction(0)
print(f"\nExplicación:")
for feature in explanation['top_features']:
    print(f"  {feature['feature']}: {feature['contribution']}")
```

---

## Ejemplo 6: Visualizar SHAP

```python
import matplotlib.pyplot as plt

# Summary plot (importancia global)
fig = analyzer.plot_summary(plot_type='bar', max_display=15)
plt.savefig('shap_summary.png', dpi=300, bbox_inches='tight')
plt.show()

# Dependence plot
fig = analyzer.plot_dependence('TransactionAmt')
plt.savefig('shap_dependence.png', dpi=300, bbox_inches='tight')
plt.show()

# Waterfall plot (explicación)
fig = analyzer.plot_waterfall(idx, max_display=10)
plt.savefig('shap_waterfall.png', dpi=300, bbox_inches='tight')
plt.show()
```

---

## Ejemplo 7: Usar Módulos por Separado

### Solo Preprocesamiento

```python
from src.preprocessing import DataProcessor

processor = DataProcessor()
df = processor.load_and_merge_data('data/raw/train_transaction.csv')
df = processor.select_important_columns(df)
df = processor.handle_missing_values(df)

# Guardar datos procesados
df.to_csv('data/processed/train_processed.csv', index=False)
```

### Solo Modelado (con datos pre-procesados)

```python
import pandas as pd
from src.model import FraudDetectionModel

# Cargar datos pre-procesados
df = pd.read_csv('data/processed/train_processed.csv')
X, y = df.drop('isFraud', axis=1), df['isFraud']

# Entrenar
model = FraudDetectionModel()
model.train_xgboost_smote(X_train, y_train)
model.save_model('models/fraud_model.pkl')
```

### Solo Explicabilidad (con modelo entrenado)

```python
from src.model import FraudDetectionModel
from src.explainability import ExplainabilityAnalyzer

# Cargar modelo
model = FraudDetectionModel()
model.load_model('models/fraud_model.pkl')

# Análisis
analyzer = ExplainabilityAnalyzer(model, X_train, X_test)
analyzer.initialize_explainer()
shap_values = analyzer.compute_shap_values(X_test)
```

---

## Ejemplo 8: Batch Prediction

```python
# Predicción en lote
predictions = model.predict(X_test)
probabilities = model.predict_proba(X_test)[:, 1]

# Crear reporte
import pandas as pd

report = pd.DataFrame({
    'Index': range(len(predictions)),
    'Prediction': predictions,
    'Fraud_Probability': probabilities,
    'Risk_Level': ['Alto' if p > 0.7 else 'Medio' if p > 0.4 else 'Bajo' 
                   for p in probabilities],
    'y_true': y_test
})

report.to_csv('predictions_report.csv', index=False)
print(f"Total predicciones: {len(report)}")
print(f"Fraudes detectados: {report['Prediction'].sum()}")
```

---

## Ejemplo 9: Validación Cruzada

```python
from sklearn.model_selection import cross_validate
from sklearn.metrics import make_scorer, precision_score, recall_score, f1_score

# Definir métricas
scoring = {
    'precision': make_scorer(precision_score),
    'recall': make_scorer(recall_score),
    'f1': make_scorer(f1_score)
}

# Validación cruzada
scores = cross_validate(model.model, X_train, y_train, 
                        cv=5, scoring=scoring)

print(f"Precision: {scores['test_precision'].mean():.4f} (+/- {scores['test_precision'].std():.4f})")
print(f"Recall: {scores['test_recall'].mean():.4f} (+/- {scores['test_recall'].std():.4f})")
print(f"F1: {scores['test_f1'].mean():.4f} (+/- {scores['test_f1'].std():.4f})")
```

---

## Ejemplo 10: Análisis de Errores

```python
from sklearn.metrics import confusion_matrix

# Obtener predicciones
y_pred = model.predict(X_test)

# Matriz de confusión
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()

print("=== Análisis de Errores ===")
print(f"Verdaderos Positivos (Fraudes detectados): {tp}")
print(f"Falsos Positivos (Legítimos bloqueados): {fp}")
print(f"Verdaderos Negativos (Legítimos aprobados): {tn}")
print(f"Falsos Negativos (Fraudes no detectados): {fn}")

print(f"\nTasa de falsos positivos: {fp/(fp+tn):.4f}")
print(f"Tasa de falsos negativos: {fn/(fn+tp):.4f}")
```

---

[← Volver a API](api-reference.md) | [Instalación →](installation.md)
