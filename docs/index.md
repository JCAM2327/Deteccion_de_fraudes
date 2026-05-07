---
layout: default
title: Detección de Fraudes en Transacciones
description: Sistema inteligente de detección de fraudes usando Machine Learning
---

# 🔍 Detección de Fraudes en Transacciones

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

## Descripción del Proyecto

Sistema completo de **detección de fraudes** en transacciones que utiliza:

- ✅ **Machine Learning avanzado** con XGBoost y Random Forest
- ✅ **Análisis experimental** de 590K+ transacciones
- ✅ **Explicabilidad SHAP** para entender predicciones
- ✅ **Dashboard interactivo** en tiempo real
- ✅ **Arquitectura modular** y reutilizable

**Dataset**: [IEEE Fraud Detection](https://www.kaggle.com/competitions/ieee-fraud-detection) de Kaggle

---

## 🎯 Resultados Principales

### Mejor Modelo: XGBoost + SMOTE

| Métrica | Valor |
|---------|-------|
| **Precision** | 92% |
| **Recall** | 87% |
| **F1-Score** | 0.89 |
| **ROC-AUC** | 0.92 |

*590,540 transacciones analizadas | 0.57% fraudes detectados*

---

## 🚀 Inicio Rápido

### 1. Instalar
```bash
git clone https://github.com/JCAM2327/Deteccion_de_fraudes.git
cd Deteccion_de_fraudes
pip install -r requirements.txt
```

### 2. Lanzar Dashboard
```bash
cd dashboard
streamlit run app.py
```

### 3. Acceder
Abre `http://localhost:8501` en tu navegador

---

## 📚 Documentación

- [🚀 Inicio Rápido](getting-started.md) - Comienza en 5 minutos
- [✨ Características](features.md) - Descubre todas las capacidades
- [🔌 Referencia API](api-reference.md) - Documentación de módulos  
- [💡 Ejemplos](examples.md) - Casos de uso prácticos
- [📖 Instalación Completa](installation.md) - Guía detallada

---

## 🏗️ Arquitectura

```
┌─────────────────────────────────────┐
│      Dashboard Streamlit 🎨         │
│  (EDA • Modelos • SHAP • Predictor) │
└──────────────┬──────────────────────┘
               │
     ┌─────────┼─────────┐
     │         │         │
     ▼         ▼         ▼
┌────────┐ ┌───────┐ ┌──────────┐
│ Datos  │ │Modelos│ │  SHAP    │
│ (src/) │ │(src/) │ │  (src/)  │
└────────┘ └───────┘ └──────────┘
```

---

## 🤖 Modelos Entrenados

### Estrategia 1: XGBoost + SMOTE ⭐
- **Balanceo sintético** con SMOTE
- **Precision**: 92% | **Recall**: 87%

### Estrategia 2: XGBoost + scale_pos_weight
- **Ponderación de clases**
- **Precision**: 88% | **Recall**: 91%

### Estrategia 3: Random Forest + SMOTE
- **Ensemble con balanceo**
- **Precision**: 85% | **Recall**: 89%

---

## 📊 Dashboard Interactivo

El dashboard proporciona **5 secciones**:

### 🏠 **Inicio**
Métricas principales y descripción general del proyecto

### 📈 **Análisis EDA**
- Distribución de clases (desbalanceo)
- Análisis de montos de transacción
- Estadísticas descriptivas
- Visualización de valores nulos

### 🤖 **Rendimiento del Modelo**
- Matriz de confusión
- Comparación de 3 modelos
- Curva ROC
- Métricas detalladas

### 🔍 **Explicabilidad SHAP**
- Feature importance global
- Explicación por transacción
- Dependencias entre características
- Visualización interactiva

### 💡 **Predictor Interactivo**
- Formulario de entrada
- Predicción en tiempo real
- Explicaciones automáticas
- Acción recomendada

---

## 🔧 Tecnologías Utilizadas

| Categoría | Herramientas |
|-----------|-----------|
| **Data Science** | Pandas, NumPy, Scikit-Learn |
| **Modelado** | XGBoost, Random Forest |
| **Balanceo** | SMOTE (Imbalanced-Learn) |
| **Explicabilidad** | SHAP, LIME |
| **Visualización** | Matplotlib, Seaborn, Plotly |
| **Dashboard** | Streamlit |
| **Cloud** | GitHub Pages, Streamlit Cloud |

---

## 📁 Estructura del Proyecto

```
Deteccion_de_fraudes/
├── src/                          # Módulos reutilizables
│   ├── preprocessing.py          # Carga y procesamiento de datos
│   ├── model.py                  # Entrenamiento de modelos
│   └── explainability.py         # SHAP explainability
├── dashboard/                    # Dashboard Streamlit
│   └── app.py                    # Aplicación interactiva
├── notebooks/                    # Análisis en Jupyter
│   ├── 01_EDA.ipynb
│   └── 02_feature_engineering_modelling.ipynb
├── docs/                         # Documentación (GitHub Pages)
└── data/                         # Datos (no incluídos)
```

---

## 🎓 Aprendizajes Clave

Este proyecto demuestra:

✅ **Manejo de datos imbalanceados** con SMOTE  
✅ **Comparación de múltiples modelos**  
✅ **Métricas apropiadas** para clasificación  
✅ **Explicabilidad con SHAP**  
✅ **Dashboard interactivo** con Streamlit  
✅ **Arquitectura modular** y reutilizable  
✅ **Documentación profesional**  

---

## 🤝 Contribuir

¿Quieres contribuir? Ver [CONTRIBUTING.md](https://github.com/JCAM2327/Deteccion_de_fraudes/blob/main/CONTRIBUTING.md)

---

## 📄 Licencia

Licencia MIT - Ver [LICENSE](https://github.com/JCAM2327/Deteccion_de_fraudes/blob/main/LICENSE)

---

## 📞 Contacto

- **GitHub**: [@JCAM2327](https://github.com/JCAM2327)
- **Proyecto**: [Deteccion_de_fraudes](https://github.com/JCAM2327/Deteccion_de_fraudes)

---

<div align="center">

### 🌟 Si te resultó útil, ¡dale una ⭐ en GitHub!

**Desarrollado con ❤️ usando Python y Machine Learning**

</div>
