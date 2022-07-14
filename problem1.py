import string


if __name__ == '__main__':

    # test strings
    # decrypt_str = 'Now is the winter of our discontent made glorious summer'
    # encrypt_str = 'vwe qa bpm eqvbmz wn wcz lqakwvbmvb uilm otwzqwca acuumz'
    
    encrypt_str = 'maxzxxlxmatmetbwmaxzhewxgxzzlunmgxoxkvtvdexw'

    char_dict = dict(zip(list(string.ascii_lowercase), range(26)))
    int_dict = dict(zip(range(26), list(string.ascii_lowercase)))
    out_dict = {}
    # iterate through 1-25
    for inc in range(1, len(char_dict)):
        temp_list = []
        
        # for each char in encrypted string, increment by inc
        for c in encrypt_str:
            if c == ' ':
                temp_list.append(' ')
            else:
                i_loc = char_dict[c]
                i_loc += inc
                if i_loc >= 26:
                    i_loc -= 26
                temp_list.append(int_dict[i_loc].upper())
        
        # save results in dictionary
        out_dict[inc] = ''.join(temp_list)
    
    # print out all rotated strings to determine correct rotation factor 
    # for rot_fac, out_str in out_dict.items():
    #     print(rot_fac, out_str)
    
    # out 
    print(f'Correct rotation factor: {7}')
    print(out_dict[7])
    print('Source: Winston Churchill')

