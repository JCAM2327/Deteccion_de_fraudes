# Documentación de API - Módulos del Proyecto

## 📚 Índice
1. [DataProcessor](#dataprocessor)
2. [FraudDetectionModel](#frauddetectionmodel)
3. [ExplainabilityAnalyzer](#explainabilityanalyzer)

---

## DataProcessor

Clase para cargar, limpiar y preparar datos para modelado.

### `__init__(test_size=0.2, random_state=42, use_smote=True)`

Inicializa el procesador de datos.

**Parámetros:**
- `test_size` (float): Proporción de datos para prueba (default: 0.2)
- `random_state` (int): Semilla para reproducibilidad (default: 42)
- `use_smote` (bool): Usar SMOTE para balanceo (default: True)

**Ejemplo:**
```python
processor = DataProcessor(test_size=0.2, use_smote=True)
```

---

### `load_and_merge_data(trans_path, id_path=None)`

Cargar y fusionar datos de transacciones e identidad.

**Parámetros:**
- `trans_path` (str): Ruta al archivo de transacciones (CSV)
- `id_path` (str, opcional): Ruta al archivo de identidad (CSV)

**Retorna:** DataFrame fusionado

**Ejemplo:**
```python
df = processor.load_and_merge_data(
    'data/raw/train_transaction.csv',
    'data/raw/train_identity.csv'
)
```

---

### `select_important_columns(df)`

Seleccionar columnas relevantes para modelado.

**Parámetros:**
- `df` (DataFrame): DataFrame con todos los datos

**Retorna:** DataFrame con columnas seleccionadas

**Ejemplo:**
```python
df_subset = processor.select_important_columns(df)
```

---

### `handle_missing_values(df)`

Manejar valores faltantes:
- Elimina columnas con >80% nulos
- Imputa numéricas con -999
- Imputa categóricas con 'Unknown'

**Parámetros:**
- `df` (DataFrame): DataFrame con valores faltantes

**Retorna:** DataFrame sin valores faltantes

**Ejemplo:**
```python
df_clean = processor.handle_missing_values(df)
```

---

### `feature_engineering(df)`

Crear nuevas características derivadas.

**Parámetros:**
- `df` (DataFrame): DataFrame de entrada

**Retorna:** DataFrame con nuevas características

**Característica creadas:**
- `TransactionAmt_log`: Logaritmo del monto
- `hour_sim`: Hora simulada del día
- `amt_card_interaction`: Interacción monto × tarjeta

**Ejemplo:**
```python
df_fe = processor.feature_engineering(df)
```

---

### `encode_categorical(df, fit=True)`

Codificar variables categóricas con LabelEncoder.

**Parámetros:**
- `df` (DataFrame): DataFrame a codificar
- `fit` (bool): Si True, entrena los encoders; si False, los aplica

**Retorna:** DataFrame con variables codificadas

**Ejemplo:**
```python
df_encoded = processor.encode_categorical(df, fit=True)
```

---

### `prepare_data(df)`

Pipeline completo de preparación (train/test split, escalado, SMOTE).

**Parámetros:**
- `df` (DataFrame): DataFrame procesado

**Retorna:** Tupla `(X_train, X_test, y_train, y_test)` - arrays NumPy escalados

**Ejemplo:**
```python
X_train, X_test, y_train, y_test = processor.prepare_data(df)
```

---

## FraudDetectionModel

Clase para entrenar y evaluar modelos de detección de fraudes.

### `__init__(model_type='xgboost', random_state=42)`

Inicializa el modelo.

**Parámetros:**
- `model_type` (str): Tipo de modelo ('xgboost' o 'random_forest')
- `random_state` (int): Semilla para reproducibilidad

**Ejemplo:**
```python
model = FraudDetectionModel(model_type='xgboost', random_state=42)
```

---

### `train_xgboost_smote(X_train, y_train)`

Entrenar XGBoost con datos balanceados por SMOTE.

**Parámetros:**
- `X_train` (ndarray): Features de entrenamiento (ya balanceadas con SMOTE)
- `y_train` (ndarray): Target de entrenamiento

**Retorna:** Modelo XGBoost entrenado

**Ejemplo:**
```python
model.train_xgboost_smote(X_train, y_train)
```

---

### `train_xgboost_weighted(X_train, y_train)`

Entrenar XGBoost con `scale_pos_weight`.

**Parámetros:**
- `X_train` (ndarray): Features de entrenamiento (no balanceadas)
- `y_train` (ndarray): Target de entrenamiento

**Retorna:** Modelo XGBoost entrenado

**Ejemplo:**
```python
model.train_xgboost_weighted(X_train, y_train)
```

---

### `predict(X)`

Realizar predicciones (0 o 1).

**Parámetros:**
- `X` (ndarray): Features para predecir

**Retorna:** Array de predicciones (0 o 1)

**Ejemplo:**
```python
predictions = model.predict(X_test)
```

---

### `predict_proba(X)`

Obtener probabilidades de predicción.

**Parámetros:**
- `X` (ndarray): Features para predecir

**Retorna:** Array de shape (n_samples, 2) con probabilidades

**Ejemplo:**
```python
proba = model.predict_proba(X_test)
fraud_probability = proba[:, 1]  # Probabilidad de fraude
```

---

### `evaluate(X_test, y_test, dataset_name='Test')`

Evaluar el modelo en un dataset.

**Parámetros:**
- `X_test` (ndarray): Features de prueba
- `y_test` (ndarray): Target de prueba
- `dataset_name` (str): Nombre del dataset para reportes

**Retorna:** Diccionario con métricas:
```python
{
    'precision': float,
    'recall': float,
    'f1': float,
    'f2': float,
    'roc_auc': float,
    'confusion_matrix': ndarray,
    'classification_report': dict,
    'predictions': ndarray,
    'probabilities': ndarray
}
```

**Ejemplo:**
```python
metrics = model.evaluate(X_test, y_test)
print(f"Precision: {metrics['precision']:.4f}")
print(f"Recall: {metrics['recall']:.4f}")
```

---

### `get_feature_importance(feature_names=None, top_n=20)`

Obtener importancia de características.

**Parámetros:**
- `feature_names` (list): Nombres de características
- `top_n` (int): Número de características a mostrar

**Retorna:** DataFrame con importancia ordenada

**Ejemplo:**
```python
importance = model.get_feature_importance(top_n=10)
print(importance)
```

---

### `save_model(path)`

Guardar modelo entrenado.

**Parámetros:**
- `path` (str): Ruta donde guardar el modelo

**Ejemplo:**
```python
model.save_model('models/fraud_model.pkl')
```

---

### `load_model(path)`

Cargar modelo entrenado.

**Parámetros:**
- `path` (str): Ruta del modelo a cargar

**Ejemplo:**
```python
model.load_model('models/fraud_model.pkl')
```

---

## ExplainabilityAnalyzer

Clase para explicar predicciones con SHAP.

### `__init__(model, X_background=None, X_explain=None)`

Inicializa el analizador.

**Parámetros:**
- `model`: Modelo entrenado
- `X_background` (ndarray): Datos de background para SHAP (recomendado: muestra de X_train)
- `X_explain` (ndarray): Datos para explicar (recomendado: X_test)

**Ejemplo:**
```python
analyzer = ExplainabilityAnalyzer(model, X_train[:100], X_test)
```

---

### `initialize_explainer(model_type='tree')`

Inicializar el explainer de SHAP.

**Parámetros:**
- `model_type` (str): 'tree' para tree-based models, 'kernel' para otros

**Ejemplo:**
```python
analyzer.initialize_explainer(model_type='tree')
```

---

### `compute_shap_values(X)`

Calcular SHAP values para un dataset.

**Parámetros:**
- `X` (ndarray): Datos para los que calcular SHAP values

**Retorna:** Array de SHAP values

**Ejemplo:**
```python
shap_values = analyzer.compute_shap_values(X_test)
```

---

### `plot_summary(feature_names=None, plot_type='bar', max_display=15)`

Crear SHAP summary plot (importancia global).

**Parámetros:**
- `feature_names` (list): Nombres de características
- `plot_type` (str): 'bar' o 'violin'
- `max_display` (int): Número de características a mostrar

**Retorna:** Figura matplotlib

**Ejemplo:**
```python
fig = analyzer.plot_summary(plot_type='bar', max_display=10)
plt.show()
```

---

### `plot_dependence(feature_idx, feature_names=None)`

Crear SHAP dependence plot para una característica.

**Parámetros:**
- `feature_idx` (int/str): Índice o nombre de la característica
- `feature_names` (list): Nombres de características

**Retorna:** Figura matplotlib

**Ejemplo:**
```python
fig = analyzer.plot_dependence('TransactionAmt')
plt.show()
```

---

### `plot_waterfall(instance_idx, feature_names=None, max_display=10)`

Crear SHAP waterfall plot para una instancia.

**Parámetros:**
- `instance_idx` (int): Índice de la muestra a explicar
- `feature_names` (list): Nombres de características
- `max_display` (int): Número de características a mostrar

**Retorna:** Figura matplotlib

**Ejemplo:**
```python
fig = analyzer.plot_waterfall(0, max_display=10)
plt.show()
```

---

### `get_feature_importance_ranking(feature_names=None, top_n=20)`

Obtener ranking de características por importancia SHAP.

**Parámetros:**
- `feature_names` (list): Nombres de características
- `top_n` (int): Número de características a mostrar

**Retorna:** DataFrame con importancia ordenada

**Ejemplo:**
```python
importance = analyzer.get_feature_importance_ranking(top_n=10)
print(importance)
```

---

### `explain_prediction(instance_idx, feature_names=None, top_n=10)`

Explicación detallada de una predicción.

**Parámetros:**
- `instance_idx` (int): Índice de la muestra
- `feature_names` (list): Nombres de características
- `top_n` (int): Número de características más importantes

**Retorna:** Diccionario con explicación:
```python
{
    'prediction': int,  # 0 o 1
    'fraud_probability': float,
    'legitimate_probability': float,
    'top_features': [
        {
            'feature': str,
            'value': float,
            'shap_value': float,
            'contribution': str  # 'aumenta riesgo' o 'disminuye riesgo'
        },
        ...
    ]
}
```

**Ejemplo:**
```python
explanation = analyzer.explain_prediction(0, top_n=5)
print(f"Predicción: {explanation['prediction']}")
print(f"Probabilidad de fraude: {explanation['fraud_probability']:.2%}")
```

---

## Flujo de Trabajo Completo

```python
from src.preprocessing import DataProcessor
from src.model import FraudDetectionModel
from src.explainability import ExplainabilityAnalyzer

# 1. Procesar datos
processor = DataProcessor()
df = processor.load_and_merge_data('data/raw/train_transaction.csv')
df = processor.select_important_columns(df)
df = processor.handle_missing_values(df)
df = processor.feature_engineering(df)
X_train, X_test, y_train, y_test = processor.prepare_data(df)

# 2. Entrenar modelo
model = FraudDetectionModel(model_type='xgboost')
model.train_xgboost_smote(X_train, y_train)

# 3. Evaluar
metrics = model.evaluate(X_test, y_test)

# 4. Explicar
analyzer = ExplainabilityAnalyzer(model, X_train[:100], X_test)
analyzer.initialize_explainer()
shap_values = analyzer.compute_shap_values(X_test)
importance = analyzer.get_feature_importance_ranking(top_n=10)
explanation = analyzer.explain_prediction(0, top_n=5)
```

---

## Manejo de Errores

Todos los módulos capturan excepciones comunes:

```python
try:
    analyzer.initialize_explainer()
except Exception as e:
    print(f"Error: {e}")
```

---

## Rendimiento y Optimizaciones

- **DataProcessor**: Eficiente con datasets grandes (>1M filas)
- **FraudDetectionModel**: Usa GPU automáticamente si está disponible
- **ExplainabilityAnalyzer**: TreeExplainer es rápido; usar KernelExplainer solo si es necesario

---

Para más ejemplos, consulta:
- `example_pipeline.py` - Ejemplo completo
- `notebooks/` - Notebooks con análisis detallado
- `dashboard/app.py` - Uso interactivo
