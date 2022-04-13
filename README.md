# NCSweeper
A tool to send Netcat requests to open ports and monitor their responses
  
Requires:  
nmap  
netcat  
colorama  

  
Usage:  
python3 NCSweeper.py [Options] --ip [Target]
  
Running the script with no options will run an nmap scan on all ports and attempt to connect to any open ports with Netcat, returning all ports that respond, as well as their response.

To run against a list of ports (one port per line) use:  
python3 NCSweep.py --ports portlist.txt --ip [Target]
  
To send specific request(s) to the open ports such as 'HELP' or 'OPTIONS':  
Single request: python3 NCSweeper.py --request HELP --ip [Target]  
Multiple requests: python3 NCSweeper.py --request HELP,OPTIONS,IPADDUSER --ip [Target]
