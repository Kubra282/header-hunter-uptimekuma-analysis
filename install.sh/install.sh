#!/bin/bash
# Uptime Kuma Kurulum Scripti (Analiz için hazırlanmıştır)

echo "🛡️ Kurulum Başlıyor..."

# 1. Dizin Oluşturma (Analiz Noktası!)
mkdir -p /opt/uptime-kuma
cd /opt/uptime-kuma

# 2. Paket İndirme (Kritik Güvenlik Sorusu Burası!)
# Hocanın sorduğu hash kontrolü burada YAPILMIYOR:
curl -L https://github.com/louislam/uptime-kuma/archive/refs/heads/main.tar.gz | tar xz --strip-components=1

# 3. Bağımlılıkların Kurulması
npm install --production
npm run setup

echo "✅ Kurulum Tamamlandı!"