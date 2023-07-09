#!/usr/bin/env python3

'''
#Author name :Abdullah Altameemi
#Project Description: Creating Apache in the entrprice envirnoment hosting web to process the  request that recieve by web server .
#Author email:aaaltameemi@madisoncollege.com  

'''
#create welcome message about the script and print it to the screen .
welcome_message ="welcome to Apache analyzer!"
print(welcome_message)
#user_message=input("would like to continue?please enter your 'y' for yes amd 'n for No: ")
#print(user_message)
#create apache log with multiple lines
apache_log="""111.222.333.123 HOME - [01/Feb/1998:01:08:39 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 198 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)" 
111.222.333.124 HOME - [01/Feb/1998:01:08:46 -0800] "GET /bannerad/ad.htm HTTP/1.0" 200 28083 "http://www.referrer.com/bannerad/ba_intro.htm" "Mozilla/4.01 (Macintosh; I; PPC)" 
111.222.333.125 AWAY - [01/Feb/1998:01:08:53 -0800] "GET /bannerad/ad7.gif HTTP/1.0" 401 9332 "http://www.referrer.com/bannerad/ba_ad.htm" "Mozilla/4.01 (Macintosh; I; PPC)" 
111.222.333.126 AWAY - [01/Feb/1998:01:09:14 -0800] "GET /bannerad/click.htm HTTP/1.0" 501 207 "http://www.referrer.com/bannerad/menu.htm" "Mozilla/4.01 (Macintosh; I; PPC)" """

#print(apache_log)
#spliting the log to single log
apache_log_entries=apache_log.split('\n')
#print(apache_log_entries)
for entry in apache_log_entries:
    #print(entry)
    #create ip address for the apache log
    ip_address=entry[0:15:1]
    print(f"log request from:{ip_address:*^22s}")
    #Split the apache log to the items
    apache_log_field=apache_log.split(' ')
   #create return code 
    return_code=apache_log_field[8]
    print(f'Return code:{return_code}')



