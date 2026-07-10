def count(word):
    count = 0
    for letter in word:
        if letter == 'a':
            count = count + 1
    return count

word = input("Enter a word:")
print(count(word))