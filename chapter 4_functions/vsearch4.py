#создание универсальной функции на примере использования множеств
def search4vowels(phrase: str) -> set:
        """Возвращает гласные найденные в слове"""
        vowels = set('oaeiu')  #создаем множества гласных
        return vowels.intersection(set(phrase)) #возвращаем на экран гласные из множества

def search4letters(phrase: str, letters: str) -> set:
        """Возвращает множество букв из 'letters', найденных 
        в указанной фразе"""
        return set(letters).intersection(set(phrase)) #заменяет строки 4-5
