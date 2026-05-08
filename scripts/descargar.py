import kagglehub
import shutil
from pathlib import Path

# Crear la carpeta data/raw si no existe
RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

try:
    print("🔑 Conectando a Kaggle...")
    print("📥 Descargando dataset 'ieee-fraud-detection'...")
    download_path = kagglehub.competition_download('ieee-fraud-detection')
    print(f"✅ Archivos descargados en: {download_path}")

    # Buscar archivos CSV dentro de la carpeta descargada
    csv_files = list(Path(download_path).glob("*.csv"))

    if not csv_files:
        print("⚠️ No se encontraron archivos CSV en la descarga.")
    else:
        for csv_file in csv_files:
            destino = RAW_DIR / csv_file.name
            shutil.copy2(csv_file, destino)  # copia preservando metadatos
            print(f"📁 Copiado: {csv_file.name} -> {destino}")

        print(f"\n✅ Datos listos en la carpeta '{RAW_DIR}/'")
        print("Archivos disponibles:")
        for f in RAW_DIR.glob("*.csv"):
            print(f"   - {f.name} ({f.stat().st_size / 1e6:.1f} MB)")

except kagglehub.exceptions.UnauthenticatedError:
    print("\n❌ Error: No estás autenticado en Kaggle.")
    print("Solución:")
    print("1. Ve a https://www.kaggle.com -> Settings -> API -> Create New API Token")
    print("2. Descarga 'kaggle.json' y súbelo a tu Codespace en ~/.kaggle/")
    print("3. Ejecuta: mkdir -p ~/.kaggle && mv kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json")
    print("4. Vuelve a ejecutar este script.")
except Exception as e:
    print(f"❌ Error inesperado: {e}")