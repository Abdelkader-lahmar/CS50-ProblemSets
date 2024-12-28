from string import digits

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        for i in range(len(s) - 1):
            if s[i].isdigit():
                if s[i+1].isalpha():
                    return False
            elif s[i + 1] == "0":
                return False
        return True
    else:
        return False

main()
