import wikipedia as wiki

z = input("Wpisz skrot nazwy jezyka w jakim chcesz miec wikipedie :")
x = input("Podaj wyszukiwana fraze w Wikipedi :")
y = wiki.page(x)
wiki.set_lang(z)

if wiki.suggest(x) is not None:
    print(f'Sugestie odnosnie wyszukiwanej frazy :{wiki.suggest(x)}')
else:
    print("Brak sugestii")
print(f'Znalezione artykuly : {wiki.search(x)}')
print(f'Tytul artykulu : {y.title}')
print(wiki.summary(x))
print(f'Url :{y.url}')
