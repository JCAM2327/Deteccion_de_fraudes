"""
Módulo de preprocesamiento de datos.

Incluye funciones para carga, limpieza e ingeniería de características.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
import joblib
from pathlib import Path


class DataProcessor:
    """
    Clase para procesar y preparar datos para modelado de fraudes.
    
    Incluye:
    - Carga de datos
    - Manejo de valores nulos
    - Codificación de variables categóricas
    - Feature engineering
    - Balanceo de clases con SMOTE
    - División train/test
    """
    
    def __init__(self, test_size=0.2, random_state=42, use_smote=True):
        """
        Inicializar el procesador de datos.
        
        Args:
            test_size: Proporción de datos para prueba (default: 0.2)
            random_state: Semilla para reproducibilidad (default: 42)
            use_smote: Usar SMOTE para balanceo (default: True)
        """
        self.test_size = test_size
        self.random_state = random_state
        self.use_smote = use_smote
        self.scaler = StandardScaler()
        self.label_encoders = {}
        self.categorical_cols = []
        self.numeric_cols = []
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        
    def load_and_merge_data(self, trans_path, id_path=None):
        """
        Cargar y fusionar datos de transacciones e identidad.
        
        Args:
            trans_path: Ruta al archivo de transacciones
            id_path: Ruta al archivo de identidad (opcional)
            
        Returns:
            DataFrame con datos combinados
        """
        print("📥 Cargando datos de transacciones...")
        df_trans = pd.read_csv(trans_path)
        print(f"   Shape: {df_trans.shape}")
        
        if id_path:
            print("📥 Cargando datos de identidad...")
            df_id = pd.read_csv(id_path)
            print(f"   Shape: {df_id.shape}")
            
            print("🔗 Fusionando tablas...")
            df = pd.merge(df_trans, df_id, on='TransactionID', how='left')
            print(f"   Shape final: {df.shape}")
        else:
            df = df_trans
            
        return df
    
    def select_important_columns(self, df):
        """
        Seleccionar columnas relevantes para modelado.
        
        Args:
            df: DataFrame con todos los datos
            
        Returns:
            DataFrame con columnas seleccionadas
        """
        # Columnas predefinidas estadísticamente relevantes
        columnas_numericas = [
            'TransactionAmt', 'TransactionDT', 'card1', 'card2', 'card3',
            'addr1', 'addr2', 'dist1', 'dist2'
        ]
        columnas_c = [f'C{i}' for i in range(1, 15)]
        columnas_d = [f'D{i}' for i in range(1, 16)]
        columnas_id = [f'id_{i:02d}' for i in range(1, 39)]
        columnas_categoricas = [
            'ProductCD', 'card4', 'card6', 'P_emaildomain',
            'R_emaildomain', 'DeviceType', 'DeviceInfo'
        ]
        
        cols_keep = (
            ['TransactionID', 'isFraud'] + columnas_numericas +
            columnas_c + columnas_d + columnas_categoricas + columnas_id
        )
        cols_keep = [col for col in cols_keep if col in df.columns]
        
        df_subset = df[cols_keep].copy()
        print(f"✂️ Columnas seleccionadas: {len(cols_keep)}")
        print(f"   Shape: {df_subset.shape}")
        
        return df_subset
    
    def handle_missing_values(self, df):
        """
        Manejar valores faltantes.
        
        - Elimina columnas con >80% nulos
        - Imputa valores numéricos con -999
        - Imputa valores categóricos con 'Unknown'
        
        Args:
            df: DataFrame con datos faltantes
            
        Returns:
            DataFrame sin valores faltantes
        """
        # Verificar nulos
        null_perc = df.isnull().mean() * 100
        print(f"\n🔍 Análisis de valores nulos:")
        print(f"   Total de nulos: {df.isnull().sum().sum()}")
        
        # Eliminar columnas con >80% nulos
        high_null_cols = null_perc[null_perc > 80].index.tolist()
        if high_null_cols:
            print(f"   Eliminadas {len(high_null_cols)} columnas con >80% nulos")
            df = df.drop(columns=high_null_cols)
        
        # Identificar tipos
        self.numeric_cols = df.select_dtypes(
            include=['float64', 'int64']
        ).columns.tolist()
        self.numeric_cols = [
            c for c in self.numeric_cols
            if c not in ['isFraud', 'TransactionID']
        ]
        self.categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
        
        # Imputar
        df[self.numeric_cols] = df[self.numeric_cols].fillna(-999)
        df[self.categorical_cols] = df[self.categorical_cols].fillna('Unknown')
        
        print(f"   ✅ No hay valores nulos después de imputar")
        
        return df
    
    def feature_engineering(self, df):
        """
        Crear nuevas características.
        
        Args:
            df: DataFrame de entrada
            
        Returns:
            DataFrame con nuevas características
        """
        print("\n🔧 Feature Engineering:")
        
        # Logaritmo del monto
        df['TransactionAmt_log'] = np.log1p(df['TransactionAmt'])
        
        # Hora simulada
        if 'TransactionDT' in df.columns:
            max_dt = df['TransactionDT'].max()
            df['hour_sim'] = (df['TransactionDT'] / max_dt * 24).astype(int)
        
        # Interacciones simples
        if 'TransactionAmt' in df.columns and 'card1' in df.columns:
            df['amt_card_interaction'] = (
                df['TransactionAmt'] * df['card1'].astype(float)
            )
        
        print(f"   Características nuevas creadas: 3")
        print(f"   Shape final: {df.shape}")
        
        return df
    
    def encode_categorical(self, df, fit=True):
        """
        Codificar variables categóricas con LabelEncoder.
        
        Args:
            df: DataFrame a codificar
            fit: Si es True, entrena los encoders; si es False, los aplica
            
        Returns:
            DataFrame con variables codificadas
        """
        df = df.copy()
        
        for col in self.categorical_cols:
            if col not in df.columns:
                continue
                
            if fit:
                le = LabelEncoder()
                df[col] = le.fit_transform(df[col].astype(str))
                self.label_encoders[col] = le
            else:
                if col in self.label_encoders:
                    le = self.label_encoders[col]
                    # Manejar categorías desconocidas
                    df[col] = df[col].astype(str).map(
                        lambda x: le.transform([x])[0]
                        if x in le.classes_ else -1
                    )
        
        return df
    
    def prepare_data(self, df):
        """
        Pipeline completo de preparación.
        
        Args:
            df: DataFrame bruto
            
        Returns:
            Tuplas (X_train, X_test, y_train, y_test)
        """
        # Preparar features y target
        X = df.drop(['TransactionID', 'isFraud'], axis=1)
        y = df['isFraud']
        
        # División train/test con estratificación
        print(f"\n📊 División train/test:")
        X_train, X_test, y_train, y_test = train_test_split(
            X, y,
            test_size=self.test_size,
            stratify=y,
            random_state=self.random_state
        )
        
        print(f"   Train: {X_train.shape[0]} muestras")
        print(f"   Test: {X_test.shape[0]} muestras")
        print(f"   Fraude en train: {y_train.mean():.4%}")
        print(f"   Fraude en test: {y_test.mean():.4%}")
        
        # Aplicar SMOTE si es necesario
        if self.use_smote:
            print(f"\n⚖️ Aplicando SMOTE para balanceo...")
            smote = SMOTE(random_state=self.random_state)
            X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
            print(f"   Antes: {len(y_train)} muestras - Fraude: {y_train.mean():.4%}")
            print(f"   Después: {len(y_train_res)} muestras - Fraude: {y_train_res.mean():.4%}")
            X_train, y_train = X_train_res, y_train_res
        
        # Escalar características
        print(f"\n📐 Escalando características...")
        X_train = self.scaler.fit_transform(X_train)
        X_test = self.scaler.transform(X_test)
        
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        
        return X_train, X_test, y_train, y_test
    
    def save_scaler(self, path):
        """Guardar el scaler entrenado."""
        joblib.dump(self.scaler, path)
        print(f"✅ Scaler guardado en {path}")
    
    def load_scaler(self, path):
        """Cargar el scaler entrenado."""
        self.scaler = joblib.load(path)
        print(f"✅ Scaler cargado desde {path}")
