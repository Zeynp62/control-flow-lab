# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age in human years like this:
#      Input a dog's age in human years: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hint:  Use the int() function to convert the string returned from input() into an integer

def to_dog_age (a):
    if a<3:
        x=a*10
        print(f"The dog's age in dog years is {x}")
    else:
        x=20+((a-2)*7)
        print(f"The dog's age in dog years is {x}")


age = input("Input a dog's age in human years:")
to_dog_age(int(age))
