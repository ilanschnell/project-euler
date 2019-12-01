from itertools import product, cycle


with open('cipher.txt') as fi:
    s = fi.read()
cipher = [int(x) for x in s.split(',')]

def try_decrypt(password, display=False):
    plain = bytes(a ^ b for a, b in zip(cipher, cycle(password)))
    if display:
        print('password:', bytes(password))
        print(plain)
        print('ascii sum:', sum(plain))
    return(plain.count(b' '))

max_spaces = 0
for p in product(range(ord('a'), ord('z') + 1), repeat=3):
    spaces = try_decrypt(p)
    if spaces > max_spaces:
        max_spaces = spaces
        password = p

try_decrypt(password, True)
