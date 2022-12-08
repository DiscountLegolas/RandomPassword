import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)


uppercaseLetter1=chr(random.randint(65,90)) 
uppercaseLetter2=chr(random.randint(65,90)) 
lowercaseLetter1=chr(random.randint(97,122)) 
lowercaseLetter2=chr(random.randint(97,122)) 
digit1=chr(random.randint(48,57)) 
digit2=chr(random.randint(48,57)) 
specialchar1=chr(random.randint(33,47)) 
specialchar2=chr(random.randint(33,47)) 


password = uppercaseLetter1 + uppercaseLetter2 +lowercaseLetter1+lowercaseLetter2+digit1+digit2+specialchar1+specialchar2
password = shuffle(password)

#Output
print(password)