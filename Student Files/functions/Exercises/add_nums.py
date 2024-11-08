def add_3_and_6():
    total = 3 + 6
    print('3 + 6 = ', total)

def add_10_and_12():
    total = 10 + 12
    print('10 + 12 = ', total)

def add_nums(number_one, number_two):
   
    total = number_one + number_two
    print(number_one, "+", number_two, " = ", total)

def input_nums():
    
    num1 = input("insert num 1:")
    num2 = input("insert num 2:")
    add_nums(int(num1), int(num2))
   # total = int(num1) + int(num2)
   # print(num1, "+", num2, "=", total)


def main():
 #1   add_3_and_6()
 #   add_10_and_12()
 #   add_nums(1,2)
    input_nums()

main()