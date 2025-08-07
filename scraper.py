import requests
from bs4 import BeautifulSoup
import datetime

# URL stranice koju scrape-ujemo
URL = "http://quotes.toscrape.com"

# Koristimo try-except blok za osnovno rukovanje greškama
try:
    # Šaljemo GET zahtev na zadati URL
    response = requests.get(URL)
    response.raise_for_status() # Proverava da li je zahtev bio uspešan (status kod 200)

    # Kreiramo BeautifulSoup objekat za parsiranje HTML-a
    soup = BeautifulSoup(response.content, "html.parser")

    # Pronalazimo sve elemente sa klasom "quote"
    quotes = soup.find_all("div", class_="quote")

    # Otvaramo fajl 'citati.txt' za pisanje. 'w' će prepisati fajl svaki put.
    # Koristimo encoding='utf-8' da bismo ispravno sačuvali specijalne karaktere.
    with open("citati.txt", "w", encoding="utf-8") as f:
        # Dodajemo trenutno vreme na početak fajla
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Citati preuzeti na dan: {now}\n")
        f.write("----------------------------------------\n\n")

        print("Preuzimam citate...")
        # Iteriramo kroz pronađene citate
        for quote in quotes:
            # Unutar svakog 'div.quote', pronalazimo tekst citata i autora
            text = quote.find("span", class_="text").get_text(strip=True)
            author = quote.find("small", class_="author").get_text(strip=True)

            # Ispisujemo u terminal i upisujemo u fajl
            print(f'"{text}" - {author}')
            f.write(f'"{text}"\n')
            f.write(f' - {author}\n\n')

        print("\nGotovo! Citati su sačuvani u fajl 'citati.txt'.")


except requests.exceptions.RequestException as e:
    print(f"Greška prilikom povezivanja na sajt: {e}")