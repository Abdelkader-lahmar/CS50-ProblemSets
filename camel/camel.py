name = input("camelCase: ")
for char in name:
    if char.isupper():
        char = "_" + char.lower()
    print(char, end="")

# if you want to save the snake_name
# new_name = ""
# for i in range(len(name)):
#     if name[i].isupper():
#         new_name += "_"
#     new_name += name[i]
# print(new_name)
