# NCSweeper
A tool to send Netcat requests to open ports and monitor their responses
  
Requires:
nmap
netcat
colorama
scapy
  
Usage:
python3 NCSweeper.py [Options] [Target]
  
Running the script with no options will run an nmap scan on all ports and attempt to connect to any open ports with Netcat, returning all ports that respond, as well as their response.

To run against a list of ports (one port per line) use:  
python3 NCSweep.py --ports portlist.txt [Target]
  
To send specific request(s) to the open ports such as 'HELP' or 'OPTIONS':  
Single request: python3 NCSweeper.py --request HELP [Target]  
Multiple requests: python3 NCSweeper.py --request HELP,OPTIONS,IPADDUSER [Target]
