import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()."

string = lower + upper + numbers + symbols
lenght = 16
password = "".join(random.sample(string,lenght))

print("your password is:" + password)