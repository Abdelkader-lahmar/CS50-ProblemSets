months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ")
    if len(date.split("/")) == 3:
        date = date.split("/")
        try:
            for _ in range(3):
                date[_] = int(date[_])
        except ValueError:
            pass
        else:
            if 0 <= date[0] <= 12 and 0 <= date[1] <= 31:
                print(f"{date[2]:04}-{date[0]:02}-{date[1]:02}")
                break
    elif len(date.split(" ")):
        date = date.split(" ")
        if len(date) == 3:
            try:
                date[1], date[2] = int(date[1][:date[1].index(",")]), int(date[2])
            except ValueError:
                pass
            else:
                if date[0] in months and 0 <= date[1] <= 31:
                    print(f"{date[2]:04}-{(months.index(date[0]) + 1):02}-{date[1]:02}")
                    break
