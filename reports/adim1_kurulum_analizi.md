# 🛡️ Adım 1: Statik Analiz (Kurulum Scripti)

**Hedef:** `install.sh` dosyasının güvenlik denetimi.

### 🔍 Bulgular:
* **Zafiyet:** Script içerisinde `curl -L ... | tar xz` komutu kullanılarak paket çekilmektedir.
* **Kritik Eksiklik:** İndirilen paketlerin bütünlüğü (Integrity) için **SHA-256 Checksum** kontrolü yapılmamaktadır.
* **Risk:** Saldırgan, DNS Spoofing veya MITM saldırısı ile paketi manipüle ederek sisteme zararlı kod (Backdoor) enjekte edebilir.

### 🛠️ Öneri:
Paket indirme aşamasından sonra `sha256sum -c` komutu ile dosya doğrulaması zorunlu tutulmalıdır.
