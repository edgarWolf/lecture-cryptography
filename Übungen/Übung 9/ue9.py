import math
import random

def sqm(x, y, m):
    if y == 0:
        return 1
    if y % 2 != 0:
        a = sqm(x, y-1, m)
        return (a * x) % m
    if y % 2 == 0:
        a = sqm(x, y/2, m)
        return (a * a) % m

def is_prime(x):
    """Laufzeitanalyse: Eingabelänge ist 2^N; Durch das Wurzelziehen wird diese erheblich gekürzt. 2^(sqrt(N)) = 2^sqrt(N^1/2) = 2^(N/2)"""
    if (x == 0 or x == 1):
         return False
    if (x == 2 or x == 3):
        return True
    sqrt_x = math.floor(math.sqrt(x))
    for i in range(2, sqrt_x + 1):
        if x % i == 0:
            return False
    return True

def test_is_prime(values):
    results = []
    for value in values:
        prime = is_prime(value)
        results.append((value, prime))
        print("Number: {}    IsPrime: {}".format(value, prime))
    return results



def get_random_prime(num_bits):
    num = random.getrandbits(num_bits)
    while not is_prime(num):
        num = random.getrandbits(num_bits)
    return num

def brute_force_dl(result, base, modul):
    for i in range(2, modul):
        local_result = sqm(base, i, modul)
        if local_result == result:
            return i
    return None

def diffie_hellman(r, beta):
    # Um einen gemeinsamen Schlüssel zu erhalten muss das alpha an den Partner übermittelt werden. Dieser kann dann kB bestimmen mit kB = sqm(alpha, b, p)
    p = get_random_prime(8)
    a = random.randint(1, p - 1)
    alpha = sqm(r, a, p)

    kA = sqm(beta, a, p)
    kB = kA
    b = brute_force_dl(beta, r, p)
    success = sqm(r, b, p) == beta if b else False
    if success:
        print("p : {}\na : {}\nalpha : {}\nkA : {}\nb : {}\nsuccess: {}".format(p, a, alpha, kA, b, success))
    else: 
        print("Could not calculate all parameters of diffie-hellman algorithm due to beta-value " + str(beta))

    # Um Beta zu berechnen müssen wir das b des Partners kennen. Das ist aber aufgrund des Problems des diskreten Logarithmus nicht effizient berechenbar.
    # Eine naive Methode bei kleinen Zahlen wäre einfach ein Brute-Force: Wir probieren alle möglichen Werte für b durch, und schauen ob Beta als Ergebnis übereinstimmt.
    # Das ist aber bei großen Zahlen mit mehr als 32 Bits kaum berechenbar.

if __name__ == "__main__":
    #print(sqm(314213123,34125121,6))
    #prime_test_values = [2, 5, 6, 11, 20, 13514, 12371247, 1324141, 424793537353]
    #results = test_is_prime(prime_test_values)
    diffie_hellman(765293517, 9)