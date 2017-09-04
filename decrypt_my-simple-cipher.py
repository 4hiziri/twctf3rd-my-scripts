#! /usr/bin/env python2

def decrypt_char(cipher_char, key_char, prev_cipher):
    return chr((ord(cipher_char) - ord(key_char) - ord(prev_cipher)) % 128)


def decrypt(key, cipher):
    ret = ''

    iv = cipher[0]
    cipher = cipher[1:]
    for i in range(len(cipher)):
        ret += decrypt_char(cipher[i], key[i % len(key)], iv)
        iv = cipher[i]

    return ret


def extract_key(cipher):
    key = [''] * 13
    recog_char = '|'
    key_len = 13
    len_c = len(cipher)
    recog_char_pos = len_c - 13 - 1

    recog_key = decrypt_char(cipher[recog_char_pos],
                             recog_char,
                             cipher[recog_char_pos - 1])
    key[(recog_char_pos - 1) % key_len] = recog_key

    # {applied_key_pos: (cipher_pos, extracted_key_pos)}
    key_encrypted_map = {i % 13: (i, e) for e, i in enumerate(range(len_c - 1 - 13, len_c - 1))}

    last_extract_key = 8
    for _ in range(12):
        cipher_char_pos, next_key_pos = key_encrypted_map[last_extract_key]
        cipher_char_pos = cipher_char_pos + 1
        next_key_char = decrypt_char(cipher[cipher_char_pos],
                                     key[last_extract_key],
                                     cipher[cipher_char_pos - 1])
        key[next_key_pos] = next_key_char
        last_extract_key = next_key_pos

    ret = ''
    for c in key:
        ret += c

    return ret


with open('encrypted.txt') as f:
    encrypted = f.readline()

cipher = encrypted.strip().decode('hex')

print(decrypt(extract_key(cipher), cipher))
