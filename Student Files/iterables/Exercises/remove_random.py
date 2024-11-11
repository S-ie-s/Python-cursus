import random

def remove_random(the_list):
    pass # replace this with your code
    print(the_list)
    random_color = random.choice(the_list)
    print(random_color)
    the_list.remove(random_color)
    print(the_list)

def main():
    colors = ['red', 'blue', 'green', 'orange']
    remove_random(colors)
    
    # Your code here

main()