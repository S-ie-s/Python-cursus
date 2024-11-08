

# Modify the main() function so that it:
# A. Prompts the user to enter a phrase.
# B. Tells the user what phrase they entered (e.g., Your phrase is 'Hello, World!').
# C. Prompts the user for a number.
# D. Tells the user what character is at that position in the user’s phrase (e.g., Character
# 4 is o).
# 3. Here is the program completed by the user:
# Choose a phrase: Hello, world!
# Your phrase is 'Hello, world!'
# Which character? [Enter number] 4
# Character 4 is o



def main():
    phrase = input("Enter a phrase: ")
    print(phrase)
    index = int(input("Enter a number "))
    print("Character", phrase[index-1], " is on position number", index)
    pass # Replace this line with your code

main()