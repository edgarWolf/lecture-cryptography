import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import string
import math



# Vig table
def init_vig_table(alphabet):
    alphabet_length = len(alphabet)
    table = [["" for i in range(alphabet_length)] for j in range(alphabet_length)]
    for i in range(alphabet_length):
        for j in range(alphabet_length):
            current_letter = alphabet[(i + j) % alphabet_length]
            table[i][j] = current_letter
    return table


alphabet = string.ascii_lowercase + "äöüß"
vig_table = init_vig_table(alphabet)

# Quelle: https://de.wikipedia.org/wiki/Buchstabenh%C3%A4ufigkeit
most_common_german_characters_sortec_desc = [
    'e',
    'n',
    'i',
    's',
    'r',
    't',
    's',
    'a',
    'h',
    'd',
    'u',
    'c',
    'l',
    'g',
    'm',
    'o',
    'b',
    'f',
    'w',
    'z',
    'k',
    'v',
    'p',
    'ü',
    'ä',
    'ö',
    'ß',
    'j',
    'x',
    'q',
    'y'
]




def get_clear_text_from_table(chiffre_char, key_char):
    column = alphabet.index(key_char)
    row = (alphabet.index(chiffre_char) - column) % len(alphabet)
    return vig_table[row][0]


# Plotting

def plot_char_dist(char_dict:dict, title=None):
    keys = char_dict.keys()
    values = char_dict.values()
    plt.bar(keys, values)
    if title:
        plt.title(title)
    plt.show()


# Helpers

def get_char_distribution(text):
    chars = {}
    for char in text:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1

    return dict(sorted(chars.items(), key=lambda item: item[1]))

def get_repeating_sequence(text:str):
    
    text_length = len(text)
    max_count = 0
    most_frequent = None
    for j in range(0, text_length - 3):
        for i in range(0, text_length, 3):
            start = i + j
            end = start + 3
            if end >= text_length:
                break
            key = text[start:end]
            count = text.count(key)

            if count > max_count and key:
                max_count = count
                most_frequent = key

    return most_frequent
        




def get_distance(text:str, substring:str):
    text_length = len(text)
    first_occurence = text.find(substring)
    second_occcurence = text.find(substring, first_occurence + 1)
    minimal_distance = second_occcurence - first_occurence

    last_occurence = second_occcurence
    while last_occurence + minimal_distance < text_length:
        next_occurence = text.find(substring, last_occurence + 1)
        if next_occurence == -1:
            break
        distance = next_occurence - last_occurence
        if distance < minimal_distance:
            minimal_distance = distance
        last_occurence = next_occurence

    return minimal_distance


def get_char_distribution_for_given_key_length(text:str, key_length:int):
    char_dist = {}
    for index, letter in enumerate(text):
        if index % key_length == 0:
            if letter not in char_dist:
                char_dist[letter] = 1
            else:
                char_dist[letter] += 1
    return dict(sorted(char_dist.items(), key=lambda item: item[1]))


def get_char_distributions_for_given_key_length(text:str, key_length:str):
    char_dists = []
    text_length = len(text)
    char_counts = int(text_length / key_length)
    for i in range(key_length):
        char_dist = {}
        for j in range(char_counts):
            index = i + j * key_length

            if index >= text_length:
                break

            letter = text[index]
            if letter not in char_dist:
                char_dist[letter] = 1
            else:
                char_dist[letter] +=1

        char_dists.append(dict(sorted(char_dist.items(), key=lambda item: item[1])))
    return char_dists

            


def get_percentage_dist_for_dict(values:dict):
    percentage_dist = {}
    dict_values_sum = sum(values.values())
    for key in values:
        percentage_dist[key] = values[key] / dict_values_sum
    return percentage_dist



def match_chars_with_most_common_german_ones(chars:list):
    chars_desc = chars[::-1]
    char_table = {}
    for i in range(len(chars_desc)):
        char_table[chars_desc[i]] = most_common_german_characters_sortec_desc[i]
    return char_table



def solve_vig_cypher(text, key):
    key_length = len(key)
    result = ""
    for i in  range(len(text)):
        chiffre_letter = text[i]
        key_letter = key[i % key_length]

        clear_letter = get_clear_text_from_table(chiffre_letter, key_letter)
        result += clear_letter
    with open("cleartext.txt", "w") as f:
        f.write(result)





if __name__ == "__main__":
    with open("chiffre.txt") as file:
        content = file.read()
        char_dist = get_char_distribution(content)
        most_common_char = max(char_dist, key=char_dist.get)
        print("Most common character: " + most_common_char)

        most_common_substring = "jüi" # Auswahl für diesen string nur weil Abstände "angenehm" sind... häufigster string "npz" hat Abstand von 23 --> Primuzahl
        distance = get_distance(content, most_common_substring) # 112
        print("Minimal distance for string " + most_common_substring + " = " + str(distance)) 

        # Vermutung: Key-Länge = 8. Die Verteilungen für diese Key-Länge berechnen.
        char_dists = get_char_distributions_for_given_key_length(content, 8)

        possible_key_mappints = []
        for char_dist in char_dists:
            # Die Verteilungen mit denen der deutschen Sprache matchen.
            table = match_chars_with_most_common_german_ones(list(char_dist.keys()))
            # Aus der Tabelle die möglichen Schlüsselchiffren für die akutelle Iteration holen
            keys = [get_clear_text_from_table(key, table[key]) for key in table]
            possible_key_mappints.append(keys)

        # Alle Mappings durchlaufen und positionsweise (hier: spaltenweise) key-Strings bauen
        shortest_length = min([len(ls) for ls in possible_key_mappints])
        for i in range(shortest_length):
            key_text = ""
            for j in range(len(possible_key_mappints)):
                key_text += possible_key_mappints[j][i]
            print(key_text)


        # Diesen Key gewählt, da zweimal als key (Index = 0 und Index = 1)
        key = "guerckli"
        solve_vig_cypher(content, key)




