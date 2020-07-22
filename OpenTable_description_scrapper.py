import bs4
import requests
import webbrowser

def getRestaurantDescription(restaurantUrl):
    res = requests.get(restaurantUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#overview-section > div._3c23fa05 > div > div > div')
    return elems[0].text

descriptions = []
language_tag = [
    'en',
    'de',
    'es',
    'fr',
    'it',
    'nl',
    'ja'
    ]

for i in range(len(language_tag)):
    print(language_tag[i])
    try:
        descriptions.append(getRestaurantDescription('https://www.opentable.com/r/harris-san-francisco?lang=%s'%(language_tag[i])))
    except IndexError:
        descriptions.append('Null')
    i += 1

print(descriptions)
