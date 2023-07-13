#!/usr/bin/env python3

'''
#Author name :Abdullah Altameemi
#Project Description: Creating Apache in the entrprice envirnoment hosting web to process the  request that recieve by web server .
#Author email:aaaltameemi@madisoncollege.com  

'''
import sys
# create welcome message about the script and print it to the screen .
welcome_message ="welcome to Apache analyzer!"
print(welcome_message)
if len(sys.argv) > 1:
    user_message = sys.argv[1]
else:
    user_message =input("would like to continue?please enter your 'y' for yes amd 'n for No: ")

accptible_message =['y','yeah','yes']
if user_message.lower() in accptible_message:
    # print(user_message)
    # create apache log with multiple lines
    # apache_log=
    # opning the log file that want to process
    apache_log_file=open('m5-access.log' , 'r')
    # reading the log file 
    apache_log= apache_log_file.read()

    # print(apache_log)
    # open text file 
    apache_log_analysis = open('apache_analysis.txt', 'w')
    # spliting entry log 
    apache_log_entries = apache_log.split( '\n')
    # print(apache_log_entries)
    # Create an empty dictionary called apache_log_summary
    apache_log_summary = {}
    # looping through each entry in the list of log apach_log_entries
    for entry in apache_log_entries:
    # print(entry)
        # grapping the first 16 character og the log entry whhich is IP address
        # ip_address = entry[0:15:1]
        
        # split the string to get the return code
        apache_log_entry_items = entry.split(' ')
        # extract the IP address and return code
        ip_address = apache_log_entry_items[0]
        return_code = apache_log_entry_items[8]
        summary = (f"{ip_address} - {return_code}")

        # to check if it is exist in dictionary if not we equal it by 0
        # if it there ,then you will increment the value of that by 1.
        apache_log_summary[ip_address] = apache_log_summary.get(ip_address,0) + 1
        # to check if returned code greater than or eqaul to 400
        if return_code >= '400' :
            print(summary)
            
        # to check if returned code greater than or eqaul to 500
        if return_code >= '500':
            continue
else:
    print('You choosed not to continue and exiting the programe ...')

# loop throw dictionary
for key in apache_log_summary:
    # to check if IP Addresses have a count greater than or equal to 5
    if apache_log_summary[key] >= 5:
        # if true we write that to the file .
        apache_log_analysis.write(f"{key} has {apache_log_summary[key]}\n")
        
# close the text file to prevent overwritten
apache_log_analysis.close()  

        
        

                        



    
    
    


