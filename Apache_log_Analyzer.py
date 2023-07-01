#!/usr/bin/env python3

'''
#Author name :Abdullah Altameemi
#Project Description: Creating Apache in the entrprice envirnoment hosting web to process the  request that recieve by web server .
#Author email:aaaltameemi@madisoncollege.com  

'''
#create welcome message about the script and print it to the screen .
welcome_message ="welcome to Apache analyzer!"
print(welcome_message)
user_message=input("would like to continue?please enter your 'y' for yes amd 'n for No: ")
print(user_message)
#creat string variable
apache_log='111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"'

IP_address=apache_log[0:15]

print(f"log format request:***{IP_address}***")
#spilt filed s of the  apache log entry .
fields=apache_log.split(' ')
#create fields type.
fields_type=type(fields)
#create return ode
return_cod=fields[8]
print(f"return code: {return_cod}")
