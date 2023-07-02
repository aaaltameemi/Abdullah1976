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
apache_log='''111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
111.222.333.124 HOME - [01/Feb/1998:01:08:46 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 28083 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
111.222.333.125 AWAY - [01/Feb/1998:01:08:53 -0800] "GET /bannerad/ad7.gif HTTP/1.0" 401 9332 "http://www.referrer.com/bannerad/ba_ad.htm" "Mozilla/4.01 (Macintosh; I; PPC)"
111.222.333.126 AWAY - [01/Feb/1998:01:09:14 -0800] "GET /bannerad/click.htm HTTP/1.0" 501 207 "http://www.referrer.com/bannerad/menu.htm" "Mozilla/4.01 (Macintosh; I; PPC)"'''

apache_log_list=apache_log.split('\n')
#loop through apache_log_list
for apache_log in apache_log_list:
    fields=apache_log.split(' ')
    IP_address=fields[0]
    return_code1=200
    return_code2=401
    return_code3=501
print(f"log request from:{IP_address} \nReturn code:{return_code1}")
print(f"log request from:{IP_address} \nReturn code:{return_code1}") 
print(f"log request from:{IP_address} \nReturn code:{return_code2}")
print(f"log request from:{IP_address} \nReturn code:{return_code3}")
