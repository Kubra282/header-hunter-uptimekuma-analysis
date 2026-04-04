import sys

# Dosya imzaları (Magic Bytes) sözlüğü
MAGIC_NUMBERS = {
    "4d5a": "Windows Executable (PE/EXE)",
    "7f454c46": "Linux Executable (ELF)",
    "89504e47": "PNG Image File",
    "25504446": "PDF Document",
    "ffd8ffe0": "JPEG Image File",
    "504b0304": "ZIP Archive / MS Office OpenXML"
}

def analyze_file(file_path):
    try:
        with open(file_path, "rb") as f:
            # İlk 4 baytı oku ve hex formatına çevir
            header = f.read(4).hex().lower()
            
            print("-" * 40)
            print(f"🔍 Dosya Analiz Ediliyor: {file_path}")
            print(f"📦 Okunan Header (Hex): {header.upper()}")
            
            # Sözlükte eşleşme ara
            found = False
            for signature, file_type in MAGIC_NUMBERS.items():
                if header.startswith(signature):
                    print(f"✅ Tespit Edilen Tür: {file_type}")
                    found = True
                    break
            
            if not found:
                print("⚠️ Bilinmeyen veya tanımlanmamış dosya türü.")
            
            # Uzantı kontrolü (Basit bir güvenlik uyarısı)
            if not file_path.lower().endswith(('.exe', '.dll')) and header == "4d5a":
                print("🚨 KRİTİK UYARI: Bu dosya zararsız görünüyor ama aslında bir EXE!")
            
            print("-" * 40)

    except FileNotFoundError:
        print("❌ Hata: Dosya bulunamadı!")
    except Exception as e:
        print(f"❌ Beklenmedik bir hata oluştu: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("💡 Kullanım: python header_hunter.py <dosya_yolu>")
    else:
        analyze_file(sys.argv[1])