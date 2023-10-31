import random
import string

db = {}

# Generate short link
def generator(length=8):
    letters_and_numbers = string.ascii_letters + string.digits
    random_word = ''.join(random.choice(letters_and_numbers) for i in range(length))
    return 'mast.er/' + random_word

while True:
    print("1. Link Shortener\n0. Exit\n")
    start = int(input("Press>>"))

    if start == 1:
        input = input("Enter the URL: ")

        if user_input in db:
            print("Your link:", input)
            print("Shortened Link:", db[input])
        else:
            shortLink = generator()
            db[input] = shortLink
            print("Your link:", input)
            print("Shortened Link:", shortLink)

        print("Database>>", db)
    elif start == 0:
        print("Exit......!")
        break
    else:
        print("Invalid Option! Try Again.")
