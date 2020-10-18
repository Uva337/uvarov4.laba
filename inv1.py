x=int(input("Введите число кг:"))
if x<=50:
    money = x*30
    print("Заработал :",money)
elif (50 <x and x <75):
    money=x*50
    print("Заработал :", money)
else:
    if (75<x and x<90):
        money=x*65
        print("Заработал :",money)
    else:
        money=x*70+20
        print("Заработал :",money)

