def main():
    time = input("What time is it? ").split(" ")
    if len(time) == 2 and time[1] == "p.m.":
        time = convert(time[0]) + 12
    else:
        time = convert(time[0])
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    hour, min = time.split(":")
    return int(hour) + int(min) / 60


if __name__ == "__main__":
    main()
