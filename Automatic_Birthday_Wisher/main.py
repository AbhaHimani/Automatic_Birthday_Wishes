##################### Normal Starting Project ######################
import pandas
import random
import smtplib
from datetime import datetime
month=datetime.now().month
day= datetime.now().day
today=(month,day)

data=pandas.read_csv("birthdays.csv")

new_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today in new_dict:
    file_path=f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as file:
       person=new_dict[today]
       contents= file.read()
       contents.replace("[NAME]",person["name"])

my_email= "my_email@gmail.com"
password= "my_password"

connection= smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(my_email,password)
connection.sendmail(from_addr=my_email,to_addrs= person["email"] , msg=f"Subject:Monday Motivation \n \n {contents} ")


connection.close()


