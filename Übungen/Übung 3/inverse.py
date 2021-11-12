
# Besser bei mod ne liste aller Zahlen für die gilt: ggt(x, mod) == 1
def get_inverse(number, mod):
    for i in range(mod):
        current_value = (number * i) % mod
        if current_value == 1:
            return i
    # -1 als Error wert
    return -1

if __name__ == '__main__':
    number = int(input("Input number you want to search an inverse for... "))
    mod = int(input("Return mod which number you want to search this inverse... "))

    inverse = get_inverse(number, mod)

    if inverse == -1:
        print("Could not find an inverse")
    else:
        print("Inverse element is " + str(inverse))


