import requests
from bs4 import BeautifulSoup


def scrape():
    zoekterm = input()
    url = f"https://www.apotheek.nl/medicijnen/{zoekterm.strip()}#wat-zijn-mogelijke-bijwerkingen"
    print(f"link: {url}")

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    koppen = soup.find_all('span', class_='sideEffectsItem_button__V-L1C')
    # print(f"koppen: {koppen}") # Voor debuggen
    bijwerkingen = []

    for idx, kop in enumerate(koppen):
        try:
            artikel_titel = kop.find('strong').text
            if artikel_titel.split(' ')[0] == 'Bij':
                pass
            else:
                bijwerkingen.append(artikel_titel.strip().replace('.', '').replace(',', 'fe'))
        except AttributeError:
            print(f"\tError in bijwerking {idx}. Bijwerking 1 niet toegevoegd aan lijst!")
        # geef voorbeeld van hoe je die informatie kunt omzetten naar een insert into statement.
        # sql = f"INSERT INTO nos (url, titel) VALUES ('{pagina_url}', '{artikel_titel}');"
    print(f"bijwerkingen: {bijwerkingen}")


if __name__ == '__main__':
    scrape()
