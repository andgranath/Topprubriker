import requests
from bs4 import BeautifulSoup

#DN-crawl

url_dn = "https://www.dn.se/"
page_dn = requests.get(url_dn)

soup_dn = BeautifulSoup(page_dn.content, "html.parser")
results_dn = soup_dn.find(class_="section__block section__block--above")
test_dn = soup_dn.find_all("div", class_="section__block")
rubriker_dn = results_dn.select("h1.teaser__title")
pufftext_dn = results_dn.select("p")

#Testar om jag kan få med pufftexten
for elem in test_dn:
    rubrik_elem_dn = elem.find("h1", class_="teaser__title")
    text_elem_dn = elem.find("p")
    if None in (rubrik_elem_dn, text_elem_dn):
        continue
    print(str(rubrik_elem_dn.text.strip()) + " – " + str(text_elem_dn.text.strip()))

#Slut test
    
    
print("""
      --- Dagens Nyheter ---
      """)
for rubrik in rubriker_dn:
    #rubrik_element = 
    print("DN: " + rubrik.text.strip())

    
#Svt-crawl
print("""
      --- Svt Nyheter ---
      """)
url_svt = "https://www.svt.se/"
page_svt = requests.get(url_svt)

soup_svt = BeautifulSoup(page_svt.content, "html.parser")
results_svt = soup_svt.find(class_="nyh_feed")
rubriker_svt = results_svt.select("h1")

for rubrik in rubriker_svt[0:6]:
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
    
    print("Expressen: " + rubrik.text)