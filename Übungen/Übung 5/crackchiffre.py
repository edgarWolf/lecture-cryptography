import string
import numpy as np

m = 29
alphabet = string.ascii_lowercase + "äöü"


def convert_char_to_indcies(elements):
    result = []
    for element in elements:
        current_indices = []
        for char in element:
            index = alphabet.find(char)
            current_indices.append(index)
        result.append(current_indices)
    return result


def get_word_diff_vector(w0, elements):
    result = []
    for i in range(len(elements)):
        w0i = w0[i]
        element = elements[i]
        diff = (element - w0i) % m
        result.append(diff)
    return result



if __name__ == "__main__":
    words = ["nase", "hase", "wick", "wack", "fupp"]
    chiffres = ["hezg", "hlzr", "lfbb", "nftb", "nkäf"]

    word_indices = []
    chiffre_indices = []

    word_indices = convert_char_to_indcies(words)
    chiffre_indices = convert_char_to_indcies(chiffres)

    w0 = word_indices[0]
    W = []
    for word_index in word_indices[1:]:
        W.append(get_word_diff_vector(w0, word_index))

    c0 = chiffre_indices[0]
    C = []
    for chiffre_index in chiffre_indices[1:]:
        C.append(get_word_diff_vector(c0, chiffre_index))

    np_W = np.array(W)
    print(np_W)

    det_W = round(np.linalg.det(np_W) % m)
    print(det_W)




    





