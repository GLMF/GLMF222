from os import listdir
from os.path import isfile, join
from odf.opendocument import load
from odf import teletype
import sys

count_with_space = 0
count = 0
nb_fic = 0

for file in listdir('docs/' + sys.argv[1]):
    filename = join('docs/' + sys.argv[1], file)
    if isfile(filename) and filename.endswith('.odt'):
        nb_fic += 1
        doc = load(filename).text
        txt = teletype.extractText(doc)
        for car in txt:
            count_with_space +=1
            if car not in (' ', '\t', '\n', u'\u00A0'):
                count += 1

print(f'Total pour {sys.argv[1]} :')
print(f'    {nb_fic} fichiers')
print(f'    Avec espaces : {count_with_space} caractères')
print(f'    Sans espaces : {count} caractères')
