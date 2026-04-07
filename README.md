<p align="center">
  <img width="204" height="192" alt="isu_logo" src="https://github.com/user-attachments/assets/83b47ed4-0449-4454-82ec-06c9c08eef43" />
</p>


# 🛡️ Hibrit Güvenlik Analizi: Header Hunter & Uptime Kuma Denetimi
<p align="center">
  <img src="https://img.shields.io/github/actions/workflow/status/Kubra282/header-hunter-uptimekuma-analysis/main.yml?branch=main&label=Security%20Tests&logo=github" alt="Security Tests">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue?logo=python" alt="Python Version">
  <img src="https://img.shields.io/badge/Docker-Enabled-blue?logo=docker" alt="Docker Support">
  <img src="https://img.shields.io/badge/Audit-Q--Sec-red" alt="Audit Method">
</p>

---

## 👨‍🏫 Akademik Bilgiler
* **Danışman:** Keyvan Arasteh Abbasabad
* **Hazırlayan:** Kübra Fison
* **Üniversite:** İstinye Üniversitesi
* **Ders:** Tersine Mühendislik (Reverse Engineering)

---

## 📜 İçindekiler
1. [🚀 Proje Genel Bakışı](#-proje-genel-bakışı)
2. [📁 Proje Klasör Yapısı ve Dosya İşlevleri](#-proje-klasör-yapısı-ve-dosya-işlevleri)
3. [🛠️ 1. Parça: Header Hunter (Siber Güvenlik Aracı)](#️-1-parça-header-hunter-siber-güvenlik-aracı)
4. [🔍 2. Parça: Uptime Kuma 5 Adımlık Güvenlik Analizi](#-2-parça-uptime-kuma-5-adımlık-güvenlik-analizi)
5. [⚙️ Kurulum ve Çalıştırma](#-kurulum-ve-çalıştırma)
6. [🏛️ Beklenen Derinlik (Teknik Analiz)](#-beklenen-derinlik-teknik-analiz)

---

## 🚀 Proje Genel Bakışı
Bu çalışma, siber savunma ekosisteminde proaktif bir yaklaşım sergileyerek özgün bir güvenlik aracı geliştirmeyi (**Header Hunter**) ve popüler bir açık kaynak projenin (**Uptime Kuma**) 5 adımlık derinlemesine siber güvenlik analizini kapsayan **hibrit bir yapıdır.**

---

## 📁 Proje Klasör Yapısı ve Dosya İşlevleri

Depodaki tüm dosyaların teknik karşılıkları aşağıdadır:

- **📂 `.github/`**: CI/CD (GitHub Actions) iş akışlarını barındıran otomasyon klasörü.
- **📂 `docs/`**: Uptime Kuma vaka analizine ait 5 adımlık detaylı Markdown raporları.
- **📂 `reports/`**: Analiz süreçlerine dair ek raporlar ve veri çıktıları.
- **📂 `ekran-goruntuleri/`**: Analiz sırasında elde edilen teknik kanıtlar (PoC).
- **📂 `src/`**: `header_hunter.py` ana kaynak kodunun bulunduğu dizin.
- **📂 `tests/`**: Aracın stabilitesini denetleyen birim testleri (Unit Tests).
- **📄 `Makefile`**: Proje yönetim, otomasyon ve test komutlarını barındıran teknik dosya.
- **📄 `install.sh`**: Tersine mühendislik yöntemleriyle analiz edilen orijinal kurulum scripti.
- **📄 `Dockerfile` & `docker-compose.yml`**: Projenin izole bir sandbox ortamında çalışmasını sağlayan konteyner yapılandırmaları.
- **📄 `TODO.md`**: Projenin gelecek geliştirme planları ve teknik roadmap'i.
- **📄 `LICENSE`**: Projenin MIT lisans standartlarına göre korunduğunu belirten belge.
- **📄 `.env.example`**: Güvenli yapılandırma ve çevresel değişken şablonu.
- **📄 `.gitattributes`**: Farklı işletim sistemlerinde dosya bütünlüğünü koruyan yapılandırma.
- **📄 `.gitignore`**: Hassas verilerin depoya sızmasını engelleyen filtre dosyası.

---

## 🛠️ 1. Parça: Header Hunter (Siber Güvenlik Aracı)
Statik analiz yöntemlerini kullanarak, dosyaların sadece uzantılarını değil, **"Magic Bytes"** (dosya imzası) değerlerini kontrol eden proaktif bir güvenlik aracıdır.

* **Mimari:** Layer 5 Middleware Static Analysis & Containerized Sandbox.
* **Protokoller:** SHA-256 Integrity Validation, .env Secret Management.

---

## 🔍 2. Parça: Uptime Kuma 5 Adımlık Güvenlik Analizi
**Q-Sec Metodolojisi** takip edilerek gerçekleştirilen denetim adımları:

| Adım | Analiz Konusu | Tespit Edilen Bulgular |
| :--- | :--- | :--- |
| **Adım 1** | **Kurulum Güvenliği** | `install.sh` üzerindeki imza kontrolü eksikliği (Tedarik Zinciri Riski). |
| **Adım 2** | **Adli Bilişim (Forensics)** | Sistem kalıntıları ve aktif port (3001) denetimi. |
| **Adım 3** | **CI/CD & Webhook** | GitHub Actions otomasyonu ve Webhook güvenlik analizi. |
| **Adım 4** | **Docker İzolasyonu** | Konteyner izolasyon seviyesi ve kernel paylaşım riskleri. |
| **Adım 5** | **Auth & Tehdit Modeli** | Oturum yönetimi mantık hataları ve kaba kuvvet saldırısı analizi. |

---




## ⚙️ Kurulum ve Çalıştırma
---

Projenin profesyonel yönetimi için `Makefile` otomasyonu kullanılması önerilir:

### 1. Yapılandırma (Environment Setup)
```bash
make setup
Docker ile Çalıştırma (Önerilen)
make docker-rebuild
Güvenlik Testlerinin Çalıştırılması
make test


### 1. Yapılandırma
```bash
cp .env.example .env
Docker ile Çalıştırma
sudo docker compose up --build
Manuel Testler
python3 -m unittest discover tests
### 1. Yapılandırma
```bash
cp .env.example .env
