#используем множества 
vowels = set('oaeiu')  #создаем множества гласных
word = input("Provide a word to search for vowels: ")
found=vowels.intersection(set(word)) #ищем общие объекты
for vowels in found:
    print(vowels)