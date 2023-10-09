list(map(chr, range(97, 123)))
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list = input("введите текст:    ")
count = 0
vowels = set("aeiou")
for input in list:
    if input in vowels:
        count += 1

print("Количество гласных равно:   ", count)
print("Количество символов =   ", len(list))
print("Текст в нижнем регистре    ", str.lower(list))







