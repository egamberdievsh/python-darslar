import random as r

def sontop():
    print("Keling o'ylagan sonni topish o'yinini o'ynaymiz")
    print("Men 1 dan 10 gacha bo'lgan bir son o'yladim topishga harakat qilib ko'ring")
    son = r.randint(1, 10)

    davom_et = True
    n = 1
    while davom_et:
        son1 = int(input("Taxminingizni kiriting: "))
        if son1 > son:
            n += 1
            print("\nXato, men o'ylagan son bundan kichikroq !\n")
        elif son1 < son:
            n += 1
            print("\nXato, men o'ylagan son bundan kattaroq !\n")
        else:
            davom_et = False
            print(f"\nTopdingiz. {son} sonini o'ylagan edim. {n} ta taxmin bilan topdingiz. Tabriklayman !!!")
def sontop_pc():
    input("1 dan 10 gacha son o'ylang va istalgan tugmani bosing. Men topaman  ")

    davom = True

    s = 0
    quyi = 1
    yuqori = 10
    while davom:
        s += 1
        if quyi != yuqori:
            son2 = r.randint(quyi, yuqori)
        else:
            son2 = quyi
        belgi = input(f"Siz {son2} ni o'yladingiz. To'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-) ?")

        if belgi == '+':
            quyi = son2 + 1

        elif belgi == '-':
            yuqori = son2 - 1

        else:
            davom = False
            print(f"Siz o'ylagan {son2} sonini {s} ta taxmin bilan topdim.")


sontop()
sontop_pc()
