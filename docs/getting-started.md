---
layout: default
title: Inicio Rápido
---

# Inicio Rápido
---

Comienza a usar el proyecto en **5 minutos**.

## Requisitos

- Python 3.8+
- Git
- pip

## Instalación

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/JCAM2327/Deteccion_de_fraudes.git
cd Deteccion_de_fraudes
```

### 2️⃣ Crear ambiente virtual

```bash
# En macOS/Linux
python -m venv venv
source venv/bin/activate

# En Windows
python -m venv venv
venv\Scripts\activate
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

## Uso

### Opción 1: Dashboard Interactivo ⭐ (Recomendado)

```bash
cd dashboard
streamlit run app.py
```

Abre http://localhost:8501 en tu navegador

### Opción 2: Ejemplo Python

```bash
python example_pipeline.py
```

### Opción 3: Usar los módulos

```python
from src.preprocessing import DataProcessor
from src.model import FraudDetectionModel

# Procesar datos
processor = DataProcessor()
df = processor.load_and_merge_data('data/raw/train_transaction.csv')
# ... más procesamiento

# Entrenar
model = FraudDetectionModel()
model.train_xgboost_smote(X_train, y_train)

# Predecir
predictions = model.predict(X_test)
```

## Dashboard - 5 Secciones

| Sección | Descripción |
|---------|------------|
| 🏠 **Inicio** | Métricas y descripción |
| 📈 **EDA** | Análisis exploratorio |
| 🤖 **Modelos** | Comparación de rendimiento |
| 🔍 **SHAP** | Explicabilidad |
| 💡 **Predictor** | Predicción en tiempo real |

## Próximos Pasos

- 📖 Lee la [documentación completa](api-reference.md)
- 💡 Explora los [ejemplos](examples.md)
- 🎨 Personaliza el [dashboard](features.md)

## ¿Problemas?

Ver [Troubleshooting](installation.md#solución-de-problemas) en la guía de instalación.

---

[← Volver a inicio](index.md)
