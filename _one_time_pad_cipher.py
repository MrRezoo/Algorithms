"""
    One Time Pad cipher
"""

import random


class OneTime:
    @staticmethod
    def encrypt(text):
        plain = [ord(i) for i in text]
        key = []
        cipher = []
        for i in plain:
            k = random.randint(1, 300)
            c = (i + k) * k
            cipher.append(c)
            key.append(k)
        return cipher, key

    @staticmethod
    def decrypt(cipher, key):
        plain = []
        for i in range(len(key)):
            p = int((cipher[i] - key[i] ** 2) / key[i])
            plain.append(chr(p))
        result = ''.join([i for i in plain])
        return result


c, k = OneTime().encrypt('reza')
print(c)
print(k)

print(OneTime().decrypt(c, k))
