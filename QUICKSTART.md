# 🚀 Guía Rápida - Detección de Fraudes

## Inicio en 5 minutos

### 1. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 2. Descargar datos (opcional)
```bash
python scripts/descargar.py
```

### 3. Lanzar el Dashboard 🎉
```bash
cd dashboard
streamlit run app.py
```

¡El dashboard se abrirá en `http://localhost:8501`!

---

## Características del Dashboard

| Sección | Descripción |
|---------|------------|
| 🏠 **Inicio** | Métricas y descripción general |
| 📈 **EDA** | Análisis exploratorio interactivo |
| 🤖 **Modelos** | Comparación de rendimiento |
| 🔍 **SHAP** | Explicabilidad de predicciones |
| 💡 **Predictor** | Predice fraudes en tiempo real |

---

## Usar los Módulos en tu Código

```python
from src.preprocessing import DataProcessor
from src.model import FraudDetectionModel

# Procesar datos
processor = DataProcessor()
df = processor.load_and_merge_data('data/raw/train_transaction.csv')
# ... más procesamiento

# Entrenar modelo
model = FraudDetectionModel()
model.train_xgboost_smote(X_train, y_train)

# Predecir
predictions = model.predict(X_test)
```

Ver [docs/API.md](docs/API.md) para documentación completa.

---

## Ejecución Completa

```bash
# Pipeline de principio a fin
python example_pipeline.py
```

---

## Documentación

- 📖 [Instalación Completa](docs/INSTALL.md)
- 🔌 [Documentación de API](docs/API.md)
- 👥 [Guía de Contribución](CONTRIBUTING.md)
- 📊 [README Completo](README.md)

---

## Características Clave ✨

✅ **590K+ transacciones** analizadas  
✅ **3 modelos** entrenados y comparados  
✅ **92% Precision** en detección de fraudes  
✅ **SHAP Explainability** integrada  
✅ **Dashboard interactivo** con Streamlit  
✅ **Módulos reutilizables** y documentados  

---

## Próximos Pasos

1. ✔️ Dashboard exploratorio
2. ✔️ Modelos entrenados
3. 📋 Integrar con API (opcional)
4. 📋 Desplegar en producción (opcional)

---

¿Problemas? Revisa [docs/INSTALL.md](docs/INSTALL.md) para solución de errores.
