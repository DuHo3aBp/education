#нужно найти, чтобы СЛОВАРЬ вернул только найденное количество повторений букв в слове
#и не выводил пустые буквы, которые не повторялись
vowels = ['o','a','e','i','u']
word = input("Provide a word to search for vowels: ")
found={}    #убрали инициированные буквы из словаря

for letter in word:
    if letter in vowels:
        found.setdefault(letter,0)  #setdefault инициализирует по умолчанию букве 0 значение, чтобы не было ошибок при запуске кода
        found[letter] += 1
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'times')