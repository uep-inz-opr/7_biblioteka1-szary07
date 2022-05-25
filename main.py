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
