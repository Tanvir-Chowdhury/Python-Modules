import secrets
from string import digits, ascii_letters

#genereting normal functions
print(secrets.choice('Choos one from this string'.split()))
print(secrets.randbelow(1000))
print(secrets.randbits(16))

#genereting tokens
print(secrets.token_hex(32))
print(secrets.token_bytes(16))
print(secrets.token_urlsafe(32))

#genereting password
def genereting_pwd(length=8):
    chars = digits + ascii_letters
    return ''.join(secrets.choice(chars) for _ in range(length))

def genereting_sec_pwd(length=16, upper=3, digit=1):
    if length<upper + digit + 1:
        raise ValueError('Nice Try!')
    while True:
        pwd = genereting_pwd(length)
        if any(c.islower() for c in pwd) and (sum(c.isupper() for c in pwd)) >= upper and (sum(c.isdigit() for c in pwd)) >= digit :
            return pwd

print(genereting_pwd())
print(genereting_sec_pwd())