str1 = input("Введите текс: ")

if len(str1) >= 15:
    even_chars = str1[::2] 
    print(even_chars)
else:
    print("Ваша строка меньше 15")
