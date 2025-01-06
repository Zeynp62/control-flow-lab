# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

def is_vowel(alpha1):
    vowel ="The letter x is a vowel"
    consonant="The letter x is a consonant"
    if(alpha1=="a" or alpha1=="e" or alpha1=="i" or alpha1=="u" or alpha1=="o" or alpha1=="A" or alpha1=="O" or alpha1=="I" or alpha1=="E" or alpha1=="U"):
        print(vowel.replace("x",alpha1))
        
    else:
        print(consonant.replace("x",alpha1))

alpha = input("Please enter a letter from the alphabet (a-z or A-Z) ")
is_vowel(alpha)
