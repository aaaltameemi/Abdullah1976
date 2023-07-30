#!/usr/bin/env python3

'''
# Author name :Abdullah Altameemi
# Project Description: Creating Apache in the entrprice envirnoment hosting web to process the  request that recieve by web server .
# Author email:aaaltameemi@madisoncollege.com
'''
import sys
import subprocess
import argparse

# create a new function using subprocess module
def IPAddressCount(fname):
    # we used capture_output , text attributes here to get the result as a string to save it on file later
    return subprocess.run(f"cat {fname} | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5",shell=True,capture_output=True,text=True)


def main():
 
    # Create an ArgumentParser instance
    parser = argparse.ArgumentParser()
    # Add a required 'filename' argument with short and long flags
    parser.add_argument('-f', '--filename', type=str, required=True, help='Enter an apache name file to process')
    
    # Parse arguments
    args = parser.parse_args()
    print("Analyze an apache web log. We will look to see if there is anyone trying to hack our website")

    # call the IPAddressCount function and access 'filename' argument value
    entryLogs = IPAddressCount(args.filename)

    # printing out the result of function 
    print(entryLogs.stdout)

    # create file and add to it the result of IPAddressCount    
    with open("apache_analysis.txt","w") as file:
        file.write(entryLogs.stdout) # stdout to get the output from the command 


# to run main function only when called directly
if __name__ == '__main__':
    main()

