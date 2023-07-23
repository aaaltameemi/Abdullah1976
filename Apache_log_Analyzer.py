#!/usr/bin/env python3

'''
#Author name :Abdullah Altameemi
#Project Description: Creating Apache in the entrprice envirnoment hosting web to process the  request that recieve by web server .
#Author email:aaaltameemi@madisoncollege.com  

'''
import sys
import subprocess 
# create a new function using subprocess module
def IPAddressCount(fname):
    # we used capture_output , text attributes here to get the result as a string to save it on file later
    return subprocess.run(f"cat {fname} | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5",shell=True,capture_output=True,text=True)

def main():
    # create welcome message about the script and print it to the screen .
    welcome_message ="welcome to Apache analyzer!"
    print(welcome_message)
    if len(sys.argv) > 1:
        user_message = sys.argv[1]
    else:
        user_message =input("would like to continue?please enter your 'y' for yes amd 'n for No: ")

    # a list to possible values while agree
    accptible_message =['y','yeah','yes']
    # a condition to check of the user_message after we lower it , is in the list or not
    if user_message.lower() in accptible_message:
        print(f"You chose {user_message}, so will continue ")
        # call the IPAdressCount function with file name 
        entrylogs = IPAddressCount ('m5-access.log')
        #printing out the result of the function
        print(entrylogs.stdout)
        # create file and add to it the result of IPAddressCount    
        with open("apache_analysis.txt","w") as file:
            file.write(entrylogs.stdout) # stdout to get the output from the command 
        
# to run main function only when called directly
if __name__ == '__main__':
    main()

        
        

                        



    
    
    


