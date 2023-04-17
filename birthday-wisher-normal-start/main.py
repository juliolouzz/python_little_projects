# Import required modules
from datetime import datetime  # Import datetime module to get the current date
import pandas as pd  # Import pandas module to read CSV files
import random  # Import random module to select a random email template
import smtplib  # Import smtplib module to send emails

# Set the sender's email and password
my_email = ""  # Set the sender's email address
password = ""  # Set the sender's email password

# Get the current date
today = datetime.now()  # Get the current date and time
today_tuple = (today.month, today.day)  # Get the current month and day as a tuple

# Read the birthday data from a CSV file and create a dictionary of birthdays
data = pd.read_csv("birthdays.csv")  # Read the birthday data from a CSV file using pandas
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}
# Convert the data into a dictionary where the key is a tuple of (month, day) and the value is the row of data

# Check if there is a birthday on the current day
if today_tuple in birthdays_dict:
    # If there is a birthday, select a random email template and fill in the name of the birthday person
    birthday_person = birthdays_dict[today_tuple]  # Get the row of data corresponding to the current date
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"  # Select a random email template file
    with open(file_path) as letter_file:  # Open the email template file
        contents = letter_file.read()  # Read the contents of the email template file
        contents = contents.replace("[NAME]", birthday_person[
            "name"])  # Replace the [NAME] placeholder with the birthday person's name

    # Send the birthday email using the SMTP server
    with smtplib.SMTP("smtp.gmail.com") as connection:  # Connect to the SMTP server
        connection.starttls()  # Start a secure connection
        connection.login(my_email, password)  # Log in to the SMTP server
        connection.sendmail(from_addr=my_email,  # Send the email
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n{contents}")

# to make the program run every day, use pythonanywhere.com, create an account, upload the files,
# create a folder for the letter templates, upload the letter templates
# go to bash in the site, write the command python3 main.py
# to make run every day, go to tasks and add this command python3 main.py
# set hour to run the program
# save? and every day in that hour this code will run
