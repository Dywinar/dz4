x =  input("Введите текст, и мы уберем весь текст кроме скобок: ")
y = 0
y = x.count("(")
while y != 0:
  if y >= 1:
    x1 = x[x.find("("):x.find(")")+ 1].replace("(", " ").replace(")", " ")
    x = x[x.find(")")+ 1:]
    print(x1)
    y-= 1
