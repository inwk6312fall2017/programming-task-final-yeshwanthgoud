# Programming Task 

Welcome to your final programming task 
  - You have to clone this repo to your account, you should be seeing this on your account, if someone elses name is listed call an instructor for help.
  - Use the Ubuntu VM / Your PC / Or Python anywhere to write the progrm.
  - Use git add, commit and push to send the code back. 
  - Don't forget to add user name and email on git. 
  - You are allowed to use any form of searching and documentation reading and book reading is promoted
  - Each task is to be saved as a individual python file with the name task0A.py, where A is the tasknumber and 0 is the number 0.
  - You cannot talk to your other people or ask for help!


# Task 1 - Biggest word in the books

### Objectives
Given three books find the biggest word in all of the three books. 
The books are Book1.txt, Book2.txt, Book3.txt

# Task 2 - Python Weather API 

Look at the weathe API from https://github.com/stevob21/weather-api and read the documentation there. You will be asked to get the weather for the next 5 days for halifax

### Installing 

Use PIP3 and install the python3-weather-api
```
pip install python3-weather-api
```

### Objectives
Based on the next 5 days of forecast of halifax find the following: 
1. The day that has the highest temperature in the next 5 days of forecast
2. The day that has the lowest temperature in the next 5 days of forecast
3. If it will rain the next 5 days inform the user and tell him which day it will rain

You should only output a formatted text that displays the information.

### Development Hints

Don't forget to create a weather object by properly calling the weather class (sometimes even the document writes forget using ())
```py
# Lookup via location name.
location = weather.lookup_by_location('halifax')
condition = location.condition()

# Get weather forecasts for the upcoming days.
for forecasts in location.forecast():
    print (forecasts['text'])
    print (forecasts['date'])
    print (forecasts['high'])
    print (forecasts['low'])
```

# Task 3 - Changing a Cisco Config file
You are given a cisco config file ("running-config.cfg") and are asked to modify it. 

### Objectives
Use the config file for the following exercises.
1 - Create a new configuration file that replaces all (sub-)interface IP addresses that start with '172.' with IP addresses that start with '192.'. Leave the remaining octets unchanged. 
2 - Create a Python dictionary of all access lists configured. The dictionary should be referenced by the access lists name and include all the lines in the access list intact.

### Hints
Acl's are just like normal files. You can read and write to them as such.
If you cannot decide what to use as keys just use the part after object
Example: 

In the ACL:
```sh
access-list transit_access_in extended permit object-group SERVICES-INSIDE-XCOMP-RADIUS object MGMT-TRANSIT object SERVER-INSIDE-XCOMP-RADIUS 
```
This part can be used as the key
```sh
object MGMT-TRANSIT object SERVER-INSIDE-XCOMP-RADIUS
```
# Task 4 - RESTCONF 
You are given a code to talk to the APIC-EM sandbox controller in the files, create-ticket.py and get-network-hosts.py through RESI. 
The API-DOCS can be found at https://developer.cisco.com/site/apic-em/docs/api.gsp

### Objectives
Modify get-network-hosts.py to display all the hosts with their names IP Addresses  and MAC Addresses. [This should be done on the same file]
Write a new function called getnetworkdevicecount that gets the count of network devices. (The API can be found under Inventory -> network-device -> count)
[Create a newfile called task04.py and import create-ticket.py to achive this]
Use the controller at: https://sandboxapic.cisco.com/

### Max time: 3 hours!

