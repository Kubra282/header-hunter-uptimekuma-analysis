import os
from dotenv import load_dotenv

# .env dosyasındaki ayarları yükle
load_dotenv()

# Artık klasör yolunu elle yazmak yerine buradan alıyoruz
# Eğer .env'de yoksa varsayılan olarak './data' klasörüne bakar
SCAN_PATH = os.getenv("SCAN_PATH", "./data")

print(f"--- Tarama Başlatılıyor: {SCAN_PATH} ---")
