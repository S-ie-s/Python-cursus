import random

# You rolled a 3
# Total after first roll: 3
# You rolled a 5
# Total after 2 rolls: 8
# You rolled a 3
# Total after 3 rolls: 11
# Your average roll was 3.67
# Thanks for playing.

def user_input():
    total_rolls=int(input("How many times would you like to roll the dice? "))
    print("Okay, you would like to roll" + total_rolls + "times")
    return total_rolls

def roll_die(max_rolls):
    i= 0
    for i in max_rolls:

        die_number = random.randint(1,6)
        print("You rolled a", die_number)

def main():
    total_rolls =user_input()
    roll_die(total_rolls)

    roll = 0
    total = 0
    roll_die()
    roll +=1
    total+= roll
    print("\tyou rolled for the", total, "time")
    



main()