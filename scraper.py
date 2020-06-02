#import bibliotek
import requests
import pprint
from bs4 import BeautifulSoup
import json

#funkcja do ekstrakcji składowych opinii
def extract_feature(opinion, selector, attribute = None):
    try:
        if attribute:
            return opinion.select(selector).pop()[attribute].strip()
        else:
            return opinion.select(selector).pop().text.strip()
    except IndexError:
            return None

#słownik z atrybutami opinii i ich selektorami
selectors = {
    "author": ["span.user-post__author-name"],
    "recommendation": ["span.user-post__author-recomendation > em"],
    "stars": ["span.user-post__score-count"],
    "content": ["div.user-post__text"],
    "cons": ["div.review-feature > div.review-feature__col:nth-child(2) > div.review-feature__item"], # do zmiany, nie zadziała jak są tylko wady/zalety
    "pros": ["div.review-feature > div.review-feature__col:nth-child(1) > div.review-feature__item"], # do zmiany, nie zadziała jak są tylko wady/zalety
    "useful": ["button.vote-yes > span"],
    "useless": ["button.vote-no > span"],
    "opinion_date": ["span.user-post__published > time:nth-child(1)", "datetime"],
    "purchase_date": ["span.user-post__published > time:nth-child(2)", "datetime"]
}

#adres url pierwszej strony z opiniami o produkcie
url_prefix = "https://www.ceneo.pl"
product_id = input("Podaj identyfikator produktu: ")
url_postfix = "tab=reviews"
url = url_prefix + "/" + product_id + url_postfix

#pusta lista z opiniami konsumentów
all_opinions = []

while url:
    #pobranie kodu pojedynczej strony z opiniami o produkcie
    response = requests.get(url)
    page_dom = BeautifulSoup(response.text, 'html.parser')

    #wydobycie z kodu strony fragmentów odpowiadających opiniom konsumentów
    opinions = page_dom.select("div.js_product-review")    
    
    #dla wszystkich opinii wydobycie ich składowych
    for opinion in opinions:
        features = {key : extract_feature(opinion, *args)
                    for key, args in selectors.items()}
        features["opinion_id"] = int(opinion["data-entry-id"])
        features["useful"] = int(features["useful"])
        features["useless"] = int(features["useless"])
        features["stars"] = float(features["stars"].split('/')[0].replace(',', '.'))
        features["content"] = features["content"].replace('\n',' ').replace('\r',' ')
        try:
            features["pros"] = features["pros"].replace('\n',', ').replace('\r',', ')
        except AttributeError:
            pass
        try:
            features["cons"] = features["cons"].replace('\n',', ').replace('\r',', ')
        except AttributeError:
            pass
        all_opinions.append(features)
    try:
        url = url_prefix + page_dom.select("a.pagination__next").pop()["href"]
    except IndexError:
        url = None      #lub: False
    print(len(all_opinions))
    print(url)

with open('./opinions_json/' + product_id + '.json', 'w', encoding="UTF-8") as fp:
    json.dump(all_opinions, fp, indent=4, ensure_ascii=False)

# pprint.pprint(all_opinions) 