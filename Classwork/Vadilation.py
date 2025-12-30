#NAME VADILATION

import re

name=input("Enter the name:")
pattern=r'^[A-Za-z]{2,25}( [A-Za-z]{2,25})+$'
res=bool(re.fullmatch(pattern,name))
print(res)

#EMAIL VADILATION

import re

email=input("Enter the email: ")
pattern=r'^[a-zA-Z0-9.-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
res = bool(re.fullmatch(pattern, email))
print(res)

#PHONENUMBER VADILATION

import re
phnno=input("Enter the phone number:")
pattern=r'^(?:\+91|91)?[6-9]\d{9}$'

res = bool(re.fullmatch(pattern,phnno))
print(res)

#PASSWORD VADILATION

import re
password=input("Enter the password:")
pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
res=bool(re.fullmatch(pattern,password))
print(res)
