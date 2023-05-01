gun_sayisi: int = int(input("Öğrenmek istediğiniz günün sayısınız girin: "))

if gun_sayisi > 7 and gun_sayisi < 1:
    print("Yanlış değer girdiniz")
elif gun_sayisi == 1:
    print("Yevmu’l-Eḥad")
elif gun_sayisi == 2:
    print("Yevmu’l-İs̠neyn")
elif gun_sayisi == 3:
    print("Yevmu’s̠-S̠ülās̠ā’")
elif gun_sayisi == 4:
    print("Yevmu’l-Erbi‘ā’")
elif gun_sayisi == 5:
    print("Yevmu’l-Hamīs")
elif gun_sayisi == 6:
    print("Yevmu’l-Cumu'a")
elif gun_sayisi == 7:
    print("Yevmu’s-Sebt")

