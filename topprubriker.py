import requests
from bs4 import BeautifulSoup
from collections import Counter
from datetime import datetime

today = datetime.now()
print("""
      Topprubrikerna i svenska medier """ +str(today))
#DN-crawl

url_dn = "https://www.dn.se/"
page_dn = requests.get(url_dn)

soup_dn = BeautifulSoup(page_dn.content, "html.parser")
results_dn = soup_dn.find(class_="section__block section__block--above")
test_dn = soup_dn.find_all("div", class_="section__block")
rubriker_dn = results_dn.select("h1.teaser__title")
pufftext_dn = results_dn.select("p")

#Testkod för att se om jag kan få med pufftexten
#for elem in test_dn:
#    rubrik_elem_dn = elem.find("h1", class_="teaser__title")
#    text_elem_dn = elem.find("p")
#    if None in (rubrik_elem_dn, text_elem_dn):
#        continue
#    print(str(rubrik_elem_dn.text.strip()) + " – " + str(text_elem_dn.text.strip()))

#Slut test

rubriker_ord = " "
#En variabel som ska fyllas med samtliga rubriker, så att jag kan plocka ut dom vanligast förekommande orden.

    
print("""
      --- Dagens Nyheter ---
      """)

for rubrik in rubriker_dn:
    rubriker_ord = rubriker_ord + " " + rubrik.text
    #Lägger till senaste rubriken i rubriker_ord
    print("DN: " + rubrik.text.strip())

    
#Svt-crawl
print("""
      --- Svt Nyheter ---
      """)
url_svt = "https://www.svt.se/"
page_svt = requests.get(url_svt)

soup_svt = BeautifulSoup(page_svt.content, "html.parser")
results_svt = soup_svt.find(class_="nyh_feed")
rubriker_svt = results_svt.select("h1", class_="nyh_teaser__heading-title")

for rubrik in rubriker_svt[0:6]:
    rubriker_ord = rubriker_ord + " " + rubrik.text
    print("Svt: " + rubrik.text)

#GT-crawl
print("""
      --- GT ---
      """)
url_gt = "https://www.gt.se"
page_gt = requests.get(url_gt)
soup_gt = BeautifulSoup(page_gt.content, "html.parser")
results_gt = soup_gt.find(class_="site-body__column-2 widget-area widget-area--hard-divide")
rubriker_gt = results_gt.select("h2")

for rubrik in rubriker_gt[0:6]:
    #Satte ett intervall eftersom GT och Expressen har omfattande block på sina sajter.
    rubriker_ord = rubriker_ord + " " + rubrik.text
    print("GT: " + rubrik.text)

#Expressen-crawl

print("""
      --- Expressen ---
      """)
url_exp = "https://www.expressen.se"
page_exp = requests.get(url_exp)
soup_exp = BeautifulSoup(page_exp.content, "html.parser")
results_exp = soup_exp.find(class_="site-body__column-2 widget-area widget-area--hard-divide")
rubriker_exp = results_exp.select("h2")

for rubrik in rubriker_exp[0:6]:
    rubriker_ord = rubriker_ord + " " + rubrik.text
    print("Expressen: " + rubrik.text)

#Aftonbladet-crawl
print("""
      --- Aftonbladet ---
      """)
url_bladet = "https://www.aftonbladet.se/"
page_bladet = requests.get(url_bladet)
soup_bladet = BeautifulSoup(page_bladet.content, "html.parser")
results_bladet = soup_bladet.find(class_="_3p4DP")
rubriker_bladet = results_bladet.select("h3", class_="_3a12d")

for rubrik in rubriker_bladet[0:6]:
    if None in rubrik:
        continue
    rubriker_ord = rubriker_ord + " " + rubrik.text
    print("AB: " + rubrik.text.strip())


#Söker efter de vanligaste orden i rubrikerna. Först görs strängen om till en lista med split.
rubrikord_split = rubriker_ord.split()
fula_ord =["sina", "inte", "och", "han", "hon", "klart", "man", "just", "nu", "till", "från", "har", "mot", "att", "efter", "det", "blir", "vid", "det", "vet", "får", "bakom", "för", "nu:", "nu"]
rensade_ord = []
for ord in rubrikord_split:
    if ord.lower() in fula_ord:
        continue
    #Jag utesluter enskilda ord, eftersom jag inte vet hur jag annars ska rensa ut dem.
    elif len(ord) >= 3:
        rensade_ord.append(ord)
    
#kör counter på listan som skapas.
print("""
      --- De vanligaste orden i rubrikerna ---
      """)
counter = Counter(rensade_ord)
vanligast = counter.most_common(5)
print(vanligast)