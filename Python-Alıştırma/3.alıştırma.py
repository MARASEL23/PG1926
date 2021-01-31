giriş = None
veri = []

print("************************************************ \n")
print("Verileri sırala.\nÇıkmak için 'q' veya 'Q' giriniz!\n")

while True:
    giriş = input("Sayi gir : ")

    try:
        if giriş == "q" or giriş == "Q":
            break
        elif giriş == "0":
            veri.insert(0, int(giriş))
        else:
            veri.append(int(giriş))

    except:
        print("Lütfen sayi giriniz")

print("Dizi :", veri)