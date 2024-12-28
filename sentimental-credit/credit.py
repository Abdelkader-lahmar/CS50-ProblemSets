from cs50 import get_string


def main():
    credit = get_string("Number: ")
    lenght = len(credit)
    if lenght > 16 or lenght < 13:
        print("INVALID")
        return
    type = check_type(credit, lenght)
    if type == "INVALID":
        print("INVALID")
        return
    if isit_valid(credit, lenght) == 0:
        print(type)
        return
    print("INVALID")
    return


def check_type(credit, lenght):
    if credit[0] == '4':
        return "VISA"
    elif lenght == 15:
        if credit[0] == "3" and (credit[1] == "4" or credit[1] == "7"):
            return "AMEX"
        else:
            return "INVALID"
    elif lenght == 16:
        if credit[0] == '5' and (credit[1] in ["1", '2', '3', '4', '5']):
            return "MASTERCARD"
        else:
            return "INVALID"
    else:
        return "INVALID"


def isit_valid(credit, lenght):
    sum = 0
    for i in range(1, lenght, 2):
        num = int(credit[lenght - i - 1]) * 2
        sum += (num % 10) + int(num / 10)
    for i in range(0, lenght, 2):
        sum += int(credit[lenght - i - 1])
    return sum % 10


main()
