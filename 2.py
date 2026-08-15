import random
import string



print ("Welcome to the Password Generator!")

Password_num = int(input('Enter the total number of characters in the password: '))

letters = int(input('Enter the number of letters in the password: '))
numb = int(input('Enter the number of numbers in the password: '))
symbo = int(input('Enter the number of symbols in the password: '))



if (letters + numb + symbo) != Password_num:
  print ("Invalid input. The sum of letters, numbers, and symbols doesn't match the password")

else :
  password_chars =( 
    random.choices(string.ascii_letters , k = letters) +
    random.choices(string.digits , k = numb) +
    random.choices(string.punctuation , k = symbo))
  
  random.shuffle(password_chars)

  password = ''.join(password_chars)

  print("Generated password: ",password)