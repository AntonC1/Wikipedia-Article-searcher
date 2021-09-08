import wikipedia as wiki

z = input("Type the abbreviation of the language in which you want Wikipedia :")
x = input("Enter the search term in Wikipedia :")
y = wiki.page(x)
wiki.set_lang(z)

if wiki.suggest(x) is not None:
    print(f'Search term suggestion :{wiki.suggest(x)}')
else:
    print("No suggestion")
print(f'Found Articles : {wiki.search(x)}')
print(f'Article title : {y.title}')
print(wiki.summary(x))
print(f'Url :{y.url}')
