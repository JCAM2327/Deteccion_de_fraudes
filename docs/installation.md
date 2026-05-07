---
layout: default
title: Instalación Detallada
---

# 📖 Guía de Instalación Detallada

Instrucciones paso a paso para instalar y configurar el proyecto.

## Requisitos Previos

- **Python 3.8+** (recomendado 3.10+)
- **pip** (gestor de paquetes)
- **Git** (para clonar el repositorio)
- **4GB+ RAM** (para procesar el dataset)
- Acceso a Internet (para descargar dependencias)

---

## Instalación Paso a Paso

### 1️⃣ Clonar el Repositorio

```bash
git clone https://github.com/JCAM2327/Deteccion_de_fraudes.git
cd Deteccion_de_fraudes
```

### 2️⃣ Crear un Ambiente Virtual

**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**En Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**En Windows (CMD):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

### 3️⃣ Actualizar pip (Opcional)

```bash
pip install --upgrade pip
```

### 4️⃣ Instalar Dependencias

```bash
pip install -r requirements.txt
```

La instalación puede tomar 2-5 minutos.

### 5️⃣ Verificar la Instalación

```bash
python -c "
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import shap
import streamlit as st
print('✅ ¡Todas las librerías están instaladas!')
"
```

---

## Descargar Datos (Opcional)

### Opción 1: Automática (Requiere Kaggle API)

1. Ve a https://www.kaggle.com/settings/account
2. Haz clic en "Create New API Token"
3. Descarga `kaggle.json`
4. Coloca en `~/.kaggle/kaggle.json`

**En macOS/Linux:**
```bash
mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json
```

**En Windows:**
```
Coloca en C:\Users\TuNombre\.kaggle\kaggle.json
```

Ahora ejecuta:
```bash
python scripts/descargar.py
```

### Opción 2: Manual

1. Ve a https://www.kaggle.com/competitions/ieee-fraud-detection
2. Descarga:
   - `train_transaction.csv`
   - `train_identity.csv`
3. Coloca en `data/raw/`

---

## Verificar Estructura

Después de clonar, deberías tener:

```
Deteccion_de_fraudes/
├── src/                    # Módulos de código
├── dashboard/              # Dashboard Streamlit
├── notebooks/              # Notebooks Jupyter
├── docs/                   # Documentación
├── data/                   # Datos (crear después de descargar)
├── models/                 # Modelos (se crean después del entrenamiento)
├── requirements.txt        # Dependencias
└── README.md              # Este archivo
```

---

## Ejecución

### 🎨 Dashboard Interactivo (Recomendado)

```bash
cd dashboard
streamlit run app.py
```

Abre http://localhost:8501

### 📚 Notebooks Jupyter

```bash
jupyter notebook
```

Ve a `notebooks/01_EDA.ipynb` o `notebooks/02_feature_engineering_modelling.ipynb`

### 🐍 Script Python

```bash
python example_pipeline.py
```

---

## Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'src'"

**Causa:** No estás en el directorio correcto

**Solución:**
```bash
cd Deteccion_de_fraudes  # Asegúrate de estar en la carpeta correcta
python example_pipeline.py
```

---

### Error: "PermissionError" al crear venv

**Causa:** Permisos insuficientes

**Solución:**
```bash
python3 -m venv venv  # Usa python3 explícitamente
```

---

### Error: "No module named 'streamlit'"

**Causa:** Dependencies no instaladas correctamente

**Solución:**
```bash
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

---

### Error: "No such file or directory: 'data/raw/train_transaction.csv'"

**Causa:** Datos no descargados

**Solución:**
```bash
python scripts/descargar.py

# O descarga manualmente desde:
# https://www.kaggle.com/competitions/ieee-fraud-detection
```

---

### Error: SHAP es muy lento

**Causa:** Calculando SHAP values en todo el dataset

**Solución:** Usa un subconjunto:
```python
analyzer = ExplainabilityAnalyzer(model, X_train[:100], X_test[:50])
```

---

### Error: Memory Error (no hay suficiente memoria)

**Causa:** Dataset muy grande

**Solución:** Usa un subconjunto:
```python
processor = DataProcessor()
df = processor.load_and_merge_data('data/raw/train_transaction.csv')
df = df.sample(frac=0.1, random_state=42)  # Usa 10% de los datos
```

---

## Configuración Avanzada

### Variables de Entorno

Copia `.env.example` a `.env` y personaliza:

```bash
cp .env.example .env
```

Edita `.env`:
```
MODEL_TYPE=xgboost
RANDOM_STATE=42
USE_SMOTE=True
```

### Python Virtual Environment con conda

Si prefieres anaconda:

```bash
conda create -n fraud-detection python=3.10
conda activate fraud-detection
pip install -r requirements.txt
```

---

## Verificación Final

Para verificar que todo esté funcionando:

```bash
# 1. Prueba los módulos
python -c "from src.preprocessing import DataProcessor; print('✅ src.preprocessing OK')"
python -c "from src.model import FraudDetectionModel; print('✅ src.model OK')"
python -c "from src.explainability import ExplainabilityAnalyzer; print('✅ src.explainability OK')"

# 2. Prueba el dashboard
streamlit run dashboard/app.py
```

---

## Próximos Pasos

Después de instalar:

1. 🚀 [Comenzar con quickstart](getting-started.md)
2. 📊 [Explorar features](features.md)
3. 🔌 [Revisar API](api-reference.md)
4. 💡 [Ver ejemplos](examples.md)

---

## Información de Sistema

Para debugging, verifica tu sistema:

```bash
python --version
pip --version
python -m pip list  # Lista todas las librerías instaladas
```

---

[← Volver a inicio](index.md) | [Ejemplos →](examples.md)
