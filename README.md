# 🛡️ Tersine Mühendislik Vize Projesi: Hibrit Güvenlik Analizi ve Araç Geliştirme

**Öğrenci Bilgileri:**
* **Ad Soyad:** Kübra Fison
* **Üniversite:** İstinye Üniversitesi
* **Bölüm:** Bilişim Güvenliği Teknolojisi
* **Ders:** Tersine Mühendislik (Vize projesi)

---

## 🎯 Proje Amacı
Bu çalışma, "Gerçek Dünya Açık Kaynak Repo Analizi" kapsamında **Uptime Kuma** projesinin siber güvenlik denetimini ve "Standart Senaryolar" kapsamında dosya bütünlüğü doğrulayan **Header Hunter** aracının geliştirilmesini hedeflemektedir.

---

## 🛠️ BÖLÜM 1: Uptime Kuma Açık Kaynak Repo Analizi (5 Kritik Adım)

Hocanın belirlediği 5 aşamalı tersine mühendislik ve güvenlik metodolojisi çerçevesinde hazırlanan analiz planı:

### 1. Adım: Kurulum ve install.sh Analizi
* **Görev:** Yazılımın kurulum betiği (`install.sh`) incelenerek sistem dizinleri, talep edilen yetkiler ve paket kaynakları analiz edilecektir.
* **Kritik Analiz:** Paketlerin indirilme sürecinde Hash (imza) kontrolü yapılıp yapılmadığı ve `curl | bash` yönteminin barındırdığı Man-in-the-Middle riskleri teknik olarak raporlanacaktır.

### 2. Adım: İzolasyon ve Forensics (İz Bırakmadan Temizlik)
* **Görev:** Yazılım kaldırıldıktan sonra portların durumu, arka plan servisleri ve gizli log kalıntıları incelenecektir.
* **İspat Yöntemi:** Tam temizlik ispatı için Sanal Makine (VM) üzerinde kurulum öncesi ve sonrası sistem snapshot karşılaştırması yapılacaktır.

### 3. Adım: CI/CD Paketleri ve Webhook Analizi
* **Görev:** `.github/workflows` dizini altındaki otomasyon akışları ve Webhook mekanizması incelenecektir.
* **Kritik Soru Yanıtı:** Webhook'un bildirim güvenliği ve bu projenin otomasyon hattındaki (CI/CD) kritik rolü belgelenecektir.

### 4. Adım: Docker Mimarisi ve Konteyner Güvenliği
* **Görev:** `docker-compose.yml` ve Docker imaj katmanları analiz edilecektir.
* **İnceleme:** Konteyner izolasyonu, yetki sınırları ve Docker ortamının Kubernetes/VM ile güvenlik farkları analiz edilecektir.

### 5. Adım: Kaynak Kod ve Auth (Giriş) Analizi
* **Görev:** Uygulamanın giriş noktası (entrypoint) ve kimlik doğrulama (JWT/Session) mekanizması analiz edilecektir.
* **Threat Modeling:** Bir saldırganın auth mekanizmasına (Brute Force, Session Hijacking vb.) dışarıdan saldırı senaryoları simüle edilecektir.

---

## 🛡️ BÖLÜM 2: Header Hunter (Dosya İmzası Analiz Aracı)

Tersine mühendisliğin temel taşlarından olan **Magic Byte (Sihirli Bayt)** analizine dayalı teknik bir araç geliştirilmiştir.

* **Hedef:** Uzantısı manipüle edilmiş (örn: `.jpg` görünümlü bir `.exe`) zararlı dosyaların gerçek türünü tespit etmek.
* **Teknik Detay:** Yazılım, dosyanın ilk baytlarındaki Hex değerlerini (Magic Numbers) okuyarak kimlik doğrulaması yapar.

### Desteklenen Bazı Dosya İmzaları:
- **PE (Windows EXE):** `4D 5A`
- **ELF (Linux Binary):** `7F 45 4C 46`
- **PNG:** `89 50 4E 47`
- **PDF:** `25 50 44 46`

### Kullanılan Araçlar:
- **Analiz:** HxD Hex Editor, Burp Suite
- **Geliştirme:** Python CLI (Command Line Interface)
- **Ortam:** VS Code & Windows Terminal

---

## 🚀 Kullanım
Geliştirilen aracı test etmek için terminal üzerinden aşağıdaki komutu kullanabilirsiniz:

```bash
python header_hunter.py <dosya_yolu>
