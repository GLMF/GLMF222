from odf.opendocument import load
from odf import teletype

count_with_space = 0
count = 0

doc = load('fichier_test.odt').text
txt = teletype.extractText(doc)
for car in txt:
    print(car, end='')
    count_with_space +=1
    if car not in (' ', '\t', '\n', u'\u00A0'):
        count += 1

print(f'\nTotal : ')
print(f'Avec espaces : {count_with_space} caractères')
print(f'Sans espaces : {count} caractères')
