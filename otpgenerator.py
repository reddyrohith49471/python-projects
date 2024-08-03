#OTP GENERATOR
#Designer :- REDDY ROHITH
import random as r
num = int(input("Enter Number:-"))
numbers = list("0123456789")
r.shuffle(numbers)
otp = "".join(numbers[0:4])
print("YOUR OTP IS:-",otp)
