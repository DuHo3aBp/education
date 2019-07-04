#создание функции на примере использования множеств
def search4vowels(word): 
        """Выводит гласные найденые в введенном в слове"""
        vowels = set('oaeiu')  #создаем множества гласных
        found = vowels.intersection(set(word)) #ищем общие объекты
        for vowels in found:
                print(vowels)