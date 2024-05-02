def add(a, b):
    answer = a + b
    print(f"{a} + {b} = {answer}")

def sub(a, b):
    answer = a - b
    print(f"{a} - {b} = {answer}")

def mul(a, b):
    answer = a * b
    print(f"{a} * {b} = {answer}")

def div(a, b):
    answer = a / b
    print(f"{a} / {b} = {answer}")

while True:
    print("A. addition")
    print("B. subtraction")
    print("C. multiplication")
    print("D. division")
    print("E. exit")

    choice = input("Enter your choice: ")

    if choice == "a" or choice == "A":
        print("addition")
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        add(a, b)
    elif choice == 'b' or choice == 'B':
        print("subtraction")
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        sub(a, b)
    elif choice == 'c' or choice == 'C':
        print("multiplication")
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        mul(a, b)
    elif choice == 'd' or choice == 'D':
        print('division')
        a = int(input("enter first number: "))
        b = int(input("enter second number: "))
        div(a, b)
    elif choice == 'e' or choice == 'E':
        print('program ended')
        quit()
