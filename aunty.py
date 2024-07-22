import socket
import argparse
from colorama import Fore,Back,Style
import sys 
from scapy.all import srp
from scapy.layers.l2 import ARP,Ether

# Color definations

red = Fore.RED
blue = Fore.BLUE
green = Fore.GREEN
cyan = Fore.CYAN
yellow = Fore.YELLOW
bright = Style.BRIGHT
reset = Style.RESET_ALL


# Defining arguments of aunty

desc = 'Information Gathering ToolKit'
use = 'Collect Information Regarding Your Target'
parser = argparse.ArgumentParser(description = desc)
parser.add_argument('-n', help= 'Provide targeted network', type= str, dest= 'network')
parser.add_argument('-d', help= 'Provide Domain name for whois info', dest= 'domain')

#Getting Arguments from parser
arguments = parser.parse_args()
provided_network = arguments.network
domain_name = arguments.domain

print(provided_network)

#Checking that Program contain arguments or not 

if len(sys.argv) < 2:
    print(f"{bright} {red}      No Arguments Given \n{reset}{green}  Use -h flag for Helping Menu{reset}")
    sys.exit(-1)

#Creating empty list to store dictionary of ip and mac
online_hosts = []

# Creating layers for broadcast
ether = Ether(dst = "ff:ff:ff:ff:ff:ff")
arp = ARP(pdst = provided_network)

#Condition to check user want to scan network or not

if provided_network:
    try:

        #stacking layer 1 and 2
        packet = ether/arp

        print(blue)
        response = srp(packet, timeout = 3)
        answered_packet = response[0]

        #Adding ip and mac of recv packets into online hosts list as a dictionary
        for sent,recv in answered_packet:
            online_hosts.append({'ip':recv.psrc,'mac':recv.hwsrc})

        # Styling Presentation of ip and mac
        print(f"{bright}{green}  \nIP Address's \t\t             MAC Address's{reset}")

        #Printing IP and MAC of online clients

        for host in online_hosts:
            print(f'{cyan}{host["ip"]}\t\t \t  {host["mac"]}{reset}')

    except KeyboardInterrupt:
        print('Program Succesfully Ended')



    