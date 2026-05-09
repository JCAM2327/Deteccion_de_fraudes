"""Tests para el módulo de preprocesamiento."""
import pandas as pd
import numpy as np
from src.preprocessing import DataProcessor

def test_dataprocessor_initialization():
    """Probar que el procesador se inicializa correctamente."""
    dp = DataProcessor(test_size=0.3, random_state=123, use_smote=False)
    assert dp.test_size == 0.3
    assert dp.random_state == 123
    assert dp.use_smote is False

def test_select_important_columns():
    """Probar selección de columnas en un DataFrame pequeño simulado."""
    # Simular columnas típicas
    data = {
        'TransactionID': [1,2],
        'isFraud': [0,1],
        'TransactionAmt': [100, 200],
        'card1': [111,222],
        'ExtraCol': [5,6]  # columna extra que debe eliminarse
    }
    df = pd.DataFrame(data)
    dp = DataProcessor()
    df_sel = dp.select_important_columns(df)
    # Verificar que se conservan las columnas esperadas y se eliminan otras
    assert 'TransactionAmt' in df_sel.columns
    assert 'card1' in df_sel.columns
    assert 'ExtraCol' not in df_sel.columns

def test_handle_missing_values():
    """Probar imputación de nulos."""
    df = pd.DataFrame({
        'num1': [1, 2, np.nan],
        'num2': [np.nan, np.nan, np.nan],  # será eliminada por >80% nulos? 100% >80%
        'cat1': ['a', np.nan, 'b'],
        'isFraud': [0,0,1],
        'TransactionID': [101,102,103]
    })
    dp = DataProcessor()
    df_clean = dp.handle_missing_values(df)
    # Columna 'num2' debería haberse eliminado (>80% nulos)
    assert 'num2' not in df_clean.columns
    # Los nulos de num1 deben imputarse con -999
    assert df_clean['num1'].iloc[2] == -999
    # Los nulos de cat1 deben imputarse con 'Unknown'
    assert df_clean['cat1'].iloc[1] == 'Unknown'

def test_feature_engineering():
    """Probar creación de nuevas features."""
    df = pd.DataFrame({
        'TransactionAmt': [100, 1000, 5000],
        'TransactionDT': [0, 500000, 1000000],
        'card1': [123, 456, 789],
        'isFraud': [0,0,1],
        'TransactionID': [1,2,3]
    })
    dp = DataProcessor()
    df_fe = dp.feature_engineering(df)
    # Se deben crear las tres nuevas columnas
    assert 'TransactionAmt_log' in df_fe.columns
    assert 'hour_sim' in df_fe.columns
    assert 'amt_card_interaction' in df_fe.columns
    # Verificar log aproximado
    assert df_fe['TransactionAmt_log'].iloc[0] == np.log1p(100)