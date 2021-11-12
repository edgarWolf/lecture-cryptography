# Erstes Element = ggt, Zweites Element = inverses (meist nicht Primärepräsentant)
def eea(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        (ggt, other_a, other_b) = eea(b, a % b)
        return (ggt, other_b, other_a - (other_b * int((a / b))))


if __name__ == '__main__':
    number = int(input("Input number you want to search an inverse for... "))
    mod = int(input("Input mod which number you want to search its inverse... "))

    (ggt, x, y) = eea(number, mod)

    if (ggt != 1):
        print("No inverse found")

    else:
        inverse =  x % mod
        print("Inverse is " + str(inverse))