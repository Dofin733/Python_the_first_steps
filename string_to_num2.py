# программа получает строковые значения от пользователя через input, а в выводе использует преобразование str в integer и float  

num = input("Please, enter a number: ")
num2 = input("Please, enter the second number: ")
num3 = float(num) * float(num2)
print("The product of", int(num), "and", int(num2), "is", float(num3))
6