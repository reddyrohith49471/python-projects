#RANDOM PASSWORD GENERATOR
#Designer :- REDDY ROHITH
import random as r
letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*0123456789")
r.shuffle(letters)
password = "".join(letters[0:6])
print("PASSWORD:-",password)
