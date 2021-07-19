
'''genrating a random password that contains at least one lowercase letter, one upper
case letter, one digit, and one special character'''

import random # allows you to take the variable from the "chars" function
import string

def randomPassword (length=10):#creating a functiom that will genarate a password
    # with 12 characters
    '''making the password to be harder by adding alphabets, lowercases and uppercases
    and a few extra signs and making them longer by 12 length'''
    randomSource = string.ascii_letters +string.digits +string.punctuation
    password = random.choice(string.ascii_lowercase)
    password += random.choice(string.ascii_uppercase)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)
  #Characters we put into apostrophes in the 3rd strp are what is going to make up our password 
    for i in range(10):# the number of password: its length is 12
        password += random.choice(randomSource)# password containing  lowercase,uppercase,digits and punctuations
        
    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = "".join(passwordList) 
    return password

print("First Random Password is", randomPassword())


    

def upper_lower(password):
    
    
    case ={'upper':0, 'lower':0}
    for letter in randomPassword:
        if letter.isupper:
            case['upper']= case['upper']+1
        if letter.islower:
            case['lower'] = case['lower'] +1
print(password)