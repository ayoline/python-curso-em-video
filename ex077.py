tuple_words = ('Contrary', 'to', 'popular', 'belief', 'Lorem', 'Ipsum', 'is', 'not', 'simply',
'random', 'text')
VOWELS = 'aeiou'
vowels_in_word = []

def who_is_vowel(word):
    for letter in word:
        if letter.lower() in VOWELS:
            vowels_in_word.append(letter.lower())

for i in range(0, len(tuple_words)):
    who_is_vowel(tuple_words[i])

    print(f'\nNa palavra {tuple_words[i].upper()} temos as vogais:', end=' ')
    for i in range(0,len(vowels_in_word)):
        print(f'{vowels_in_word[i]}', end=' ')

    vowels_in_word = []

print('\nFIM')
