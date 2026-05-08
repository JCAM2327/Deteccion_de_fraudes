---
layout: default
title: Referencia de API
---

# 🔌 Referencia de API

Documentación completa de los módulos del proyecto.

## DataProcessor

Clase para cargar, limpiar y preparar datos.

### Métodos

#### `__init__(test_size=0.2, random_state=42, use_smote=True)`
Inicializa el procesador.

```python
processor = DataProcessor(test_size=0.2, use_smote=True)
```

#### `load_and_merge_data(trans_path, id_path=None)`
Cargar y fusionar datos de transacciones e identidad.

```python
df = processor.load_and_merge_data(
    'data/raw/train_transaction.csv',
    'data/raw/train_identity.csv'
)
```

#### `select_important_columns(df)`
Seleccionar columnas relevantes.

```python
df_subset = processor.select_important_columns(df)
```

#### `handle_missing_values(df)`
Manejar valores faltantes.

```python
df_clean = processor.handle_missing_values(df)
```

#### `feature_engineering(df)`
Crear nuevas características.

```python
df_fe = processor.feature_engineering(df)
```

#### `encode_categorical(df, fit=True)`
Codificar variables categóricas.

```python
df_encoded = processor.encode_categorical(df, fit=True)
```

#### `prepare_data(df)`
Pipeline completo de preparación.

```python
X_train, X_test, y_train, y_test = processor.prepare_data(df)
```

---

## FraudDetectionModel

Clase para entrenar y evaluar modelos.

### Métodos

#### `__init__(model_type='xgboost', random_state=42)`
Inicializa el modelo.

```python
model = FraudDetectionModel(model_type='xgboost')
```

#### `train_xgboost_smote(X_train, y_train)`
Entrenar XGBoost con SMOTE.

```python
model.train_xgboost_smote(X_train, y_train)
```

#### `train_xgboost_weighted(X_train, y_train)`
Entrenar XGBoost con scale_pos_weight.

```python
model.train_xgboost_weighted(X_train, y_train)
```

#### `train_random_forest(X_train, y_train)`
Entrenar Random Forest con SMOTE.

```python
model.train_random_forest(X_train, y_train)
```

#### `predict(X)`
Realizar predicciones.

```python
predictions = model.predict(X_test)
```

#### `predict_proba(X)`
Obtener probabilidades.

```python
proba = model.predict_proba(X_test)[:, 1]  # Probabilidad de fraude
```

#### `evaluate(X_test, y_test, dataset_name='Test')`
Evaluar el modelo.

```python
metrics = model.evaluate(X_test, y_test)
print(f"Precision: {metrics['precision']:.4f}")
```

**Retorna:**
```python
{
    'precision': float,
    'recall': float,
    'f1': float,
    'f2': float,
    'roc_auc': float,
    'confusion_matrix': ndarray,
    'classification_report': dict
}
```

#### `get_feature_importance(feature_names=None, top_n=20)`
Obtener importancia de características.

```python
importance = model.get_feature_importance(top_n=10)
```

#### `save_model(path)` / `load_model(path)`
Guardar y cargar modelos.

```python
model.save_model('models/fraud_model.pkl')
model.load_model('models/fraud_model.pkl')
```

---

## ExplainabilityAnalyzer

> **Nota importante:** Esta clase acepta directamente una instancia de `FraudDetectionModel` (no es necesario pasar `model.model`). Internamente extrae el modelo XGBoost automáticamente.

Clase para explicabilidad con SHAP.

### Métodos

#### `__init__(model, X_background=None, X_explain=None)`
Inicializa el analizador.

- `model`: Puede ser una instancia de `FraudDetectionModel` o un modelo XGBoost entrenado directamente.
- `X_background`: Datos de fondo para SHAP (normalmente una muestra de `X_train`).
- `X_explain`: Datos a explicar (normalmente `X_test` o una muestra).

#### `initialize_explainer(model_type='tree')`
Inicializar SHAP explainer.

```python
analyzer.initialize_explainer(model_type='tree')
```

#### `compute_shap_values(X)`
Calcular SHAP values.

```python
shap_values = analyzer.compute_shap_values(X_test)
```

#### `plot_summary(feature_names=None, plot_type='bar', max_display=15)`
Crear SHAP summary plot.

```python
fig = analyzer.plot_summary(plot_type='bar')
plt.show()
```

#### `plot_dependence(feature_idx, feature_names=None)`
Crear dependence plot.

```python
fig = analyzer.plot_dependence('TransactionAmt')
plt.show()
```

#### `plot_waterfall(instance_idx, feature_names=None, max_display=10)`
Crear waterfall plot.

```python
fig = analyzer.plot_waterfall(0)
plt.show()
```

#### `get_feature_importance_ranking(feature_names=None, top_n=20)`
Ranking de importancia SHAP.

```python
importance = analyzer.get_feature_importance_ranking(top_n=10)
```

#### `explain_prediction(instance_idx, feature_names=None, top_n=10)`
Explicación detallada.

```python
explanation = analyzer.explain_prediction(0, top_n=5)
print(f"Fraude: {explanation['fraud_probability']:.2%}")
```

**Retorna:**
```python
{
    'prediction': int,  # 0 o 1
    'fraud_probability': float,
    'legitimate_probability': float,
    'top_features': [...]  # Lista de características
}
```

---

## Flujo de Trabajo Completo

```python
from src.preprocessing import DataProcessor
from src.model import FraudDetectionModel
from src.explainability import ExplainabilityAnalyzer

# 1. Procesar
processor = DataProcessor()
df = processor.load_and_merge_data('data/raw/train_transaction.csv')
df = processor.select_important_columns(df)
df = processor.handle_missing_values(df)
df = processor.feature_engineering(df)
X_train, X_test, y_train, y_test = processor.prepare_data(df)

# 2. Entrenar
model = FraudDetectionModel(model_type='xgboost')
model.train_xgboost_smote(X_train, y_train)

# 3. Evaluar
metrics = model.evaluate(X_test, y_test)

# 4. Explicar (model se pasa directamente)
analyzer = ExplainabilityAnalyzer(model, X_train[:100], X_test)
analyzer.initialize_explainer()
shap_values = analyzer.compute_shap_values(X_test)
importance = analyzer.get_feature_importance_ranking(top_n=10)
explanation = analyzer.explain_prediction(0, top_n=5)
```

---

## Tipos de Datos

### DataProcessor
- **Input**: CSVs de transacciones e identidad
- **Output**: DataFrames procesados y escalados

### FraudDetectionModel
- **Input**: Arrays NumPy (train/test)
- **Output**: Predicciones, probabilidades, métricas

### ExplainabilityAnalyzer
- **Input**: Modelo entrenado, datos
- **Output**: SHAP values, plots, explicaciones

---

## Manejo de Errores

Todos los métodos capturan excepciones comunes:

```python
try:
    analyzer.initialize_explainer()
except Exception as e:
    print(f"Error: {e}")
```

---

## Parámetros Comunes

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|------------|
| `test_size` | float | 0.2 | Proporción test |
| `random_state` | int | 42 | Semilla |
| `use_smote` | bool | True | Usar SMOTE |
| `model_type` | str | 'xgboost' | Tipo de modelo |
| `top_n` | int | 20 | Features a mostrar |
| `max_display` | int | 15 | Máximo a visualizar |

---

[← Volver a Features](features.md) | [Ejemplos →](examples.md)
