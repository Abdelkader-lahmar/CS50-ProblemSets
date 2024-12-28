-- Keep a log of any SQL queries you execute as you solve the mystery.
.tables --to know mor about database and the tables inside of it
.schema --to get more information about tables
SELECT * FROM crime_scene_reports; --taking a look in crime_scene_reports table
SELECT * FROM crime_scene_reports WHERE street = 'Humphrey Street' AND year = 2023 AND month = 7 AND day = 28; --searching for tne crime to get exact information i need
.schema bakery_security_logs --thinking that the theif went to bakery so getting know more about it
SELECT * FROM bakery_security_logs WHERE year = 2023  AND month = 7 AND day = 28; --viewing logs for that day
.schema interviews
SELECT * FROM interviews WHERE year = 2023 AND month = 7 AND day = 28; --getting more information to know what is the next step and getting more clear view
.schema atm_transactions
SELECT * FROM atm_transactions WHERE year = 2023 AND month = 7 AND day = 28 AND atm_location = 'Humphrey Lane' AND transaction_type = 'withdraw'; --gathering more information
.schema flights
SELECT * FROM flights WHERE year = 2023 AND month = 7 AND day = 29; --see the flights where
--+----+-------------------+------------------------+------+-------+-----+------+--------+
--| id | origin_airport_id | destination_airport_id | year | month | day | hour | minute |
--+----+-------------------+------------------------+------+-------+-----+------+--------+
--| 36 | 8                 | 4                      | 2023 | 7     | 29  | 8    | 20     |
--this is the earliest flight out of Fiftyville so the theif is on it
.schema airports
SELECT * FROM airports WHERE id = 4; --to know where is the destination which is New York City
.schema passengers
SELECT * FROM passengers WHERE flight_id = 36; --to know passenger of this flight
.schema phone_calls
SELECT * FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration <= 60;
--now it time to serche for the thief
SELECT * FROM people WHERE
    phone_number IN (SELECT caller FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60)
    AND passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = 36)
    AND license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2023  AND month = 7 AND day = 28 AND hour = 10 AND minute BETWEEN 15 and 25)
    AND id IN (SELECT person_id FROM bank_accounts WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE year = 2023 AND month = 7 AND day = 28 AND transaction_type = 'withdraw' AND atm_location = 'Leggett Street'));
--the thef is Bruce now let serche for who helpt him
SELECT * FROM people WHERE phone_number IN (SELECT receiver FROM phone_calls WHERE year = 2023 AND month = 7 AND day = 28 AND duration < 60 AND caller = '(367) 555-5533');
-- and it's Robin
-- it take me a long time because of stupid mistakes i made
