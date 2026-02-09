bakiye = 1000
while True:
    print("1 - Para çek\n2 - Para yatır\n3 - Bakiye görüntüle\n4 - Çıkış\n")

    try:
        secim = int(input("İşlem seçin: "))
    except:
        print("\nHatalı seçim!\n")
        continue

    if secim == 1:
        miktar = int(input("Çekmek istediğiniz miktarı girin: "))
        if miktar>bakiye:
            print("\nYetersiz bakiye!\n")
                
        elif miktar<=0:
            print("\nGeçersiz miktar!\n")
                
        else:
            bakiye -= miktar
            print("\nİşlem tamamlandı.\n")
        

    elif secim == 2:
        miktar2 = int(input("Yatırmak istediğiniz miktarı girin: "))
        if miktar2<=0:
            print("\nGeçersiz miktar!\n")
        else:
            bakiye += miktar2
            print("\nİşlem tamamlandı.\n")
        

    elif secim == 3:
        print("\nBakiye:", bakiye, "TL\n")
        

    elif secim==4:
        print("Çıkış yapıldı.")
        break

    else:
        print("\nHatalı seçim!\n")
        continue

