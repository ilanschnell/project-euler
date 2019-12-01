from itertools import product, cycle


with open('cipher.txt') as fi:
    s = fi.read()
cipher = [int(x) for x in s.split(',')]

def try_decrypt(password, display=False):
    plain = bytes(a ^ b for a, b in zip(cipher, cycle(password)))
    if display:
        print(bytes(password), sum(plain))
        print(plain)
    else:
        return(plain.count(b' '))

max_spaces = 0
for p in product(range(97, 123), repeat=3):
    spaces = try_decrypt(p)
    if spaces > max_spaces:
        max_spaces = spaces
        password = p

try_decrypt(password, True)
