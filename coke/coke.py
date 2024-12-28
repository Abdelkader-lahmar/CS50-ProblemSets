due = 50
while due > 0:
    print(f"Amount Due: {due}")
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        due -= coin
print(f"Change Owed: {due * -1}")
