'''
NMAP and NETCAT Analysis Tool

---DEPENDENCIES---
Install Colorama using pip:
pip install colorama
------------------


-----USAGE-----:
python net_analyse.py --ip 0.0.0.0 -> IP Address to scan NMAP
python net_analyse.py --ip 0.0.0.0 --request HELP -> with single Request
python net_analyse.py --ip 0.0.0.0 --request HELP,OPTIONS -> with multiple Requests
python net_analyse.py --ip 0.0.0.0 --ports ports.txt-> scan ports from ports.txt file seperated by new line

'''

import subprocess, argparse, colorama
from colorama import Fore,init


parser = argparse.ArgumentParser()
parser.add_argument('--ip', type=str, required=True)
parser.add_argument('--ports', type=str)
parser.add_argument('--requests', type=str)
args = parser.parse_args()


addr=args.ip
requests_list=[]
if args.requests:
    try:
        if "," in args.requests:
            requests_list=(args.requests).split(",")
        else:
            requests_list.append(args.requests)
    except:
        print(Fore.RED,"Invalid Character in Requests")


if args.ports:
    try:
        ports_file=args.ports
        with open(ports_file,"r") as rr:
            ports=rr.read().splitlines()
            #print(ports)
    except:
        print(Fore.RED,"Error with Ports file")
else:
    ports=[]

def run_nmap_with_ports(addr,s):
    global ports
    for port in ports:
        result = subprocess.run(['nmap', "-p"+str(port) ,addr], stdout=subprocess.PIPE)
        x=(result.stdout.decode('utf-8'))
        if s!="n":
            print(x)

def run_nmap(addr):
    try:
        global ports
        result = subprocess.run(['nmap',"-p-", addr], stdout=subprocess.PIPE)
        x=(result.stdout.decode('utf-8')).split("\n")
        print(x)
        for i in x:
            if "SERVICE" in i:
                s_i=x.index(i)
                s_i+=1
                s=x[s_i:-3]
                break
        if s:
            print(Fore.GREEN,"Open Port(s) Status:")
        for t in s:
            if "open" in t:
                print(t)
                port = t.split("/")[0]
                ports.append(port)
    except:
        print(Fore.RED,"Error connecting to Host, please try again.")
        exit()
#print(ports)
#ports=['21', '22', '80', '110', '143', '443', '465', '587', '993', '995', '2000']
def check_ports_with_command(addr,ports,command):
    for comm in command:
        print(Fore.BLUE,"___________________________________________")
        print(Fore.BLUE,"Executing for command: %s"%comm)
        print(Fore.BLUE, "___________________________________________")
        for port in ports:
            print(Fore.GREEN,"..........................................")
            print(Fore.GREEN,"Executing netcat: %s %s %s" % ('netcat ',addr,port))
            print(Fore.GREEN, "..........................................")
            print(comm)
            proc = subprocess.Popen(["netcat",addr,port], stdin=subprocess.PIPE)
            comm=comm+"\n"
            proc.stdin.write(comm.encode())
            try:
                output, error = proc.communicate(timeout=3)
            except subprocess.TimeoutExpired:
                proc.kill()
                output, error = proc.communicate()
                try:
                    print(Fore.LIGHTBLUE_EX,output.decode('utf-8'))
                except:
                    continue

def check_ports_without_command(addr,ports):
    for port in ports:
        print(Fore.BLUE, "___________________________________________")
        print(Fore.BLUE,"Executing command: %s %s %s" % ('netcat ',addr,port))
        print(Fore.BLUE, "___________________________________________")
        proc = subprocess.Popen(["netcat",addr,port])
        try:
            output, error = proc.communicate(timeout=3)
        except subprocess.TimeoutExpired:
            proc.kill()
            output, error = proc.communicate()
            try:
                print(Fore.LIGHTBLUE_EX,output.decode('utf-8'))
            except:
                continue



if addr and not requests_list and not ports:
    run_nmap(addr)
    check_ports_without_command(addr,ports)
elif addr and requests_list and not ports:
    run_nmap(addr)
    check_ports_with_command(addr,ports,requests_list)
elif addr and requests_list and ports:
    run_nmap_with_ports(addr,"n")
    check_ports_with_command(addr,ports,requests_list)
elif addr and not requests_list and ports:
    run_nmap_with_ports(addr,"n")
    check_ports_without_command(addr, ports)

