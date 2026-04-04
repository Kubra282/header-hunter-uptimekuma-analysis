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

## 📁 GitHub Proje Yapısı (Klasör Mimarisi)

Proje, kurumsal yazılım standartlarına uygun olarak organize edilmiştir:

* 📂 **`src/`**: `header_hunter.py` ana kaynak kodu.
* 📂 **`tests/`**: Kodun doğruluğunu denetleyen `test_header_hunter.py` birim testleri.
* 📂 **`reports/`**: 5 Adımlık detaylı analiz raporları (.md dosyaları).
* 📂 **`dashboard/`**: Analiz sonuçlarını görselleştiren HTML/CSS tabanlı panel.
* 📂 **`ekran-goruntuleri/`**: Analiz sırasında alınan teknik kanıtlar ve ekran çıktıları.
* 📄 **`.env.example`**: Proje yapılandırma şablonu.
* 🐳 **`Dockerfile` & `docker-compose.yml`**: Docker yapılandırması.

---

## ⚙️ Kurulum ve Çalıştırma

### Docker ile Çalıştırma (Önerilen)
1. `.env.example` dosyasını `.env` olarak kopyalayın.
2. Komutu çalıştırın:
```bash
docker-compose up --build

3.python3 -m unittest discover tests

---
