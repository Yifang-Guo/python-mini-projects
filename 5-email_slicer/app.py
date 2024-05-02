#collect email from user
#split the email using the @, save the first part as the user name, the second part is gonna be saved domain
#split the domain using .


def main():
    print("Welcome to email slicer")

    email_input = input("Input your email address: ")

    username, domain = email_input.split("@")
    domain, extension = domain.split(".")

    print(f"user name: {username}, domain: {domain}, extension: {extension}")

main()
