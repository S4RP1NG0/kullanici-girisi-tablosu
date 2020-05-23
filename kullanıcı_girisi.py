sys_kullanıcı_adı="Demo"
sys_parola="12345"
deneme_hakkı=3

while True:
    kullanıcı_adı = input("Kullanıcı Adı: ")
    parola = input("Parola: ")

    if (kullanıcı_adı == sys_kullanıcı_adı and sys_parola != parola):
        print("Parola Hatalı..")
        deneme_hakkı -=1
        print("Giriş Hakkı: ", deneme_hakkı)
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola):
        print("Kullanıcı Adı Hatalı..")
        deneme_hakkı -=1
        print("Giriş Hakkı: ", deneme_hakkı)
    elif (kullanıcı_adı != sys_kullanıcı_adı and parola != sys_parola):
        print("Kullanıcı adı ve parola hatalı.")
        deneme_hakkı -=1
        print("Giriş Hakkı: ", deneme_hakkı)
    else:
        print("Giriş yapıldı.")
    if (deneme_hakkı==0):        
        print("Deneme Hakkınız Kalmadı..")
        break
