import random
import pymorphy2

spisok = ["ангел", "понос","лодка","остов","кошка","химия","физик","совет","свеча","поток","пенал","бебра","ножны","бобёр","живот","ложка","отдел","право","устой","обувь", ]
zagadka = spisok[random.randint(0, len(spisok) - 1)]
popitka = 0
print(zagadka)
win = False
while popitka <= 5:
    word = input()
    morph = pymorphy2.MorphAnalyzer()
    analyz = str(morph.parse(word))
    if 'FakeDictionary()' in analyz or 'UnknownPrefixAnalyzer' in analyz :
        print('Такого слова не существует')
    elif len(word) != 5:
        print('Слово не из 5 букв')
    elif 'NOUN' not in analyz:
        print('Это не существительное')
    else:
        popitka += 1
        for char in word:
            if char in zagadka:
                if word.index(char) == zagadka.index(char):
                    print(char.upper(), end='')
                else:
                    print(char, end='')
            else:
                print('*', end='')
    if zagadka == word.lower():
        win = True