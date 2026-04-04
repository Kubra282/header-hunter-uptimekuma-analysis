FROM python:3.9-slim

WORKDIR /app

# Gerekli dosyaları kopyala
COPY src/ /app/src/
COPY tests/ /app/tests/
COPY .env.example /app/.env

# Gerekli kütüphaneyi yükle (dotenv desteği için)
RUN pip install python-dotenv

# Aracı çalıştır
CMD ["python3", "src/header_hunter.py"]
