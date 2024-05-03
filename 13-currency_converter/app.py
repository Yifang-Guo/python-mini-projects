def main():
    print("This program converts US dollars to Pounds Sterling")

    dollars = eval(input("Enter amount in dollars: "))

    pounds = converts_to_pounds(dollars)

    print(f"That is {pounds}.")

converts_to_pounds = lambda dollars : dollars * .82

main()