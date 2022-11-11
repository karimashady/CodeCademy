# https://docs.python.org/3/library/csv.html#id3
# Name	Username	Email
#Roger Smith	rsmith	wigginsryan@yahoo.com
#Michelle Beck	mlbeck	hcosta@hotmail.com
#Ashley Barker	a_bark_x	a_bark_x@turner.com
#Lynn Gonzales	goodmanjames	lynniegonz@hotmail.com
#Jennifer Chase	chasej	jchase@ramirez.com
#Charles Hoover	choover	choover89@yahoo.com
#Adrian Evans	adevans	adevans98@yahoo.com
#Susan Walter	susan82	swilliams@yahoo.com
#Stephanie King	stephanieking	sking@morris-tyler.com
#Erika Miller	jessica32	ejmiller79@yahoo.com

import json
import csv

compromised_users= []

with open('passwords.csv') as password_file:
  password_csv = csv.DictReader(password_file)
  for password_row in password_csv:
    compromised_users.append(password_row['Username'])

with open('compromised_users.txt', 'w') as compromised_user_file:
  for compromised_user in compromised_users:
    compromised_user_file.write(compromised_user)

with open('boss_message.json', 'w') as boss_message:
  boss_message_dict = {'recipient': 'The Boss' ,'message': 'Mission Success' }
  json.dump(boss_message_dict, boss_message)

with open('new_passwords.csv', 'w') as new_passwords_obj:
  slash_null_sig = "shit, u got hacked :/"
  new_passwords_obj.write(slash_null_sig)
