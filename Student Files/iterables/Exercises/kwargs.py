def greet_me(**kwargs):
    print(type(kwargs))
    print(kwargs)

def main():
    greet_me(a=1,b=2,c=3)

main()