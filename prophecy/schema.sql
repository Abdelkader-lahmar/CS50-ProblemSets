CREATE TABLE students(
id INTEGER NOT NULL,
name TEXT NOT NULL,
PRIMARY KEY(id));

CREATE TABLE houses (
house TEXT NOT NULL,
head TEXT NOT NULL,
PRIMARY KEY(house));

CREATE TABLE relation (
id INTEGER,
house TEXT,
FOREIGN KEY (id) REFERENCES students(id),
FOREIGN KEY (house) REFERENCES houses(house));

CREATE UNIQUE INDEX house_head ON houses(head);
