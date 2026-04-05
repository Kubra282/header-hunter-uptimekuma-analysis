# 🛡️ Hibrit Güvenlik Analizi: Header Hunter & Uptime Kuma Denetimi

Bu proje, **İstinye Üniversitesi - Bilişim Güvenliği Teknolojisi** programı **Tersine Mühendislik** dersi vize ödevi kapsamında geliştirilmiştir. Proje, hem özgün bir güvenlik aracı geliştirmeyi hem de popüler bir açık kaynak projenin (Uptime Kuma) derinlemesine siber güvenlik analizini içeren **hibrit bir yapıya** sahiptir.

**Hazırlayan:** Kübra Fison  
**Okul:** İstinye Üniversitesi  
**Ders:** Tersine Mühendislik (Reverse Engineering)

---

## 🚀 Proje Genel Bakışı

Proje iki ana sütun üzerine inşa edilmiştir:

1.  **Geliştirilen Araç (Header Hunter):** Statik analiz yöntemlerini kullanarak, dosyaların sadece uzantılarını değil, "Magic Bytes" (dosya imzası) değerlerini kontrol eden bir Python aracıdır.
2.  **Vaka Analizi (Uptime Kuma):** Q-Sec metodolojisi (Slide 2-10) takip edilerek, Uptime Kuma yazılımının kurulumundan Docker izolasyonuna kadar 5 kritik adımda gerçekleştirilen güvenlik denetimidir.

---

## 🛠️ 1. Parça: Header Hunter (Siber Güvenlik Aracı)

`header_hunter.py`, bir siber saldırganın dosya uzantılarını değiştirerek (örneğin zararlı bir `.exe` dosyasını `.txt` yaparak) sistemi yanıltmasını engeller.

* **Çalışma Mantığı:** Dosyanın ilk birkaç baytını okur (Örn: PDF için `%PDF` veya `25 50 44 46`) ve beyan edilen uzantı ile gerçek imzanın uyuşup uyuşmadığını denetler.
* **Teknik Altyapı:** Python 3.x ve `python-dotenv` kütüphanesi kullanılmıştır.
* **Yapılandırma:** Tarama dizini gibi ayarlar dinamik olarak `.env` dosyasından okunur.

---

## 🔍 2. Parça: Uptime Kuma 5 Adımlık Güvenlik Analizi

Hocanın paylaştığı **Q-Sec Vaka Analizi** kriterlerine göre gerçekleştirilen denetim adımları:

| Adım | Analiz Konusu | Tespit Edilen Bulgular |
| :--- | :--- | :--- |
| **Adım 1** | **Kurulum Güvenliği** | `install.sh` dosyasında paketlerin SHA256 hash kontrolü yapılmadan indirilmesi (Tedarik Zinciri Riski). |
| **Adım 2** | **Adli Bilişim (Forensics)** | Sistemde aktif portların (3001) ve `kuma.db` veritabanı kalıntılarının analizi. |
| **Adım 3** | **CI/CD & Webhook** | GitHub Actions ve dış bildirim kanallarındaki (Webhook) otomasyon güvenliği. |
| **Adım 4** | **Docker İzolasyonu** | Konteyner yapısının kernel paylaşımı ve "Container Escape" risklerine karşı denetimi. |
| **Adım 5** | **Auth & Tehdit Modeli** | Giriş mekanizmasındaki mantıksal hatalar (Slide 9) ve kaba kuvvet saldırısı riskleri. |

---
## 📁 Proje Klasör Yapısı ve Dosyalar

Şu anki depo yapısı ve dosyaların işlevleri aşağıdadır:

* 📂 **`src/`**: `header_hunter.py` ana kaynak kodunun bulunduğu klasör.
* 📂 **`tests/`**: Kodun doğruluğunu denetleyen birim testleri içerir.
* 📂 **`reports/`**: Uptime Kuma vaka analizine ait 5 adımlık detaylı raporlar.
* 📂 **`ekran-goruntuleri/`**: Analiz sırasında alınan teknik kanıtlar ve ekran çıktıları.
* 📄 **`header_hunter.py`**: Aracın ana çalışma dosyası (Root erişimi için).
* 📄 **`install.sh`**: Tersine mühendislik yöntemleriyle analiz edilen orijinal kurulum scripti.
* 📄 **`.env.example`**: Proje yapılandırma ve çevre değişkenleri şablonu.
* 📄 **`.gitignore`**: GitHub'a yüklenmeyecek (gizli veya gereksiz) dosyaların listesi.
* 🐳 **`Dockerfile` & `docker-compose.yml`**: Projenin izole bir Docker konteynerinde çalıştırılmasını sağlayan yapılandırmalar.
* Bu proje versiyon kontrol prensiplerine uygun olarak geliştirilmiştir.
---

## ⚙️ Kurulum ve Çalıştırma

Projenin sorunsuz çalışması için terminalde proje klasöründe olduğunuzdan emin olun.

### 1. Yapılandırma (Environment Setup)
Hassas verilerin yönetimi için örnek yapılandırmayı kopyalayın:
```bash
cp .env.example .env

Docker ile Çalıştırma (Önerilen)
sudo docker compose up --build

Manuel Testlerin Çalıştırılması
python3 -m unittest discover tests
