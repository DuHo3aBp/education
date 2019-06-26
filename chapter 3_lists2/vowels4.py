#изменили list3.py из главы 2, чтобы СЛОВАРЬ вернул количество повторений букв в слове
vowels = ['o','a','e','i','u']
word = input("Provide a word to search for vowels: ")
found={ 'o':0,
        'a':0,
        'e':0,
        'i':0,
        'u':0   }

for letter in word:
    if letter in vowels:
        found[letter] += 1
for k, v in sorted(found.items()): #sorted позволяет отсортировать словарь по возрастанию
    print(k, 'was found', v, 'times')