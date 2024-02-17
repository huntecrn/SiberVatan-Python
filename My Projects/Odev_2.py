
# ÖDEV1
def emeklilik_kontrol(yas):
    emeklilik_yasi = 65
    
    if yas < emeklilik_yasi:
        kalan_yil = emeklilik_yasi - yas
        print(f"Emekliliğine {kalan_yil} yıl kaldı.")
    else:
        print("Zaten emeklisiniz.")

yas = int(input("Lütfen yaşınızı girin: "))
emeklilik_kontrol(yas)

# ÖDEV2
print("Yapamadım")

# ÖDEV3
def en_buyuk_sayi(liste):
    if not liste:
        return None
    else:
        return max(liste)

def en_kucuk_sayi(liste):
    if not liste:
        return None
    else:
        return min(liste)

liste1 = [10, 20, 30, 40, 50]
liste2 = [1, 2, 3, 4, 5]
toplam = en_buyuk_sayi(liste1) + en_kucuk_sayi(liste2)
print("İki listenin en büyük ve en küçük sayılarının toplamı:", toplam)

# ÖDEV3
print("Yapamadım")

# ÖDEV4
print("Yapamadım")

# ÖDEV5
def cift_tek_birlestir(liste1, liste2):
    yeni_liste = []
    

    for sayi in liste1:
        if sayi % 2 == 0:
            yeni_liste.append(sayi)
    

    for sayi in liste2:
        if sayi % 2 != 0:
            yeni_liste.append(sayi)
    
    return yeni_liste

liste1 = [1, 2, 3, 4, 5]
liste2 = [6, 7, 8, 9, 10]

sonuc_listesi = cift_tek_birlestir(liste1, liste2)
print("Çift ve tek sayıların birleştirilmiş hali:", sonuc_listesi)

# ÖDEV6
import random

def rus_ruleti():
    print("Rus Ruleti Oyununa Hoş Geldiniz!")
    print("1 ile 6 arasında bir sayı seçilmiştir.")
    hedef_sayi = random.randint(1, 6)
    
    while True:
        tahmin = int(input("Tahmininizi girin (1 ile 6 arasında bir sayı): "))
        if tahmin == hedef_sayi:
            print("Tebrikler! Doğru tahmin ettiniz. Oyunu kazandınız!")
            break
        else:
            print("BOOMMM!")

rus_ruleti()
