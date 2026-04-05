FROM python:3.9-slim

WORKDIR /app

# Gerekli kütüphaneleri yükle (Hocanın en sevdiği kısım)
RUN pip install python-dotenv

# Tüm dosyaları kopyala
COPY . .

# Uygulamayı çalıştır
CMD ["python3", "src/header_hunter.py"]
