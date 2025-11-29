import random
oyun = ["taş", "kağıt", "makas"]
puan1 = 0
puan2 = 0
print("3 olan kazanır!")
while True:
    secim1 = random.choice(oyun)
    while True:
        secim2 = input("Taş, kağıt, yoksa makas mı?")
        if secim2 not in ["taş", "kağıt", "makas"]:
            print("Lütfen geçerli bir cevap girin.")
            continue
        else:
            break
        
    print("Benim seçimim:", secim1)
    if secim1 == secim2:
        print("Berabere, tekrar!")
        
    elif (secim1 == "taş" and secim2 == "kağıt") or (secim1 == "makas" and secim2 == "taş") or (secim1 == "kağıt" and secim2 == "makas"):
        puan2 += 1
        print("Puan durumu: ", puan2, "-", puan1)
        
    else:
        puan1 += 1
        print("Puan durumu: ", puan2, "-", puan1)
        
        
    if puan1 == 3:
        print("Maalesef kaybettin!")
        while True:
            cevap = input("Tekrar oynamak ister misin?")
            if cevap not in ["evet", "hayır"]:
                print("Lütfen geçerli bir cevap girin.")
                continue
            else:
                break
        if cevap == "evet":
            puan1 = 0
            puan2 = 0
            print("3 olan kazanır!")
            continue
        elif cevap == "hayır":
            print("Güzel oyundu!")
            break
           
    elif puan2 == 3:
        print("Tebrikler, kazandın!")
        while True:
            cevap = input("Tekrar oynamak ister misin?")
            if cevap not in ["evet", "hayır"]:
                print("Lütfen geçerli bir cevap girin.")
                continue
            else:
                break
        if cevap == "evet":
            puan1 = 0
            puan2 = 0
            print("3 olan kazanır!")
            continue
        elif cevap == "hayır":
            print("Güzel oyundu!")
            break
       
            
        
