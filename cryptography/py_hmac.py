import hmac
import hashlib

def calc_digest(key, message):
    key = bytes(key, 'utf-8')
    message = bytes(message, 'utf-8') 
    dig = hmac.new(key, message, hashlib.md5)
    return dig.hexdigest()

print(calc_digest('6465', 'Hello'))