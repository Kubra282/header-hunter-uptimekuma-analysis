# 🕵️ Adım 2: İzolasyon ve Forensics (İz Analizi) Raporu

**Görev:** Uptime Kuma yazılımı sistemden kaldırıldıktan sonra geride bıraktığı dijital izlerin (kalıntıların) siber güvenlik açısından incelenmesi.

---

### 🔍 1. Port ve Ağ Analizi (Network Forensics)
Yazılımın dış dünya ile iletişim kurduğu **3001** portunun, kaldırma işlemi sonrası durumu test edilmiştir.

* **Uygulanan Komut:** `netstat -ano | findstr :3001`
* **Tespit:** Komut sonucunda hiçbir çıktı alınmamıştır.
* **Güvenlik Yorumu:** Yazılımın ağ soketlerini başarıyla kapattığı ve sistemde açık bir "arka kapı" (backdoor) bırakmadığı doğrulanmıştır.
* **bu adımda terminalde netstat komutunu çalıştırdım ve 3001 portunun kapalı olduğunu teyit ettim. Ekran görüntüsü aşağıdadır:"
![Port Kontrolü](.https://github.com/Kubra282/header-hunter-uptimekuma-analysis/blob/main/ekran-goruntuleri/WhatsApp%20Image%202026-03-26%20at%2023.26.55.jpeg)
---

### 📂 2. Dosya Sistemi ve Veritabanı Kalıntıları
Yazılım dosyaları silinse bile, kullanıcı verilerinin sistemde kalıp kalmadığı denetlenmiştir.

* **İnceleme Noktası:** `/opt/uptime-kuma` veya `%AppData%/uptime-kuma`
* **Kritik Bulgu:** Yazılım kaldırıldıktan sonra SQLite veritabanı dosyasının (`kuma.db`) ve log kayıtlarının silinmediği görülmüştür.
* **Risk:** Bu durum, sistem üzerinde fiziksel erişimi olan bir saldırganın, eski kullanıcı verilerine ve izleme geçmişine ulaşmasına (Information Disclosure) neden olabilir.

---

### 🛠️ 3. Adli Bilişim (Forensics) Önerisi
Tam izolasyon sağlamak için "Kaldırma (Uninstall)" scriptine şu adımlar eklenmelidir:
1.  Veritabanı dosyalarının (`.db`) kalıcı olarak silinmesi (Wipe).
2.  Sistem servis kayıtlarının (systemd/services) temizlenmesi.
