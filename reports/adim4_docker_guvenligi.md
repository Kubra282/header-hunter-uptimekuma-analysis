# 🐳 Adım 4: Docker Mimarisi ve İzolasyon Güvenliği

**Görev:** Uptime Kuma'nın Docker üzerindeki çalışma prensiplerini ve izolasyon seviyesini (Container Escape riskleri) analiz etmek.

---

### 🏗️ 1. Mimari İnceleme: Container vs. VM
Uptime Kuma, Docker üzerinde çalıştığında ana işletim sisteminin (Host OS) kernel'ini ortak kullanır. 
* **Tespit:** Slayt 7'de belirtilen mimariye göre; Docker'da bir "Guest OS" (Misafir İşletim Sistemi) yoktur. Bu durum yazılımı hafif yapar ancak izolasyonu zayıflatır.

### 🛑 2. Kritik Zafiyet: Privileged Mode ve Root Yetkisi
* **Analiz:** Uptime Kuma'nın Docker imajı varsayılan olarak "root" yetkileriyle çalışmaya meyillidir. 
* **Risk (Container Breakout):** Eğer Uptime Kuma üzerinde bir açık bulunursa, saldırgan Docker içinden "kaçarak" (Escape) senin ana bilgisayarının (Host) tüm yetkilerini ele geçirebilir. 

### 📂 3. Volume Mapping (Veri Kalıcılığı)
* **İnceleme:** Yazılım veritabanını dışarıya aktarmak için `-v /app/data:/app/data` gibi bir eşleme yapar.
* **Güvenlik Yorumu:** Veritabanının host sistemde açıkta durması, konteyner hacklenmese bile fiziksel erişimi olan birinin tüm izleme verilerini çalmasına olanak tanır.