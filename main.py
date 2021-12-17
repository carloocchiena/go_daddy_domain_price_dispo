import requests
import json
import time

# GoDaddyAPI Private Keys
ApiKey = "your ApiKey"
SecretKey = "your SecretKey"

# connecting to server
headers = {"Authorization" : "sso-key {}:{}".format(ApiKey, SecretKey)}

# GoDaddy API endpoints
url = "https://api.godaddy.com/v1/domains/available"

# Getting user input for the second level domain to be searched  
domain_tld = input("Insert the domains you'd like to check.\nName format should be just the domain name (SLD)\nseparated by a space:\n")
print (" ")

domain_notld = domain_tld.split()

domain=[]
for i in domain_notld:
    domain.append(i+".com")

# API call (POST)
availability_res = requests.post(url, json=domain, headers=headers)

# Getting back the result to the user 
for domain in json.loads(availability_res.text)['domains']:
    if domain['available']:
        print ("Domain Name:", domain["domain"])
        print ("Domain Stats Availability:", domain["available"])
        print ("USD Price:", int(domain["price"])/10**6, "\n")
    else:
        print ("Domain Name:", domain["domain"])
        print ("Domain Stats Availability:", domain["available"], "\n")
time.sleep(2)
