# 🕵️ Adım 5: Threat Modeling (Tehdit Modelleme) ve Auth Analizi

**Görev:** Yazılımın giriş (Authentication) mekanizmasındaki mantıksal hataları ve potansiyel sızma noktalarını belirlemek.

---

### 🔑 1. Kimlik Doğrulama (Auth) Analizi
* **Tespit:** Uptime Kuma giriş ekranında "Brute Force" (Kaba Kuvvet) saldırılarına karşı varsayılan olarak bir kısıtlama (Rate Limiting) çok zayıf seviyededir.
* **Mantıksal Hata:** Slayt 9'daki `TODO` örneğinde olduğu gibi, oturum yönetimi (Session Management) sırasında token'ların süresi dolsa bile bazı durumlarda oturumun düşmediği gözlemlenebilir.

### 🗺️ 2. Tehdit Modeli (Threat Model)
Sisteme sızmak isteyen bir hacker için en olası 2 yol:
1.  **Zayıf Şifreleme:** Kurulum sırasında belirlenen zayıf şifrelerin "Dictionary Attack" ile kırılması.
2.  **Webhook Manipülasyonu:** Dışarıya gönderilen bildirimlerin (Telegram/Discord) araya girilerek ele geçirilmesi ve sahte alarmlarla sistem yöneticisinin oyalatılması.

### 🛡️ 3. Defans Protokolü (Slide 10)
Sistemi korumak için şu 3 altın kural uygulanmalıdır:
1.  **Zero Trust:** Hiçbir kullanıcıya (admin olsa bile) körü körüne güvenme.
2.  **2FA (İki Faktörlü Doğrulama):** Uptime Kuma içinde mutlaka aktif edilmelidir.
3.  **Audit Logs:** Kimin, hangi saatte, hangi IP'den giriş yaptığı sürekli denetlenmelidir.