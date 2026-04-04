# 🕵️ Adım 2: Network & Digital Forensics

**Hedef:** Uygulamanın çalışma anındaki ağ izleri ve sistemde bıraktığı kalıntılar.

### 🔍 Bulgular:
* **Port Denetimi:** `netstat -ano` komutu ile yapılan incelemede, uygulamanın varsayılan **3001** portunu dinlediği teyit edilmiştir.
* **Adli Kalıntı:** Uygulama silinse dahi `/app/data/kuma.db` (SQLite) veritabanı sistemde kalmaktadır.
* **Veri Gizliliği:** Bu veritabanı şifrelenmemiş durumdadır; fiziksel erişimi olan bir saldırgan tüm izleme verilerini (Monitoring Logs) ele geçirebilir.

### 🧪 Kanıt:
Terminal çıktısında 3001 portu aktif olarak gözlemlenmiştir.
