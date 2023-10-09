numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = int(input("Введите число от 0 - 10:    "))
if (numbers >= 0 and numbers <= 3) or (numbers >= 6 and numbers <= 10):
    print("подходящий диапазон")
else:
    print("неудачный диапазон")


