import string

# are functions with docstrings required?
# confirm that for the first part of problem 2, there is nothing to technically submit?

if __name__ == '__main__':

    char_dict = dict(zip(list(string.ascii_lowercase), range(26)))
    eng_freq_txt = 'etaoinshrdlcumwfgypbvkjxqz'

    # encrypt_txt = "dvvkzecfssprkkve"
    with open('problem2.txt') as f:
        encrypt_txt = f.readlines()[0]

    encrypt_txt_freq_dict = {}
    for i in encrypt_txt:
        if i == ' ':
            pass
        else:
            if i in encrypt_txt_freq_dict.keys():
                encrypt_txt_freq_dict[i] += 1
            else:
                encrypt_txt_freq_dict[i] = 1

    sorted_encrypt_txt_freq_dict = dict(sorted(encrypt_txt_freq_dict.items(), key=lambda item: item[1], reverse=True))
    most_freq = list(sorted_encrypt_txt_freq_dict.keys())[0]
    rot = (25 - char_dict[most_freq]) + 26 % char_dict[most_freq]

    rot_char_list = []
    for char, indx in char_dict.items():
        char_shift = ord(char) + rot
        if char_shift > 122:
            char_shift = char_shift % 122 + 96
        rot_char_list.append(chr(char_shift))

    decrypted_txt = []
    for i in encrypt_txt:
        if i.isalpha():
            char_indx = char_dict[i]
            decrypted_txt.append(rot_char_list[char_indx])
        else:
            decrypted_txt.append(i)

    print(f"plain text: {''.join(decrypted_txt)}")
    print(f'author: Satoshi Nakamoto')
    print(f'from: Bitcoin: A Peer-to-Peer Electronic Cash System')
    print(f'rotation factor: {rot}')
