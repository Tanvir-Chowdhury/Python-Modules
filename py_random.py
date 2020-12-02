import random

print(random.random()) # prints random numbers

print(random.uniform(1, 10)) # prints random numbers between 1-10

print(random.randint(1, 10)) # prints random int numbers between 1-10

greetings = ["hi", "hello", "hola", "howdy"]
greet = random.choice(greetings)                # random from a list
print(f"{greet}! Tanvir")

colors = ["red", "green", "blue"]
print(random.choices(colors, k=5))  # prints random 5 times in a list

colors2 = ["red", "green", "blue"]
print(random.choices(colors2, weights=[10,8,4], k=10)) # same as colors but weights means percentage

numbers = list(range(50))
print(numbers)              
random.shuffle(numbers)     # shuffles the whole list
print(numbers)