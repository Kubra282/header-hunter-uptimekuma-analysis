# 🛡️ Adım 1: Uptime Kuma Kurulum ve install.sh Statik Analizi

**Görev:** Yazılımın sisteme giriş yolunun (install script) tersine mühendislik yöntemleriyle incelenmesi ve siber güvenlik zafiyetlerinin tespiti.

---

### 🔍 1. Kurulum Metodolojisi: "curl | bash" Analizi
Uptime Kuma'nın resmi kurulum yöntemi incelendiğinde, terminal üzerinden şu komutun kullanıldığı görülmüştür:
`curl -sL https://git.io/uptime-kuma-install | bash`

* **Teknik Tespit:** Bu yöntem, uzak sunucudaki bir scripti (betiği) doğrudan sistemin komut satırına (bash) yönlendirir.
* **Güvenlik Riski:** Bu işlem "körü körüne güven" modelidir. Aradaki bağlantı (MITM saldırısı) manipüle edilirse, sistem fark etmeden zararlı kodları çalıştırabilir.

---

### 📂 2. Dizin Yapısı ve Yetki Talepleri
Kurulum scripti (`install.sh`) statik olarak analiz edildiğinde şu bulgulara ulaşılmıştır:

* **Dizin Oluşturma:** Script, `mkdir -p /opt/uptime-kuma` komutunu kullanarak sistemin kök dizininde (root) kalıcı bir alan açar.
* **Yetki Seviyesi:** Bu işlemlerin yapılabilmesi için kullanıcıdan yüksek yönetici yetkisi (**sudo**) talep edilmektedir.

---

### 🛑 3. Kritik Güvenlik Zafiyeti: Hash (İmza) Kontrolü
Hocanın sorduğu en kritik soru olan "Paket bütünlüğü doğrulanıyor mu?" sorusunun cevabı analiz edilmiştir:

* **Tespit:** Script içerisinde, dış kaynaktan indirilen paketlerin **SHA-256 Hash değerlerini** veya dijital imzalarını kontrol eden herhangi bir mekanizma **tespit edilememiştir.**
* **Risk:** Yazılım, indirdiği dosyaların "orijinal" olup olmadığını teyit etmez. Bu durum, siber güvenlik dünyasında ciddi bir "Tedarik Zinciri Saldırısı" (Supply Chain Attack) riskidir.

---

### ✅ Güvenlik Önerisi
Tam güvenli bir kurulum için script içerisine, indirilen `.tar.gz` dosyasının Hash değerini önceden tanımlanmış güvenli bir değerle karşılaştıran bir `if-else` bloğu eklenmelidir.