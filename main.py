class Biblioteka:
    def __init__(self, tytul, autor, rok):
        self.tytul = str(tytul)
        self.autor = str(autor)
        self.rok = (rok)
    def __repr__(self):
        return f"{self.tytul} {self.autor} {self.rok}"


tablica_pozycji = []
tablica_tytulow = []
tablica_autorow = []
ilosc = []
wynik = []

#print("Podaj ilosc")
podaj_ilosc = int(input())

for podane_dane in range(podaj_ilosc):
    #dana = input().split(',')
    dana = eval(input())
    tytul = dana[0]
    autor = dana[1]
    rok = int(dana[2])
    pozycja = Biblioteka(tytul,autor,rok)
    tablica_pozycji.append(pozycja)

#print(tablica_pozycji)

for pozycja in tablica_pozycji:
    tablica_tytulow.append(pozycja.tytul)

for y in tablica_tytulow:
    ilosc.append(tablica_tytulow.count(y))

#print(ilosc)
x = 0
for pozycja in tablica_pozycji:
    wynik.append("('"+pozycja.tytul+"', '"+pozycja.autor+"', "+str(ilosc[x])+")")
    x += 1
    wynik = set(wynik)
    wynik = sorted(wynik)

for z in wynik:
    print(z)
"""

import string


print("Podaj ilosc")
podaj_ilosc = int(input())
tablica_tytulow = []
tablica_autorow = []
tablica_rok = []

for podane_dane in range(podaj_ilosc):
    dana = input().split(',')
    tytul = str(dana[0])
    autor = str(dana[1])
    rok = dana[2]
    tytul = tytul.translate(str.maketrans('','',string.punctuation))
    autor = autor.translate(str.maketrans('','',string.punctuation))
    rok = rok.translate(str.maketrans('','',string.punctuation))
    rok = int(rok)
   
    tablica_tytulow.append(tytul)
    tablica_autorow.append(autor)
    tablica_rok.append(rok)
    

print(tablica_tytulow)
print(tablica_autorow)
print(tablica_rok)




class Biblioteka:
   def __init__(self, tytul, autor, rok):
    self.tytul = tytul
    self.rok = rok
"""