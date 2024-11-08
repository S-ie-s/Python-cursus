# Modify the main() function so that it:
# A. Prompts the user to enter a phrase.
# B. Tells the user what phrase they entered (e.g., Your phrase is 'Hello, World!').
# C. Prompts the user for a start number.
# D. Prompts the user for a end number.
# E. Tells the user the substring (within single quotes) that starts with the start number
# and ends with the end number.
# 3. Here is the output of the program:
# Choose a phrase: Hello, world!
# Your phrase is 'Hello, world!'
# Character to start with? [Enter number] 4
# Character to end with? [Enter number] 9
# Your substring is 'o, wor'


def main():
    phrase = input("Choose a phrase: ")
    print("Your phrase is:", phrase)
    start_num = int(input("Start number? "))
    end_num = int(input("End number? "))
    print("Your substring is", phrase[start_num-1:end_num])
    # Write your code here

main()