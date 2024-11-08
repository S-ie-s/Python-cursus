# write the divide() function

def divide(num1, num2):
    num3 = num1 // num2
    num_remainder = num1 % num2

    print(num1, "divided by", num2, "equals", num3,
           " with a remainder of", num_remainder)


def main():
    divide(5, 2)
    divide(6, 3)
    divide(12, 5)
    divide(1, 2)

main()