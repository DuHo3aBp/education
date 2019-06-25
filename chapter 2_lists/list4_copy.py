#не используйте оператор присваивания, чтобы скопировать список
#используйте метод copy
import time

first=[1,2,3]      
second = first
second.append(4)
print("second is:", second)
print("first is:", first)   #как результат переменные ссылаются на один и тот же список

#а при использовании copy создастся новый список
time.sleep(2)
print("=====================")
third = second.copy()
third.append(5)
print("third is:", third)
print("second is:", second)
print("first is:", first)
