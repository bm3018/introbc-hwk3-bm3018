import string


if __name__ == '__main__':

    char_dict = dict(zip(list(string.ascii_lowercase), range(26)))
    eng_freq_txt = 'etaoinshrdlcumwfgypbvkjxqz'

    # test string
    # encrypt_txt = "dvvkzecfssprkkve"

    # read problem 2 text file 
    with open('problem2.txt') as f:
        encrypt_txt = f.readlines()[0]

    # get count of letter frequencies in encrypted string
    encrypt_txt_freq_dict = {}
    for i in encrypt_txt:
        if i == ' ':
            pass
        else:
            if i in encrypt_txt_freq_dict.keys():
                encrypt_txt_freq_dict[i] += 1
            else:
                encrypt_txt_freq_dict[i] = 1

    # sort by most frequent letters
    sorted_encrypt_txt_freq_dict = dict(sorted(encrypt_txt_freq_dict.items(), key=lambda item: item[1], reverse=True))
    # select most frequent 
    most_freq = list(sorted_encrypt_txt_freq_dict.keys())[0]
    # get shift from most freq letter to the most common english letter 
    rot = (25 - char_dict[most_freq]) + (char_dict[eng_freq_txt[0]] + 1)

    # for each character, index in alphabet generate shifted list
    rot_char_list = []
    for char, indx in char_dict.items():
        char_shift = ord(char) + rot
        if char_shift > 122:
            char_shift = char_shift % 122 + 96
        rot_char_list.append(chr(char_shift))

    # used shifted list to decrypt text 
    decrypted_txt = []
    for i in encrypt_txt:
        if i.isalpha():
            char_indx = char_dict[i]
            decrypted_txt.append(rot_char_list[char_indx])
        else:
            decrypted_txt.append(i)

    # out
    print(f"plain text: {''.join(decrypted_txt)}")
    print(f'author: Satoshi Nakamoto')
    print(f'from: Bitcoin: A Peer-to-Peer Electronic Cash System')
    print(f'rotation factor: {rot}')
