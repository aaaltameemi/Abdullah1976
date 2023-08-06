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
    # open the .credentials-vt file , and get the value of your api-key
    with open(".credentials-vt",'r') as file:
        api_key = file.readline().strip()
        # split the line by = to get the value of the variable
        api_key = api_key.split("=")[1]

    # dictionary with a key of ‘x-apikey’ and a value of your api key from Virus Total
    headerVariable = {
        'x-apikey':api_key
    }
    print(f"https://virustotal.com/api/v3/ip_addressses/{ip_address}")    
    # Capture the  http response , and return that response it text manner
    # Add the header argument to your url request.
    returned_data = requests.get(f"https://virustotal.com/api/v3/ip_addresses/{ip_address}",headers=headerVariable).text
    return returned_data

def main():
    
    # Create an ArgumentParser instance
    parser = argparse.ArgumentParser()
    # Add a required 'filename' argument with short and long flags
    parser.add_argument('-f', '--filename', type=str, required=False, help='Enter an apache name file to process')
    # Add a continue flag argument with choices of y , n 
    parser.add_argument('-c', '--continues', choices=['y', 'n'], default="n", help='Choose yes (y) or no (n)')
    # Parse arguments
    args = parser.parse_args()
    if args.filename:
        # call the IPAddressCount function and access 'filename' argument value
        entryLogs = IPAddressCount(args.filename)
    # check if continues argument its equal to y , it's read the m5-access.log
    elif args.continues == 'y':
        entryLogs = IPAddressCount("m5-access.log")
        print("This script will read Apache log entries and analyze them.\n\nYou chose y, so will continute")
    
    # it ends the program if the user passed n.
    else:
        print("You chose n to end the program end bye.")
        sys.exit()
    
    # splitted strings 
    returned_logs = entryLogs.stdout.split("\n")
    # clear most of the tabs from every line
    returned_logs = [x.strip() for x in returned_logs if x != ""]

    # get the last element and split it with a space 
    most_requested_ip = returned_logs[-1].split(" ")

    # print("Analyze an apache web log. We will look to see if there is anyone trying to hack our website")
    print(most_requested_ip[1])

    # Capture the response in a variable
    response = IPLookup(most_requested_ip[1])


    # print the first 250 characters of the response
    # print(response[:250])

    # got response as text , then Parse and print the response
    response = json.loads(response)
    # a single line that prints the dictionary
    # print(json.dumps(response,indent=4))

    # find information about the IP Address
    print("Bitdefender category: " + response['data']['attributes']['last_analysis_results']['BitDefender']['category'])
    # for k in response:
        # if k == "city" or k == "org":
        #     print(f"... IP {k.upper()} : {response[k]}")

    # create file and add to it the result of IPAddressCount    
    with open("apache_analysis.txt","w") as file:
        file.write(entryLogs.stdout) # stdout to get the output from the command 
    
    # Use Beautiful Soup to Get Information about that IP
    # myHtml = bs4.BeautifulSoup(response,features="html.parser")
    # print(myHtml.find_all("dd",class_="col-8 text-monospace")[1].text)
    

# to run main function only when called directly
if __name__ == '__main__':
    main()
