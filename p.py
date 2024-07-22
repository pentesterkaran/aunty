import socket
import ipaddress
import sys
import os
import time
from colorama import Fore,Back,Style 

# res = sock.connect_ex(("157.240.198.174",80))
# print(res)
# if not res:
#     print(f"80 is open")
class rang:
    red = Fore.RED
    blue = Fore.BLUE
    cyan = Fore.CYAN
    yellow = Fore.YELLOW
    green = Fore.GREEN
    bright = Style.BRIGHT
    reset = Style.RESET_ALL


def get_ip(target):
    try:
        target = ipaddress.ip_address(target)
        return str(target)
    except ValueError:
        try:
            target = socket.gethostbyname(target)
            return target
        except socket.gaierror:
            print("You have to provide valid ip or hostname")


def port_scan(ip,start,end):
    print(f"{rang.bright}{rang.blue}\nPORT\t\t STATE{rang.reset}")
    for port in range(start,end+1):

        try:
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip,port))
            
            if result == 0:
                print(f"{port}\t\t {rang.yellow}OPEN {rang.reset}")
            else:
                print(f"{port}\t\t {rang.cyan}CLOSE{rang.reset}")
        except socket.error as e:
            print(f"{rang.red}SomeThing Bad Happen with socket{rang.reset}")
            sys.exit(-1)
        except OverflowError:
            print(f"{rang.red}I think By Mistake you provide port number more than 65535{rang.reset}")
            sys.exit(-1)
        # except TypeError:
        #     print("String Datatype is Expected")
        finally :
            sock.close()


def clear_term():
    os.system('cls' if os.system=='nt' else 'clear')

if __name__ == "__main__":
    ip_addr = get_ip(sys.argv[1])
    start= int(sys.argv[2])
    end = int(sys.argv[3])
    clear_term()
    print(f"{rang.green}{rang.bright}\t\t\tStarted Scanning Ports at {ip_addr}{rang.reset}")
    start_time = time.time()
    try:
        port_scan(ip_addr,start,end)
    except KeyboardInterrupt:
        print(f"{rang.red}\n\tKeyboard Interrupt Successfully Received{rang.reset}")
    print(f"{rang.bright}{rang.yellow}Time-Taken:{time.time()-start_time}")