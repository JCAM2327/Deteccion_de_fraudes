# Guía de Instalación y Configuración

## 📋 Requisitos Previos

- **Python 3.8+** (recomendado 3.10 o superior)
- **pip** (gestor de paquetes de Python)
- **Git** (para clonar el repositorio)
- **Conexión a Internet** (para descargar datos y dependencias)

### Para Usuarios de Windows
Se recomienda usar **Windows Terminal** o **PowerShell** para mejor compatibilidad.

---

## 🚀 Instalación Paso a Paso

### 1. Clonar el Repositorio

```bash
git clone https://github.com/JCAM2327/Deteccion_de_fraudes.git
cd Deteccion_de_fraudes
```

### 2. Crear un Ambiente Virtual (Recomendado)

**En macOS/Linux:**
```bash
python -m venv venv
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

### 3. Actualizar pip (Opcional)

```bash
pip install --upgrade pip
```

### 4. Instalar Dependencias

```bash
pip install -r requirements.txt
```

La instalación puede tomar algunos minutos dependiendo de tu conexión.

### 5. Configurar Credenciales de Kaggle (Para Descargar Datos)

Sigue estos pasos solo si deseas descargar el dataset automáticamente:

1. Ve a https://www.kaggle.com/settings/account
2. Haz clic en "Create New API Token"
3. Se descargará un archivo `kaggle.json`
4. Coloca el archivo en la ubicación correcta:

   **En macOS/Linux:**
   ```bash
   mkdir -p ~/.kaggle
   mv ~/Downloads/kaggle.json ~/.kaggle/
   chmod 600 ~/.kaggle/kaggle.json
   ```

   **En Windows:**
   ```
   C:\Users\TuNombre\.kaggle\kaggle.json
   ```

---

## 📥 Descargar Datos

### Opción 1: Descargar Automáticamente

```bash
python scripts/descargar.py
```

Los datos se guardarán en `data/raw/`.

### Opción 2: Descargar Manualmente

1. Ve a https://www.kaggle.com/competitions/ieee-fraud-detection
2. Descarga los archivos:
   - `train_transaction.csv`
   - `train_identity.csv`
3. Coloca los archivos en `data/raw/`

---

## 🏃 Ejecutar el Dashboard

### Iniciar la Aplicación

```bash
cd dashboard
streamlit run app.py
```

La aplicación abrirá en tu navegador en `http://localhost:8501`.

### Características del Dashboard

- 📊 Análisis Exploratorio de Datos (EDA)
- 🤖 Rendimiento de Modelos
- 🔍 Explicabilidad con SHAP
- 💡 Predictor Interactivo en Tiempo Real

---

## 📓 Ejecutar los Notebooks

### Notebook 1: Análisis Exploratorio

```bash
jupyter notebook notebooks/01_EDA.ipynb
```

### Notebook 2: Feature Engineering y Modelado

```bash
jupyter notebook notebooks/02_feature_engineering_modelling.ipynb
```

---

## 🔧 Usar los Módulos en tu Código

Los módulos se pueden importar y usar en tus propios scripts:

```python
from src.preprocessing import DataProcessor
from src.model import FraudDetectionModel
from src.explainability import ExplainabilityAnalyzer

# Cargar y procesar datos
processor = DataProcessor()
df = processor.load_and_merge_data(
    'data/raw/train_transaction.csv',
    'data/raw/train_identity.csv'
)

# ... resto del código
```

Ver documentación de cada módulo para ejemplos completos.

---

## 🐛 Solución de Problemas

### Error: "ModuleNotFoundError: No module named 'src'"

**Solución:** Asegúrate de estar en el directorio raíz del proyecto
```bash
cd Deteccion_de_fraudes
```

### Error: "PermissionError" al crear venv

**Solución:** Usa:
```bash
python3 -m venv venv
```

### Error: "No such file or directory: 'data/raw/train_transaction.csv'"

**Solución:** Descarga los datos ejecutando:
```bash
python scripts/descargar.py
```

### Error: "SHAP calculation too slow"

**Solución:** Usa un subconjunto de datos para explicabilidad:
```python
X_explain_sample = X_explain[:100]  # Primeras 100 muestras
analyzer.compute_shap_values(X_explain_sample)
```

---

## 📦 Dependencias Principales

| Librería | Versión | Propósito |
|----------|---------|-----------|
| pandas | >=1.3.0 | Manipulación de datos |
| numpy | >=1.21.0 | Cálculos numéricos |
| scikit-learn | >=1.0.0 | Algoritmos ML |
| xgboost | >=1.5.0 | Gradient boosting |
| shap | >=0.40.0 | Explicabilidad |
| streamlit | >=1.20.0 | Dashboard |
| imbalanced-learn | >=0.9.0 | SMOTE |

Para ver todas las dependencias ejecuta:
```bash
pip list
```

---

## ✅ Verificar la Instalación

Ejecuta este comando para verificar que todo esté instalado correctamente:

```bash
python -c "
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
import shap
import streamlit as st
print('✅ Todas las librerías instaladas correctamente!')
"
```

---

## 🎓 Próximos Pasos

1. Revisa el [README.md](README.md) para entender el proyecto
2. Ejecuta el Dashboard para explorar los datos
3. Lee los notebooks para aprender sobre el análisis
4. Experimenta con el módulo `src/` para crear tus propios modelos

¡Bienvenido al proyecto! Si tienes preguntas, abre un [Issue](https://github.com/JCAM2327/Deteccion_de_fraudes/issues) 🎉
