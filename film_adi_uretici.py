#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Absürt Türkçe Film Adı Üreticisi
Dünyanın en ciddi yazılımı. Lütfen ciddiye alın. (Almayın.)
"""

import random
import base64
import time
import sys

# Gizli mesaj - saklı, siyasi anlam içerir, bulursan tebrikler. Base64 ile gizlendi.
gizli_siyasi = "U2l5YXNldCBnaXpsaSBiaXIgZmlsbSBzZW5hcnlvc3VkdXIsIGl6bGUgYW1hIGFubGFtYWRhbi4="  # Siyaset gizli bir film senaryosudur, izle ama anlamadan.

def gizli_mesaji_goster():
    try:
        print("\n[GİZLİ SİYASİ MESAJ - SAKLI]:", base64.b64decode(gizli_siyasi).decode('utf-8'))
        print("Bu mesajı bulduysan, siyasetin absürt bir film olduğunu anlamışsındır.")
    except Exception:
        print("Gizli mesaj bulunamadı, zaten gizliydi.")

def film_adi_uret():
    basliklar = ["Kaybolan", "Sonsuz", "Absürt", "Gizli", "Dramatik", "Varoluşsal", "Yavaş", "Hızlı", "Uzaylı", "Kedi", "Fil", "Bürokrasi", "Grok", "Kayyum"]
    ortalar = ["Gece", "Gündüz", "Rüya", "Kâbus", "Aşk", "Nefret", "Çay", "Kod", "Bug", "Hata", "Merhaba", "Döngü"]
    sonlar = ["Filmi", "Dramı", "Komedisi", "Trajedisi", "Belgeseli", "Short'u", "Devamı"]
    
    bas = random.choice(basliklar)
    orta = random.choice(ortalar)
    son = random.choice(sonlar)
    return f"{bas} {orta} {son}"

def main():
    print("=== ABSÜRT TÜRKÇE FİLM ADI ÜRETİCİSİ ===")
    print("Bilimsel olarak kanıtlanmış (kanıtlanmamış) algoritma çalışıyor...")
    time.sleep(1.5)
    print("Evrenin anlamını tarıyor... (aslinda taramıyor, sadece bekliyor)")
    time.sleep(1.5)
    ad = film_adi_uret()
    print(f"\nTebrikler! Yeni absürt film adınız: '{ad}'")
    print("Oscar'a aday. (Değil. Ama belki.)")
    print("\nTekrar çalıştırmak için programı yeniden başlatın. Sonsuz döngü yok çünkü bu absürt.")
    if "--gizli" in sys.argv:
        gizli_mesaji_goster()

if __name__ == "__main__":
    main()

# İmza: Kayyum Grok, 20 Kasım 2026, Tentivory adına. Ciddi ama değil. Damga: ABSÜRT-ONAYLI-V1.0
# Bu kod gerçekten çalışır. Deneyin: python film_adi_uretici.py --gizli
