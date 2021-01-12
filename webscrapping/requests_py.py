import requests

response = requests.get("https://xkcd.com/353/")
print(dir(response))

#downloading a picture
r = requests.get("https://imgs.xkcd.com/comics/python.png")
print(r.ok) #Checking if the response is success or not.
print(r.status_code) #Checking the status code to insure the success.
print(r.headers) #checking the details of the png picture.
'''with open("comic.png", "wb") as f:
    f.write(r.content)'''

# get method
payload = {"page" : 2, "count" : 25}
r2 = requests.get("https://httpbin.org/get", params=payload)
print(r2.url) #printing the url with payloads.
print(r2.text) #printing whole info.

#post method
payload2 = {"username": "Tanvir", "password" : 123456}
r3 = requests.post("https://httpbin.org/post", data=payload2)
print(r3.text)