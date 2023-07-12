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
#apache_log=
# opning the log file that want to process
apache_log_file=open('m4-access.log' , 'r')
#reading the log file 
apache_log= apache_log_file.read()

#print(apache_log)
#open text file 
apache_log_analysis = open('apache_analysis.txt', 'w')
#spliting entry log 
apache_log_entries = apache_log.split( '\n')
#print(apache_log_entries)

#looping through each entry in the list of log apach_log_entries
for entry in apache_log_entries:
   # print(entry)
    #grapping the first 16 character og the log entry whhich is IP address
    #ip_address = entry[0:15:1]
    
    #split the string to get the return code
    apache_log_entry_items = entry.split(' ')
    #extract the IP address
    ip_address = apache_log_entry_items[0]
    return_code = apache_log_entry_items[8]
    summary=(f"{ip_address} - {return_code}")
    print(summary)
    #write to the txt file 
    apache_log_analysis.write(summary + "\n")

#close the text file to prevent overwritten
apache_log_analysis.closed()  


    
    

                    



    
    
    


