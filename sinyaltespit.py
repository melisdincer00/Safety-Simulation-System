
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
                password = int(input("Şifrenizi giriniz: "))
    
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
            password = int(input("Şifre belirleyiniz: "))
            adminadi_sifre["adminadi"]=username
            adminadi_sifre["sifre"]=password
            print("Üye Oldunuz!")
            
            
        elif secim == "3":
            yeni_sifre = input("Yeni şifrenizi belirleyiniz: ")
            adminadi_sifre["sifre"] = yeni_sifre
            print("Şifreniz başarıyla değiştirildi.")
    
        else:
            print("Lütfen geçerli bir seçim yapınız!")
        

elif cevap == "kullanıcı":
    print("""Kullanıcı olarak giriş yapıldı
          Kullanıcıların sistemde herhangi bir yetkisi yoktur.
          Kullanıcılar sistemde sadece sinyal alınan konumları görebilirler.""")
