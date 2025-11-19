import requests
import json
import time

API_URL = "https://trendurunlermarket.com/api/v1/products"
OUTPUT_FILE = "urun_listesi.json"

def urunleri_cek():
    print("🟦 TRM Ürünlerini çekiyorum...")
    try:
        response = requests.get(API_URL, timeout=20)
        if response.status_code == 200:
            urunler = response.json()
            with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
                json.dump(urunler, f, ensure_ascii=False, indent=2)
            print("🟩 Başarılı: Ürünler kaydedildi → urun_listesi.json")
        else:
            print(f"🟥 API Hatası: {response.status_code}")
    except Exception as e:
        print(f"🟥 Bağlantı hatası: {e}")

def dongu():
    while True:
        urunleri_cek()
        print("⏳ 1 saat bekleniyor...")
        time.sleep(3600)

if __name__ == "__main__":
    print("🚀 TRM ÜRÜN VERİ BOTU BAŞLADI")
    dongu()
