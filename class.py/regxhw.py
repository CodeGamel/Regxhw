import re

names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]

pattern =r'^([A-Z][a-z]*)( [A-Z][a-z]*)*$'


def verification(names):
    for name in names:
        if re.fullmatch(pattern, name):
            print(name)
    else:
        print('invalid name')
    
verification(names)
    