# 📋 Sentinel-H: Geliştirme ve Analiz Yol Haritası (Roadmap)

Bu dosya, **Header Hunter** aracının teknik gelişimi ve **Uptime Kuma** güvenlik analizinin gelecekteki derinleştirme adımlarını içermektedir. Projenin "Sistem Mimarı" perspektifiyle sürdürülebilirliği için planlanan görevler aşağıdadır.

---

## 🛠️ 1. Header Hunter: Teknik Geliştirmeler
*Hedef: Statik analiz aracını bir "Malware Röntgen" cihazına dönüştürmek.*

- [ ] **ELF/PE Header Analizi:** Sadece Magic Bytes değil, dosyanın `Entry Point` (Giriş Noktası) ve `Section` bilgilerini okuyacak modülün eklenmesi.
- [ ] **Kütüphane Tespiti:** Dosyanın içindeki `Import Table` (İçe Aktarma Tablosu) üzerinden hangi dış kütüphaneleri (.dll/.so) çağırdığının raporlanması.
- [ ] **Recursive Scan:** Belirli bir dizindeki binlerce dosyanın asenkron olarak taranması ve şüpheli olanların karantinaya alınması.
- [ ] **JSON Export:** Analiz sonuçlarının SIEM sistemlerine (Wazuh, Splunk) entegre edilebilmesi için JSON çıktısı desteği.

---

## 🔍 2. Uptime Kuma Güvenlik Denetimi (5 Adım Planı)
*Hedef: Mevcut analiz bulgularını teknik kanıtlarla derinleştirmek.*

### Adım 1: Reverse Engineering & Setup
- [ ] `install.sh` içerisindeki paket çekme komutlarına (curl/wget) otomatik SHA256 doğrulama katmanı ekleyen bir "Patch" scripti yazılması.

### Adım 2: Forensics & Cleanup
- [ ] **Post-Uninstall Forensic Sweep:** Yazılım kaldırıldıktan sonra `/var/lib/docker` ve `/tmp` dizinlerinde kalan artıkların otomatik tespiti için bir Bash scripti geliştirilmesi.
- [ ] Açık kalan portların (3001) otomatik kapatılma kontrolünün otomatize edilmesi.

### Adım 3: CI/CD Pipeline
- [ ] **Webhook Security:** Webhook üzerinden gelen bildirimlerin "Secret Token" ile doğrulanması mekanizmasının test edilmesi.
- [ ] GitHub Actions üzerinde `Gitleaks` kullanarak kaynak kodda unutulmuş API anahtarlarının taranması.

### Adım 4: Docker & Container Security
- [ ] **Rootless Container:** Uptime Kuma imajının `root` yetkisi olmadan (Non-root user) çalıştırılması için Dockerfile optimizasyonu.
- [ ] **Seccomp/AppArmor:** Konteynerin sistem çağrılarını kısıtlayan güvenlik profillerinin oluşturulması.

### Adım 5: Threat Modeling (Auth Analysis)
- [ ] **Brute-Force Protection:** Login ekranına "Rate Limiting" (İstek Sınırlama) özelliğinin kaynak kod seviyesinde entegre edilmesi.
- [ ] JWT/Session tokenlarının yaşam süresi ve güvenli flag (HttpOnly/Secure) analizlerinin tamamlanması.

---

## 🚀 3. Genel Proje Yönetimi
- [ ] **GitHub Badges:** README dosyasına "Build Status", "Test Coverage" ve "License" badgelerinin eklenmesi.
- [ ] **İstinye Logosu:** Kurumsal raporlama için dokümantasyonun PDF versiyonuna üniversite logosu ve ders künyesinin eklenmesi.
- [ ] **Wiki:** /knowledge-base benzeri bir teknik dokümantasyonun GitHub Wiki üzerinde oluşturulması.

---
*Bu liste, projenin "Üretim (Production)" ortamına geçişi ve akademik derinliği için dinamik olarak güncellenmektedir.*
