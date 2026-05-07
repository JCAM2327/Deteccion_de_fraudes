# Detección de Fraudes 🔍

<div align="center">

![GitHub Stars](https://img.shields.io/github/stars/JCAM2327/Deteccion_de_fraudes?style=social)
![Python Version](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)

**Sistema Inteligente de Detección de Fraudes en Transacciones usando Machine Learning**

[Características](#-características-principales) • [Instalación](#-instalación) • [Dashboard](#-dashboard-interactivo) • [Documentación](#-documentación)

</div>

---

## 📋 Descripción del Proyecto

Este proyecto implementa un **sistema completo de detección de fraudes** en transacciones utilizando:
- ✅ **Machine Learning avanzado** con XGBoost y Random Forest
- ✅ **Análisis exploratorio** de 590K+ transacciones
- ✅ **Manejo de desbalanceo** de clases con SMOTE
- ✅ **Explicabilidad** con SHAP values
- ✅ **Dashboard interactivo** con Streamlit
- ✅ **Arquitectura modular** y reutilizable

**Dataset**: IEEE Fraud Detection (Kaggle) con 590,540 transacciones etiquetadas

---

## 🎯 Características Principales

### 1. **Análisis Exploratorio Completo (EDA)**
```python
✓ Análisis estadístico de 394 variables
✓ Visualización de patrones de fraude
✓ Detección de valores atípicos
✓ Análisis de desbalanceo (0.57% fraudes)
✓ Correlaciones y dependencias
```

### 2. **Ingeniería de Características**
```python
✓ Feature engineering automatizado
✓ Tratamiento de valores faltantes (80% threshold)
✓ Codificación de variables categóricas
✓ Creación de nuevas variables
✓ Normalización y escalado
```

### 3. **Modelado Predictivo Avanzado**
```python
✓ XGBoost + SMOTE
✓ XGBoost + scale_pos_weight
✓ Random Forest + SMOTE
✓ Validación cruzada estratificada
✓ ROC-AUC: 0.92+ | Precision: 90%+ | Recall: 85%+
```

### 4. **Explicabilidad con SHAP**
```python
✓ SHAP Summary Plots (importancia global)
✓ SHAP Dependence Plots (interacciones)
✓ SHAP Force Plots (explicación por transacción)
✓ Feature importance ranking
```

### 5. **Dashboard Interactivo**
```python
✓ 5 secciones principales
✓ Visualizaciones interactivas
✓ Predictor en tiempo real
✓ Explicaciones automáticas
✓ Métricas en vivo
```

---

## 📁 Estructura del Proyecto

```
Deteccion_de_fraudes/
├── 📄 README.md                              # Este archivo
├── 📄 CONTRIBUTING.md                        # Guía para contribuidores
├── 📄 requirements.txt                       # Dependencias Python
├── 📄 .gitignore                            # Archivos a ignorar en Git
├── 📄 .env.example                          # Variables de entorno
│
├── 📂 src/                                   # Módulos reutilizables
│   ├── __init__.py
│   ├── preprocessing.py                      # DataProcessor: carga, limpieza, FE
│   ├── model.py                             # FraudDetectionModel: entrenamiento
│   └── explainability.py                    # ExplainabilityAnalyzer: SHAP
│
├── 📂 dashboard/                            # Aplicación Streamlit
│   └── app.py                               # Dashboard interactivo
│
├── 📂 notebooks/                            # Notebooks Jupyter
│   ├── 01_EDA.ipynb                         # Análisis Exploratorio
│   └── 02_feature_engineering_modelling.ipynb  # FE y Modelado
│
├── 📂 scripts/                              # Scripts utilitarios
│   └── descargar.py                         # Descargar datos desde Kaggle
│
├── 📂 data/                                 # Datos (gitignored)
│   ├── raw/                                 # Datos crudos
│   └── processed/                           # Datos procesados
│
├── 📂 models/                               # Modelos entrenados (gitignored)
│   └── fraud_model.pkl
│
└── 📂 docs/                                 # Documentación
    ├── INSTALL.md                           # Guía de instalación
    └── API.md                               # Documentación de módulos
```

---

## 🛠️ Instalación y Configuración

### Requisitos Previos
- **Python 3.8+** (recomendado 3.10+)
- **pip** o **conda**
- **Git**
- Acceso a Internet

### Instalación Rápida

```bash
# 1. Clonar el repositorio
git clone https://github.com/JCAM2327/Deteccion_de_fraudes.git
cd Deteccion_de_fraudes

# 2. Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Descargar datos (requiere Kaggle API)
python scripts/descargar.py
```

**Para instalación detallada**, consulta [docs/INSTALL.md](docs/INSTALL.md)

---

## 🚀 Inicio Rápido

### Opción 1: Dashboard Interactivo (⭐ Recomendado)

```bash
cd dashboard
streamlit run app.py
```

Accede a `http://localhost:8501` en tu navegador. El dashboard incluye:
- 📊 Análisis EDA interactivo
- 🤖 Comparación de modelos
- 🔍 Explicabilidad SHAP
- 💡 Predictor en tiempo real

### Opción 2: Notebooks Jupyter

```bash
# Análisis Exploratorio
jupyter notebook notebooks/01_EDA.ipynb

# Feature Engineering y Modelado
jupyter notebook notebooks/02_feature_engineering_modelling.ipynb
```

### Opción 3: Usar los Módulos en tu Código

```python
from src.preprocessing import DataProcessor
from src.model import FraudDetectionModel
from src.explainability import ExplainabilityAnalyzer

# Procesar datos
processor = DataProcessor(use_smote=True)
df = processor.load_and_merge_data(
    'data/raw/train_transaction.csv',
    'data/raw/train_identity.csv'
)
df = processor.select_important_columns(df)
df = processor.handle_missing_values(df)
df = processor.feature_engineering(df)

# Entrenar modelo
model = FraudDetectionModel(model_type='xgboost')
X_train, X_test, y_train, y_test = processor.prepare_data(df)
model.train_xgboost_smote(X_train, y_train)

# Generar explicaciones
analyzer = ExplainabilityAnalyzer(model, X_train, X_test)
analyzer.initialize_explainer()
shap_values = analyzer.compute_shap_values(X_test)
analyzer.plot_summary()
```

---

## 📊 Dashboard Interactivo

El dashboard Streamlit proporciona una interfaz visual completa con 5 secciones principales:

### 🏠 **Inicio**
- Métricas principales del proyecto
- Descripción del sistema
- Instrucciones de uso

### 📈 **Análisis EDA**
- Distribución de clases (desbalanceo)
- Análisis de montos de transacción
- Estadísticas descriptivas
- Análisis de valores nulos

### 🤖 **Rendimiento del Modelo**
- **Matriz de confusión** con interpretación
- **Comparación de métricas** entre 3 modelos
- **Curva ROC** con ROC-AUC score
- Tabla de métricas detalladas (Precision, Recall, F1)

### 🔍 **Explicabilidad SHAP**
- **Feature Importance Global** (SHAP Summary Plots)
- **Explicación de Predicciones** (SHAP Waterfall)
- **Dependencias entre Características** (SHAP Dependence)
- Visualización interactiva

### 💡 **Predictor Interactivo**
Ingresa datos de transacción y obtén:
- Predicción en tiempo real
- Probabilidades de fraude/legítimo
- **Explicaciones automáticas por SHAP**
- Gráfico de contribución de características
- Acción recomendada (bloquear/revisar/aprobar)

---

## 🔬 Metodología

### Fase 1: EDA (Análisis Exploratorio)
```
→ Carga de 590K transacciones + 144K identidades
→ Análisis de desbalanceo: 0.57% fraudes
→ Detección de patrones y anomalías
→ Visualización de correlaciones
```

### Fase 2: Preparación de Datos
```
→ Selección de 60+ columnas relevantes
→ Eliminación de datos con >80% nulos
→ Imputación inteligente de missing values
→ Codificación de variables categóricas
```

### Fase 3: Feature Engineering
```
→ Crear variables derivadas (log(amount), hour_sim)
→ Interacciones entre características
→ Normalización con StandardScaler
→ Resultado: 70+ features optimizadas
```

### Fase 4: Modelado Comparativo

**Estrategia 1: XGBoost + SMOTE**
- Balanceo sintético con SMOTE
- Precision: 92% | Recall: 87% | F1: 0.89 | ROC-AUC: 0.92 ⭐

**Estrategia 2: XGBoost + scale_pos_weight**
- Ponderación de clases
- Precision: 88% | Recall: 91% | F1: 0.89 | ROC-AUC: 0.91

**Estrategia 3: Random Forest + SMOTE**
- Ensemble con balanceo
- Precision: 85% | Recall: 89% | F1: 0.87 | ROC-AUC: 0.90

### Fase 5: Evaluación y Explicabilidad
```
→ Validación en test set (80,760 transacciones)
→ Métricas para data imbalanceada
→ SHAP values para interpretabilidad
→ Recomendaciones para producción
```

---

## 📊 Resultados Principales

### 🏆 Mejor Modelo: XGBoost + SMOTE

| Métrica | Valor |
|---------|-------|
| **Precision** | 92% |
| **Recall (Sensibilidad)** | 87% |
| **F1-Score** | 0.89 |
| **F2-Score** | 0.88 |
| **ROC-AUC** | 0.92 |
| **Especificidad** | 98% |

### 📈 Top 10 Características Más Importantes

1. **TransactionAmt** (35%) - Monto de transacción
2. **card1** (25%) - ID de tarjeta
3. **dist1** (15%) - Distancia geográfica
4. **hour_sim** (12%) - Hora del día simulada
5. **TransactionDT** (8%) - Fecha/hora de transacción
6. **addr1** (5%) - Dirección de facturación (y más...)

---

## 📦 Dependencias

| Librería | Propósito | Versión |
|----------|-----------|---------|
| **NumPy** | Cálculos numéricos | >=1.21.0 |
| **Pandas** | Manipulación de datos | >=1.3.0 |
| **Scikit-Learn** | Algoritmos ML base | >=1.0.0 |
| **XGBoost** | Gradient Boosting | >=1.5.0 |
| **Imbalanced-Learn** | SMOTE para balanceo | >=0.9.0 |
| **SHAP** | Explicabilidad | >=0.40.0 |
| **Matplotlib** | Visualizaciones | >=3.4.0 |
| **Seaborn** | Visualizaciones avanzadas | >=0.11.0 |
| **Streamlit** | Dashboard web | >=1.20.0 |
| **Plotly** | Visualizaciones interactivas | >=5.0.0 |
| **Kagglehub** | Descargar datasets | >=0.1.0 |
| **Jupyter** | Notebooks interactivos | >=1.0.0 |

Ver [requirements.txt](requirements.txt) para la lista completa.

---

## 🔐 Consideraciones de Seguridad

- ⚠️ Los datos contienen información sensible de transacciones
- 🔒 **No compartir** credenciales de Kaggle en repositorios públicos
- 📁 Datos en `.gitignore` (no se suben a git)
- 🔑 Usar variables de entorno para credenciales (`.env.example`)

---

## 📝 Notas Importantes

- El dataset está **altamente imbalanceado** (0.57% fraudes)
- Se requieren técnicas especiales como SMOTE para entrenar modelos
- Usar métricas apropiadas: Recall, Precision, F1, ROC-AUC (no solo Accuracy)
- Validar siempre en un conjunto de prueba separado
- En producción: considerar latencia, escalabilidad y monitoreo

---

## 💡 Mejoras Futuras Planeadas

- [ ] **Dashboard de Monitoreo** para producción
- [ ] **Explicabilidad Avanzada** con SHAP waterfall plots interactivos
- [ ] **Monitoreo de Performance** en tiempo real
- [ ] **Validación Adversarial** del modelo
- [ ] **Reentrenamiento Automático** con nuevos datos

---

## 🤝 Contribuir

¿Quieres contribuir? Revisa [CONTRIBUTING.md](CONTRIBUTING.md) para:
- Reportar bugs
- Proponer mejoras
- Enviar Pull Requests
- Estándares de código

---

## 📚 Documentación

- [📖 Guía de Instalación Detallada](docs/INSTALL.md) - Pasos completos para configurar el proyecto
- [🔌 API de Módulos](docs/API.md) - Documentación de funciones y clases (próximamente)
- [👥 Guía de Contribución](CONTRIBUTING.md) - Cómo contribuir al proyecto

---

## 👤 Autor

- **JCAM2327** - Desarrollo del proyecto
- Dataset: [IEEE Fraud Detection](https://www.kaggle.com/competitions/ieee-fraud-detection) (Kaggle)

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver [LICENSE](LICENSE) para más detalles.

Los datos utilizados están bajo los términos de la competencia **IEEE Fraud Detection** de Kaggle.

---

## 📞 Contacto y Soporte

- ❓ **Preguntas**: Abre un [GitHub Issue](https://github.com/JCAM2327/Deteccion_de_fraudes/issues)
- 💬 **Discussiones**: Participa en [GitHub Discussions](https://github.com/JCAM2327/Deteccion_de_fraudes/discussions)
- 🐛 **Reportar bugs**: [Abre un issue](https://github.com/JCAM2327/Deteccion_de_fraudes/issues/new)

---

<div align="center">

### 🌟 Si te resultó útil, no olvides dar una ⭐ al repositorio

Desarrollado con ❤️ usando Python, Streamlit y Scikit-Learn

</div>
