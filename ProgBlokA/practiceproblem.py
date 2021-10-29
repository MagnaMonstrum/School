def encoding(text):
    'prints ASCII codes of characters in S, one per line'
    print('Char Decimal Hex Binary') # print column headings
    for c in text:
        code = ord(c) # compute ASCII code
        # print character and its code in decimal, hex, and binary
        print(' {} {:7} {:10x} {:7b}'.format(c,code,code,code))
encoding("dad")