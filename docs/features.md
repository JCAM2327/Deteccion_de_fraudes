---
layout: default
title: Características
---

# ✨ Características del Proyecto

## 🎯 Análisis Exploratorio (EDA)

### Estadísticas Completas
- 🔢 Análisis de 394 variables
- 📊 Distribución de clases (0.57% fraudes)
- 📈 Correlaciones y dependencias
- 🔍 Detección de valores atípicos
- 📉 Análisis de valores nulos

### Visualizaciones Interactivas
- Gráficos dinámicos con Plotly
- Filtrado y exploración
- Comparativas por clase
- Tendencias temporales

---

## 🤖 Modelado Predictivo

### 3 Estrategias de Entrenamiento

#### ⭐ XGBoost + SMOTE
```
Precision:  92%
Recall:     87%
F1-Score:   0.89
ROC-AUC:    0.92
```

#### XGBoost + scale_pos_weight
```
Precision:  88%
Recall:     91%
F1-Score:   0.89
ROC-AUC:    0.91
```

#### Random Forest + SMOTE
```
Precision:  85%
Recall:     89%
F1-Score:   0.87
ROC-AUC:    0.90
```

### Características del Modelado
- ✅ Validación cruzada estratificada
- ✅ Ajuste de hiperparámetros
- ✅ Manejo automático de desbalanceo
- ✅ Métricas apropiadas para data imbalanceada
- ✅ Confusion matrix detallada

---

## 🔍 Explicabilidad con SHAP

### SHAP Summary Plots
- Importancia global de características
- Visualización bar y violin plots
- Ranking de features

### SHAP Dependence Plots
- Cómo interactúan características
- Efectos no lineales
- Dependencias de pares

### SHAP Waterfall Plots
- Explicación por transacción
- Contribución de cada feature
- Cálculo de base values

### Feature Importance
- Ranking SHAP global
- Contribución media absoluta
- Identificación de variables clave

---

## 💡 Dashboard Interactivo

### Sección 1: Inicio
- 📊 Métricas principales en vivo
- 📋 Descripción del proyecto
- 🎓 Instrucciones de uso
- 💼 Información del portafolio

### Sección 2: Análisis EDA
- 📈 Distribución de clases
- 💰 Análisis de montos
- 📊 Estadísticas descriptivas
- 🔍 Análisis de nulos

### Sección 3: Rendimiento de Modelos
- 📊 Matriz de confusión
- 📈 Comparación de 3 modelos
- 📉 Curva ROC
- 📋 Tabla de métricas

### Sección 4: Explicabilidad SHAP
- 🌟 Feature importance global
- 🔍 Explicación por transacción
- 🔗 Dependencias entre features
- 📊 Visualización interactiva

### Sección 5: Predictor Interactivo
- 🎯 Formulario de entrada
- ⚡ Predicción en tiempo real
- 📊 Explicación por SHAP
- 🎨 Gráfico de contribución

---

## 🏗️ Módulos Reutilizables

### DataProcessor
```python
processor = DataProcessor()
df = processor.load_and_merge_data(...)
df = processor.select_important_columns(df)
df = processor.handle_missing_values(df)
df = processor.feature_engineering(df)
X_train, X_test, y_train, y_test = processor.prepare_data(df)
```

### FraudDetectionModel
```python
model = FraudDetectionModel()
model.train_xgboost_smote(X_train, y_train)
metrics = model.evaluate(X_test, y_test)
importance = model.get_feature_importance(top_n=10)
```

### ExplainabilityAnalyzer
```python
analyzer = ExplainabilityAnalyzer(model, X_train, X_test)
analyzer.initialize_explainer()
shap_values = analyzer.compute_shap_values(X_test)
importance = analyzer.get_feature_importance_ranking()
explanation = analyzer.explain_prediction(idx)
```

---

## 📚 Documentación Completa

- ✅ Docstrings en todas las funciones
- ✅ Ejemplos de código incluídos
- ✅ Parámetros y retornos documentados
- ✅ Manejo robusto de errores
- ✅ Logging detallado

---

## 🔧 Configuración Flexible

### Variables de Entorno
```bash
MODEL_TYPE=xgboost
RANDOM_STATE=42
TEST_SIZE=0.2
USE_SMOTE=True
```

### Parámetros Ajustables
- Proporción train/test
- Usar o no SMOTE
- Tipo de modelo
- Número de características
- Umbral de nulos

---

## 🚀 Rendimiento

- ⚡ Procesamiento rápido de 590K transacciones
- 💾 Bajo uso de memoria
- 🔄 Escalable a datasets más grandes
- 🎯 Predicciones en tiempo real

---

## 📦 Dependencias Mínimas

Solo las librerías esenciales:
- Pandas, NumPy - manipulación de datos
- Scikit-Learn - ML base
- XGBoost - gradient boosting
- SHAP - explicabilidad
- Streamlit - dashboard

---

## 🌟 Casos de Uso

### Análisis Académico
Demostración de técnicas ML avanzadas

### Competiciones
Aplicable a Kaggle, hackathons

### Producción
Fácil de adaptar a datos reales

### Educación
Material de aprendizaje completo

---

[← Volver a inicio](index.md) | [Referencia API →](api-reference.md)
