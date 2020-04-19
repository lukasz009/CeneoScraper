# CeneoScraper
## Etap 1 - analiza struktury opinii w serwisie [Ceneo.pl](https://ceneo.pl/)
|Składowa                |Selektor                                        |Nazwa zmiennej|
|------------------------|------------------------------------------------|--------------|
|opinia                  |li.js_product-review                            |opinion       |
|identyfikator opiniii   |["data-entry-id"]                               |opinion_id    |
|autor                   |div.reviewer-name-line                          |author        |
|rekomendacja            |div.product-review-summary > em                 |recommendation|
|ocena                   |span.review-score-count                         |stars         |
|treść opinii            |p.product-review-body                           |content       |
|lista wad               |div.cons-cell > ul                              |cons          |
|lista zalet             |div.pros-cell > ul                              |pros          |
|przydatna               |button.vote-yes > span                          |useful        |
|nieprzydatna            |button.vote-no > span                           |useless       |
|data wystawienia opinii |span.review-time > time:first-child["datetime"] |opinion_date  |
|data zakupu             |span.review-time > time:nth-child(2)["datetime"]|purchase_date |
## Etap 2 - pobranie składowych pojedynczej opinii
- pobranie kodu jednej strony z opiniami o konkretnym produkcie
- wyciągnięcie z kodu strony fragmentów odpowiadających poszczególnym opiniom
- zapisanie do pojednynczych zmiennych wartości poszczególnych składowych opinii
## Etap 3 - pobranie wszystkich opinii o pojedynczym produkcie
- zapisanie do złożonej struktury danych składkowych wszystkich opinii z pojednyczej strony
- przechodzenie po kolejnych stronach z opiniami
- zapis wszystkich opini o pojedynczym produkcie do pliku
## Etap 4 - wyczyszenie danych i transformacja
- transformacja i wyszyszczenie danych
- refactoring kodu
- parametryzacja (bardziej uniwersalny kod)
## Etap 5 (Pandas, Matplotlib)
- wczytanie opinii do ramki danych
- policzenie podstawowych statystyk
- narysowanie wykresów funkcji
## Etap 6 - interfejs webowy dla scrappera (Flask)