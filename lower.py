word = 'banana'
new_word = word.lower()
print(new_word)

new_word = word.encode()
print(new_word)

new_word = word.capitalize()
print(new_word)

new_word = word.endswith('na')
print(new_word)

new_word = word.replace('na', 'ca')
print(new_word)

new_word = word.translate(str.maketrans('na', 'ma'))
print(new_word)

new_word = word.index('n')
print(new_word)

new_word = word.count('a')
print(new_word)

new_word = word.center(12,'-')
print(new_word)

new_word = word.isalpha()
print(new_word)

new_word = word.format()
print(new_word)

new_word = word.find('n')
print(new_word)

new_word = word.isnumeric()
print(new_word)

