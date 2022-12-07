



from math import * #*-kõik funksioonid on vaja kasutada. kasutame: sin()
#import math kasutame:math.sin()
#2.osa Math kasutamine
print("Ristküliku ja ringi pindalad")
a=float(input("Anna laius:"))
b=float(input("Anna kõrgus:"))
S=a*b #+(plus),-(minus),/(delenie),*(umnozenie),**(stepen),sqrt(),//,%(protsent)
d=sqrt(a**2+b**2)
r=float(input("Anna raadius:"))
Skr=pi*r**2
print(f"Ristküliku pindalad on {S}. Ringi Pindala on {round(Skr,)}.")



#1. osa print(), input(),int(),float()
print("Hi Men!") #print() teksti või andmete väljastuseks
nimi=input("Mis on sinu nimi? ")#sisendi lugemine: akraanil "..."ja ootab , kuni kasutaha vajutab Enter Klahvi
#input() -> str
print(f"{nimi}, sul on väga ilus nimi!")
print(nimi,",sul on väga ilus nimi!")#kui on erinevat andmate tüübid
print(nimi+", sul on väga ilus nimi!")#kui on sarnane andmete tüüp
vanus=int(input("kui vana sa oled?"))# input()->int
print(f"{nimi} jargmisel aastal saad {vanus+1}")
print("Aga selle aastal on ",vanus)
vanus+=1 #muudame muutuja väärtus
print(f"Järgmine aasta on käes, siis {nimi} on {vanus} aastat vana")
pikkus=float(input("mis on sinu pikkus?")) #input()->float: 1.75
print(f"{nimi} on {vanus} aastat vana ja suurepärase pikkusega {pikkus}")

