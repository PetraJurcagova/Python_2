alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#zakodovani zpravy
def encode(text, shift_number): # shift_number = posun
    shifted_text = " "
    for one_letter in text:
        if one_letter != " ": # vyreseni mezery
            index = alphabet.index(one_letter) # funkce index
            new_index = index + shift_number
            shifted_text += alphabet[new_index]
        else:
            shifted_text += one_letter
    print(shifted_text)

encode("petra ahoj", 3)










