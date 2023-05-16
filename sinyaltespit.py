konumlar = ("2100 SOKAK NO:5 GÜNEŞ APT. HATAY/ARSUZ", "2100 SOKAK NO:6 ÇİÇEK APT.HATAY/ARSUZ", "2100 SOKAK NO:14 DİNÇER APT.HATAY/ARSUZ")

# Alınan sinyallerin ve hangi konumdan alındığının yazılacağı liste
sinyal_listesi = []

# Konumların ekleneceği sözlük
sinyal_konumlari = {}

cevap = input("Sisteme admin olarak mı kullanıcı olarak mı giriş yapmak istiyorsunuz? (admin/kullanıcı): ").lower()

while cevap != "admin" and cevap != "kullanıcı":
    cevap = input("Lütfen geçerli bir cevap veriniz. (admin/kullanıcı): ").lower()

if cevap == "admin":
    print("Giriş Ekranına Yönlendiriliyorsunuz...")
    print("Lütfen menüden seçim yapınız")
    menu = ["1. Giriş Yap", "2.Üye Ol","3.Şifremi Unuttum"]
    adminadi_sifre = {"adminadi": "melitto", "sifre": "12345"}
    

    while True:
        for i in menu:
            print(i)
        secim = input("Seçim: ")
    
        if secim == "1":
            giris_hakki = 3
    
            print("Hoşgeldiniz!")
    
            while giris_hakki > 0:
                print(f"{giris_hakki} giriş hakkınız kaldı.")
                username = input("Kullanıcı adını giriniz: ")
                password = input("Şifrenizi giriniz: ")
    
                if username == adminadi_sifre["adminadi"] and password == adminadi_sifre["sifre"]:
                    print("Giriş Başarılı!")
                    break
                else:
                    print("Kullanıcı adı veya şifre hatalı.")
    
                giris_hakki -= 1
    
                if giris_hakki == 0:
                    print("Giriş hakkınız kalmadı.")
                    break
                
        elif secim == "2":
            print("Lütfen üye olunuz.")
            username = input("Kullanıcı adı belirleyiniz: ")
            password = input("Şifre belirleyiniz: ")
            adminadi_sifre["adminadi"]=username
            adminadi_sifre["sifre"]=password
            print("Üye Oldunuz!")
            
            
        elif secim == "3":
            yeni_sifre = input("Yeni şifrenizi belirleyiniz: ")
            adminadi_sifre["sifre"] = yeni_sifre
            print("Şifreniz başarıyla değiştirildi.")
    
        else:
            print("Lütfen geçerli bir seçim yapınız!")
        
        for konum in konumlar:
            while True:
                print("Drone konuma gidiyor:", konum)
                sinyal_var_mi = input("Sinyal var mı? (E/H): ")
        
                if sinyal_var_mi.upper() == "E":
                    sinyal_sayisi = int(input("Sinyal sayısını girin: "))
                    sinyal_listesi.append((konum, sinyal_sayisi))
                    sinyal_konumlari[konum] = sinyal_sayisi
                    print("Sinyal tespit edildi: Konum:", konum, "Sinyal Sayısı:", sinyal_sayisi)
                    break
                else:
                    print("Sinyal tespit edilemedi: Konum:", konum)
                    break
        
        baska_enkaz = input("Başka enkaz var mı? (E/H): ")
        
        if baska_enkaz.upper() == "E":
            yeni_konum = input("Yeni enkazın konumunu girin: ")
            while True:
                print("Drone konuma gidiyor:", yeni_konum)
                sinyal_var_mi = input("Sinyal var mı? (E/H): ")
        
                if sinyal_var_mi.upper() == "E":
                    sinyal_sayisi = int(input("Sinyal sayısını girin: "))
                    sinyal_listesi.append((yeni_konum, sinyal_sayisi))
                    sinyal_konumlari[yeni_konum] = sinyal_sayisi
                    print("Sinyal tespit edildi: Konum:", yeni_konum, "Sinyal Sayısı:", sinyal_sayisi)
                    break
                else:
                    print("Sinyal tespit edilemedi: Konum:", yeni_konum)
                    break  
        
        # Sinyal yoksa drone durdurulsun
        if len(konumlar) != len(sinyal_konumlari):
            print("Drone durduruldu: Tüm konumlar tarandı, enkaz bulunamadı.")
        
        # Sinyal listesini ekrana bastırma
        print("Sinyal Listesi:")
        for sinyal in sinyal_listesi:
            print("Konum:", sinyal[0],"Sinyal Sayısı:", sinyal[1])
                
elif cevap == "kullanıcı":
    print("""Kullanıcı olarak giriş yapıldı
          Kullanıcıların sistemde herhangi bir yetkisi yoktur.
          Kullanıcılar sistemde sadece sinyal alınan konumları görebilirler.""")
   
    if len(sinyal_listesi) == 0:
        print("Henüz sinyal tespiti yapılmadı.")
    else:
        print("Sinyal Listesi:")
        for sinyal in sinyal_listesi:
            print("Konum:", sinyal[0], "Sinyal Sayısı:", sinyal[1])
