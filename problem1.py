import string

# are functions with docstrings required?
# do you want us to print out string rotation factors? - it is not explicity requested 

if __name__ == '__main__':

    # decrypt_str = 'Now is the winter of our discontent made glorious summer'
    # encrypt_str = 'vwe qa bpm eqvbmz wn wcz lqakwvbmvb uilm otwzqwca acuumz'
    
    encrypt_str = 'maxzxxlxmatmetbwmaxzhewxgxzzlunmgxoxkvtvdexw'

    char_dict = dict(zip(list(string.ascii_lowercase), range(26)))
    int_dict = dict(zip(range(26), list(string.ascii_lowercase)))
    out_dict = {}
    for inc in range(1, len(char_dict)):
        temp_list = []
        for c in encrypt_str:
            if c == ' ':
                temp_list.append(' ')
            else:
                i_loc = char_dict[c]
                i_loc += inc
                if i_loc >= 26:
                    i_loc -= 26
                temp_list.append(int_dict[i_loc].upper())
        
        out_dict[inc] = ''.join(temp_list)
    
    # for rot_fac, out_str in out_dict.items():
    #     print(rot_fac, out_str)
    
    print(f'Correct rotation factor: {7}')
    print(out_dict[7])
    print('Source: Winston Churchill')

