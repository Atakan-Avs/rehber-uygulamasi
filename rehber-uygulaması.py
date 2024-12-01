# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 20:36:37 2024

@author: Atakan
"""

#guide_application
rehber={}

def kisi_ekle(isim,telefon):
    rehber[isim] = telefon   #isim-key telefon-value
    print(f"{isim} rehbere eklendi")

def kisi_ara(isim):
    if isim in rehber:
        print(f"{isim}: {rehber[isim]}")
    else:
        print("kişi bulunamadı")

def kisi_guncelle(isim,yeni_telefon):
    if isim in rehber:
        rehber[isim] = yeni_telefon
    else:
        print("kişi rehberde bulunamadı")

def kisi_sil(isim):
    if isim in rehber:
        del rehber[isim]
        print("kişi silindi")
    else:
        print("kişi rehberde yok")

while True:
    print("1.Kişi ekleme:")
    print("2.Kişi arama:")
    print("3.Kişi güncelleme:")
    print("4.Kişi silme:")
    print("5.Çıkış")

    secim=input("lütfen seçiminizi yapınız:(1-5)")

    if secim=="1":
        isimgir=input("lütfen eklemek istediğiniz kişinin ismini giriniz:")
        telnogir=input("lütfen eklediğiniz kişinin telefon numarasını giriniz:")
        kisi_ekle(isim,telefon)

    elif secim=="2":
        isimgir=input("lütfen aramak istediğiniz kişinin ismini giriniz:")
        kiis_ara(isim)

    elif secim=="3":
        isimgir=input("lütfen güncellemek istediğiniz kişinin ismini giriniz:")
        telnogir=input("lütfen güncellemek istediğiniz kişinin telefon numarasını giriniz:")
        kisi_guncelle(isim,telefon)

    elif secim=="4":
        isimgir=input("lütfen silmek istediğiniz kişinin ismini giriniz:")
        kisi_sil(isim)

    elif secim=="5":
        print("Çıkış yapılıyor...")
        break