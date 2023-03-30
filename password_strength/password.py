#from django.test import TestCase

# Create your tests here.



import re

password=input("Please enter password: ")

score=0

if len(password)>8:
    score+=1

result=re.search(r'[A-Z]',password)
if result:
    score+=1

result2=re.search(r'[a-z]',password)
if result2:
    score+=1

result3=re.search(r'[1-9]',password)
if result3:
    score+=1

result4=re.search(r'[!@#$%^&*({[:/.,?<>})]',password)
if result4:
    score+=1


if score==5:
    print("Very Strong password")
elif score==4:
    print("Strong Password")
elif score==3:
    print("Moderate password")
elif score==2:
    print("Weak Password")
else:
    print("very weak password")

#--------------------------------------------------------

def password_check(password):
    score=0
    if len(password)>8:
        score+=1
    result=re.search(r'[A-Z]',password)
    if result:
        score+=1
    result2=re.search(r'[a-z]',password)
    if result2:
        score+=1
    result3=re.search(r'[1-9]',password)
    if result3:
        score+=1
    result4=re.search(r'[!@#$%^&*({[:/.,?<>})]',password)
    if result4:
        score+=1
    
    if score==5:
        strength="Very Strong password"
    elif score==4:
        strength="Strong Password"
    elif score==3:
        strength="Moderate password"
    elif score==2:
        strength="Weak Password"
    else:
        strength="very weak password"

    return strength



password=input("Please enter password: ")

pwd=password_check(password)  
print(pwd)