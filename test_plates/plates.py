from string import punctuation


def main():
    plate = input("Input: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
        for i in range(len(s) - 1):
            if s[i].isdigit() and not s[i + 1].isdigit():
                return False
            elif s[i].isalpha() and s[i + 1] == "0":
                return False
        return True
    return False


# another version i tried using any():
# def is_valid(S)
#     if 2 <= len(s) <= 6 and s[0:2].isalpha() and s.isalnum():
#         if any((s[i].isdigit() and not s[i + 1].isdigit()) or (s[i].isalpha() and s[i + 1] == "0") for i in range(len(s) - 1)):
#             return False
#         return True
#     return False


if __name__ == "__main__":
    main()
