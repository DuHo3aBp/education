#создание функции на примере использования множеств
def search4vowels(word:str) -> set: 
        """Возвращает гласные найденные в слове"""
        vowels = set('oaeiu')  #создаем множества гласных
        return vowels.intersection(set(word)) #ищем общие объекты
