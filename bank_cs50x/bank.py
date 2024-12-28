from cs50 import get_string

user = get_string("Greeting: ").lower().lstrip()

try:
    index = user.index("h")
    if index == 0:
        if "hello" in user:
            print("$0")
        else:
            print("$20")
    else:
        print("$100")
except ValueError:
    print("$100")
