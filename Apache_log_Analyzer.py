#!/usr/bin/env python3

'''
# Author name :Abdullah Altameemi
# Project Description: Creating Apache in the entrprice envirnoment hosting web to process the  request that recieve by web server .
# Author email:aaaltameemi@madisoncollege.com
'''
import sys
import subprocess
import argparse
import requests
import bs4
import json

# create a new function using subprocess module
def IPAddressCount(fname):
    # we used capture_output , text attributes here to get the result as a string to save it on file later
    return subprocess.run(f"cat {fname} | cut -d ' ' -f1 | sort -n | uniq -c | sort -n | tail -n5",shell=True,capture_output=True,text=True)

# create a new function to use requests module, it takes single argument 
def IPLookup(ip_address):
    # Print the Response from the Function
    print(f"http://ipinfo.io/{ip_address}/json")

    # Capture the  http response , and return that response it text manner
    returned_data = requests.get(f"http://ipinfo.io/{ip_address}/json").text
    return returned_data

def main():
 
    
    # Create an ArgumentParser instance
    parser = argparse.ArgumentParser()
    # Add a required 'filename' argument with short and long flags
    parser.add_argument('-f', '--filename', type=str, required=True, help='Enter an apache name file to process')
    
    # Parse arguments
    args = parser.parse_args()

    # call the IPAddressCount function and access 'filename' argument value
    entryLogs = IPAddressCount(args.filename)

    # splitted strings 
    returned_logs = entryLogs.stdout.split("\n")

    # clear most of the tabs from every line
    returned_logs = [x.strip() for x in returned_logs if x != ""]

    # get the last element and split it with a space 
    most_requested_ip = returned_logs[-1].split(" ")

    print("Analyze an apache web log. We will look to see if there is anyone trying to hack our website")
    print(most_requested_ip[1])

    # Capture the response in a variable
    response = IPLookup(most_requested_ip[1])


    # print the first 250 characters of the response
    # print(response[:250])

    # got response as text , then Parse and print the response
    response = json.loads(response)
    for k in response:
        if k == "city" or k == "org":
            print(f"... IP {k.upper()} : {response[k]}")

    # create file and add to it the result of IPAddressCount    
    with open("apache_analysis.txt","w") as file:
        file.write(entryLogs.stdout) # stdout to get the output from the command 
    
    # Use Beautiful Soup to Get Information about that IP
    # myHtml = bs4.BeautifulSoup(response,features="html.parser")
    # print(myHtml.find_all("dd",class_="col-8 text-monospace")[1].text)


# to run main function only when called directly
if __name__ == '__main__':
    main()

