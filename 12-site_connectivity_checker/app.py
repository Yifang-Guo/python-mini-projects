from urllib.request import urlopen
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

def main(url):
    print("Checking connectivity ")

    response = urlopen(url)
    print(f"Connected to {url} successfully")
    print(f"the response code was: {response.getcode()}")

print("This is a site connectivity checker program")
input_url = input("Input the url of the site you want to check: ")
main(input_url)

