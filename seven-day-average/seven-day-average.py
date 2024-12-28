import csv
import requests


def main():
    # Read NYTimes Covid Database
    download = requests.get(
        "https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv"
    )
    decoded_content = download.content.decode("utf-8")
    file = decoded_content.splitlines()
    reader = csv.DictReader(file)

    # Construct 14 day lists of new cases for each states
    new_cases = calculate(reader)
    print(new_cases)

    # Create a list to store selected states
    states = []
    print("Choose one or more states to view average COVID cases.")
    print("Press enter when done.\n")

    while True:
        state = input("State: ")
        if state in new_cases:
            states.append(state)
        if len(state) == 0:
            break

    print(f"\nSeven-Day Averages")

    # Print out 7-day averages for this week vs last week
    comparative_averages(new_cases, states)


# TODO: Create a dictionary to store 14 most recent days of new cases by state
def calculate(reader):
    new_cases = {}
    prev_cases = {}
    for read in reader:
        state = read["state"]
        if state not in new_cases:
            new_cases[state] = [read["cases"]]
            prev_cases[state] = [read["cases"]]
        else:
            length = len(prev_cases[state])
            new_cases[state].append(int(read["cases"]) - int(prev_cases[state][length - 1]))
            prev_cases[state].append(int(read["cases"]))
        if len(new_cases[state]) == 15:
            new_cases[state].pop(0)
            prev_cases[state].pop(0)

    return new_cases

# TODO: Calculate and print out seven day average for given state
def comparative_averages(new_cases, states):
    new_week = {}
    prev_week = {}
    for state in states:
        new_week[state] = int(sum(new_cases[state][7:]) / 7)
        prev_week[state] = int(sum(new_cases[state][0:7]) / 7)
        try:
            (new_week[state] / prev_week[state]) - 1
        except ZeroDivisionError:
            if new_week[state] == 0:
                return print(f"{state} had no new cases")
            else:
                return print(f"{state} had {sum(new_cases[state][7:])} new cases")
        perc = round(((new_week[state] / prev_week[state]) - 1) * 100, 2)
        if perc > 0:
            stat = "increase"
        else:
            stat = "decrease"
            perc *= -1
        print(f"{state} had a 7-day average of {new_week[state]} and a {stat} of {perc}%.")


main()
