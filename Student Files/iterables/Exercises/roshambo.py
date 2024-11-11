import random

def main():
    pass # replace this with your code
    rps_seq = ['Rock', 'Paper', 'Scissors']
    random_rps = random.choice(rps_seq)
    user_choice = int(input("1 for rock, 2 for paper, 3 for scissors "))

    user_rps = rps_seq[user_choice - 1]
    
    
    print("computer: ", random_rps)
    print("user: ", user_rps)
hjfkyky
    
    
    

main()