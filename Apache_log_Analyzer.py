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
with open ('m4-access.log','r') as File:
    apache_log_entries= File.readlines()

    #print(apache_log)
#create  writable File
writable_file = open("apache_analysis","w")
for entry in apache_log_entries:
    apache_log_field =entry.split(' ')
    #create return code
    return_code = apache_log_field[8]
    #print(entry)
    #create ip address for apache_log_entries
    ip_address = entry[0:15:1]
    
    writable_file.writelines(f"{ip_address}{return_code}")
    
    print(f"{ip_address} -{return_code}")



    
    
    


