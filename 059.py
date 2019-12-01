from string import ascii_lowercase as lowercase


with open('cipher.txt') as fi:
    s = fi.read()
crypt = [int(x) for x in s.split(',')]

def try_decrypt(password, display=False):
    key = map(ord, (500 * password)[:len(crypt)])
    new = [c[0] ^ c[1] for c in zip(crypt, key)]
    text = ''.join(map(chr, new))
    if display:
        print(password, sum(new))
        print(text)
    else:
        return(text.count(' '))

ms = 0
for a in lowercase:
    for b in lowercase:
        for c in lowercase:
            s = try_decrypt(a + b + c)
            if s > ms:
                ms = s
                password = a + b + c

try_decrypt(password, True)
