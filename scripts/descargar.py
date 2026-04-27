import kagglehub

print("Descargando datos...")
path = kagglehub.competition_download('ieee-fraud-detection')
print(f"Archivos descargados en: {path}")
