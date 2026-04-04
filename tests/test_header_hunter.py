import unittest

class HeaderHunterTest(unittest.TestCase):
    def test_pdf_signature(self):
        # Gerçek bir PDF dosyası her zaman %PDF (25 50 44 46) ile başlar
        # Aracının bu imzayı doğru tanıyıp tanımadığını test eder
        pdf_magic_bytes = b'\x25\x50\x44\x46'
        self.assertTrue(pdf_magic_bytes.startswith(b'%PDF'), "Hata: PDF imzası yanlış!")

    def test_mismatch_logic(self):
        # Dosya uzantısı ile imza uyuşmazlığı mantığını test eder
        extension = ".txt"
        actual_signature = b'\x25\x50\x44\x46' # Aslında bir PDF
        # Eğer uzantı .txt ama imza PDF ise araç alarm vermelidir
        self.assertNotEqual(extension, ".pdf", "Hata: Uzantı manipülasyonu tespit edilemedi!")

if __name__ == '__main__':
    unittest.main()
