# x = input("Deger",)
# if ():
#     x = 1, print("True")
# else:
#     print("False")

# x = 5
# y = 4

# if (x > y):
#     print("En büyük sayı..:",x)
# elif (x==y):
#     print("Sayılar eşittir.")
# else:
#     (print("En büyük sayı..:",x))

# kullanici_adi = "aladin"
# şifre = 123
# x = input("Kullanıcı adı: ",)
# y = input("Şifre: ",)
# if (x == "aladin"):
#     print("Doğru")
# else:
#     print("Yanlış")
# if (y == "123"):
#     print("Doğru")
# else:
#     print("Yanlış")

print("                        HOŞGELDİNİZ                        \n")
print("                        Toplama için 1'e                        ")
print("                        Çıkarma için 2'ye                        ")
print("                        Çarpma için 3'e                        ")
print("                        Bölme için 4'e                        \n")
print("               YAPMAK İSTEDİĞİNİZ İŞLEMİ SEÇİNİZ                        \n")
print("               *Tüm işlemleriniz kayıt altına alınacaktır*             \n")
işlem =int(input("               Yapmak istediğiniz işlem numarası: "))
if(işlem == 1):
    Deger1 =int( input("Lütfen toplamak istediğiniz ilk sayıyı giriniz: "))
    Deger2 = int(input("Lütfen toplamak istediğiniz ikinci sayıyı giriniz: "))
    print(Deger1+Deger2)
elif(işlem == 2):
    Deger3 =int( input("Lütfen çıkarmak istediğiniz ilk sayıyı giriniz: "))
    Deger4 = int( input("Lütfen çıkarmak istediğiniz ikinci sayıyı giriniz: "))
    print(Deger3 - Deger4)
elif(işlem == 3):
    Deger5 =int( input("Lütfen çarpmak istediğiniz ilk sayıyı giriniz: "))
    Deger6 = int( input("Lütfen çarpmak istediğiniz ikinci sayıyı giriniz: "))
    print(Deger5*Deger6)
else:
    Deger7 =int( input("Lütfen bölmek istediğiniz ilk sayıyı giriniz: "))
    Deger8 = int( input("Lütfen bölmek istediğiniz ikinci sayıyı giriniz: "))
    print(Deger7/Deger8)

