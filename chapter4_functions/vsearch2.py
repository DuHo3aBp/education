#создание функции на примере использования множеств
def search4vowels(word): 
        """Возвращает булево значение в зависимостиъ
        от присутствия любых гласных"""
        vowels = set('oaeiu')  #создаем множества гласных
        found = vowels.intersection(set(word)) #ищем общие объекты
        return bool(found)
