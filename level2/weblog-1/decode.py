#!/usr/bin/env python3

def xor_decode(encoded, key):
    decoded = list(encoded)
    key_len = len(key)
    for i in range(len(encoded)):
        for j in range(key_len):
            decoded[i] = chr(ord(decoded[i]) ^ ord(key[j]))
    return ''.join(decoded)

key = '2020-06-02'

encode_1 = 'bmha[tqp[gkjpajpw'
encode_2 = '+rev+sss+lpih+qthke`w+mieacaw*tlt'
encode_3 = '8;tlt$lae`av,&LPPT+5*5$040$Jkp$Bkqj`&-?w}wpai, [CAP_&g&Y-?'

decode_1 = xor_decode(encode_1, key)
decode_2 = xor_decode(encode_2, key)
decode_3 = xor_decode(encode_3, key)

print(decode_1 + decode_2 + decode_3)