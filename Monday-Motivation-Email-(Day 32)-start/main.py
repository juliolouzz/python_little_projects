import datetime as dt
import random
import smtplib


# Get the day of the week as a  number 0 to 6, 0 = monday and 6 = sunday

today = dt.datetime.today()
day_of_the_week = today.weekday()


# Open the txt file, put quotes in a list a random choose a quote from that list

with open("quotes.txt") as quotes_file:
    quotes = quotes_file.readlines()

lucky_quote = random.choice(quotes)
# could put the 3 above lines inside the if statement

# Send email to me with a quote every monday

my_email = "" # your email
password = "" # your password

if day_of_the_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Monday Motivation!\n\n{lucky_quote}")
    connection.close()



