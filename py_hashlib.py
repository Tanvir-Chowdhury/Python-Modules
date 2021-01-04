import hashlib, binascii

#using blake2b algorithm
h = hashlib.blake2b()
h.update(b'Hash me')
h.update(b'now!')
print(h.hexdigest())
print(h.digest())
print(h.block_size)
print(h.digest_size)
print(h.name)
print(hashlib.blake2b(b'Hash me now!').hexdigest())

#using md5 algorithm
h = hashlib.md5()
h.update(b'hello')
print(h.hexdigest())

#making a password hash with salt
h = hashlib.pbkdf2_hmac('md5', b'Tanvir', b'6465', 1000)
print(binascii.hexlify(h))

