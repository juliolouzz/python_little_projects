# import smtplib
#
# my_email = "julio.cdl.vet@gmail.com"
# password = "fmtouwiddychsrms"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="julio.louzano@icloud.com",
#                         msg="Subject:Hello\n\nThis is the body of my email.")
# connection.close()

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_the_week = now.weekday()
day = now.day
sec = now.second

date_of_birth = dt.datetime(year=1995, month=12, day=15)