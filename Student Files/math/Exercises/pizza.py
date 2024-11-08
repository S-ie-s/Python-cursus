import math

# Ask how many people wat to eat pizza. How many slices per person 
# and how many slices you can get out of a pizza
#
def user_input():
    people = int(input("How many people? "))
    slices = int(input("How many slices eats a person? "))
    slice_per_pizza = int(input("How many slices per pizza? "))
    return people, slices, slice_per_pizza

# calculating how many pizza's are needed.
# calculating how many slices will be over
def calc_pizza(user_pizza_numbers):
    people, slices, slice_per_pizza = user_pizza_numbers

    total_pizza = (people * slices) / slice_per_pizza
    whole_pizza = math.ceil(total_pizza)
    rest_slices = (people * slices) % slice_per_pizza
    
    return whole_pizza, rest_slices

def print_out(print_result):
    whole_pizza, rest_slices = print_result
    print("You need :", whole_pizza, " pizza's")
    print("There will be ", rest_slices, "slices over")

def main():
    user_pizza_numbers = user_input()
    print_result = calc_pizza(user_pizza_numbers)
    print_out(print_result)

main()