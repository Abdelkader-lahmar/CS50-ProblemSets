from csv import DictReader
from cs50 import SQL

db = SQL("sqlite:///roster.db")

with open("students.csv") as file:
    lists = DictReader(file)
    for li in lists:
        db.execute("INSERT INTO students (id, name) VALUES(?, ?)", li["id"], li["student_name"])
        try:
            db.execute("INSERT INTO houses (house, head) VALUES(?, ?)", li["house"], li["head"])
        except ValueError:
            pass
        db.execute("INSERT INTO relation (id, house) VALUES(?, ?)", li["id"], li["house"])
