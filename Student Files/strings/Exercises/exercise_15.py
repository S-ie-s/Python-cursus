import math


def print_out():
    answer ='y'
    while(answer == 'y'):
        company = input("Company name: ")
        revenue = input("Revenue: ")
        expenses = input("Expenses: ")
        
        answer = input("Would you like to add a new tab (press y) or quit(press q)")

    print(revenue, expenses )
    '{:,.2f}'.format(revenue)

def main():
    print_out()


main()