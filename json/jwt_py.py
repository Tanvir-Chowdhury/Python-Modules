import jwt

data = {'payload' : 'Data', 'Id': 123}

token = jwt.encode(data, '6465')
data_out = jwt.decode(token, '6465')
print(data_out)
print(token)