import random

def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

uppercase_letter_1 = chr(random.randint(65,90))
uppercase_letter_2 = chr(random.randint(65,90))


lowercase_letter_1 = chr(random.randint(97,122))
lowercase_letter_2 =chr(random.randint(97,122))


digit_1 = chr(random.randint(48,57))
digit_2 = chr(random.randint(48,57))


special_letter_1 = chr(random.randint(33,125))
special_letter_2 = chr(random.randint(33,125))

password = uppercase_letter_1+uppercase_letter_2+lowercase_letter_1+lowercase_letter_2+digit_1+digit_2+special_letter_1+special_letter_2
password = shuffle(password)
print("Password is ",password)