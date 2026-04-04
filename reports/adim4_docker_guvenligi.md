# 🐳 Adım 4: Docker & Container Security

**Hedef:** Konteyner izolasyon seviyesinin denetimi.

### 🔍 Bulgular:
* **İzolasyon:** Uptime Kuma, Host Kernel'ini ortak kullanmaktadır. `Dockerfile` içerisinde `USER` tanımlanmadığı için işlemler varsayılan olarak **root** yetkisiyle çalışmaktadır.
* **Hacim Güvenliği (Volume):** `docker-compose.yml` dosyasındaki `./data:/app/data` eşlemesi, host sistemdeki dosyaların konteyner içinden manipüle edilmesine (Path Traversal) açıktır.

### 🛑 Risk:** "Container Escape" zafiyeti ile saldırgan konteynerden çıkarak ana makine (Host OS) üzerinde yetki yükseltebilir.
