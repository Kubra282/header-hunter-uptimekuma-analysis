# Sentinel-H: Professional Security Tool Management (Venv Supported)
# Student: Kübra Fison | Instructor: Keyvan Arasteh Abbasabad

.PHONY: setup run test clean

# 1. Sanal ortamı kur ve bağımlılıkları yükle
setup:
	cp .env.example .env
	python3 -m venv venv
	./venv/bin/pip install -r requirements.txt
	@echo "Kurulum tamamlandı. Kullanmak için: source venv/bin/activate"

# 2. Aracı sanal ortam üzerinden çalıştır
run:
	./venv/bin/python3 src/header_hunter.py

# 3. Güvenlik testlerini sanal ortam üzerinden başlat
test:
	./venv/bin/python3 -m unittest discover tests

# 4. Temizlik (Forensics Cleanup)
clean:
	rm -rf venv
	rm -rf __pycache__
	find . -type d -name "__pycache__" -exec rm -rf {} +
	@echo "Sanal ortam ve kalıntılar temizlendi."
