import requests
import threading
import sys
import queue
import ipaddress
import socket
from colorama import Fore,Back,Style
import os
import argparse
import urllib3
import time

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class color:
    red = Fore.RED
    blue = Fore.BLUE
    yellow = Fore.YELLOW
    cyan = Fore.CYAN
    black = Fore.BLACK
    green = Fore.GREEN
    rst = Style.RESET_ALL
    bright = Style.BRIGHT

def take_arguments():
    parser = argparse.ArgumentParser(description="Script for directory bruteforce")
    parser.add_argument('-u','--url',help='Provide target url for directory bruteforce',dest='url',type=str,required=True)
    parser.add_argument('-t','--threads',help='Give number of threads',dest='threads',type=int)
    parser.add_argument('-w','--wordlists',help='Give wordlists for directories',dest='path_to_wordlists',type=str,required=True)

    return parser.parse_args()


# def get_ip(target):
#     try:
#         ip = ipaddress.ip_address(target)
#         return str(ip)
#     except:
#         try:
#             ip = socket.gethostname(target)
#             return str(ip)
#         except socket.error as e:
#             print(e)


def clear_term():
    os.system('cls' if os.system == 'nt' else 'clear')

def add_dir_in_queue(path,url):
    with open(path,'r',encoding='utf-8',errors='ignore') as directory_list:
        for dir in directory_list.read().splitlines():
            url_element = f"{url}/{dir}"
            q.put(url_element)

def bruto():
    
    # proxy = {'http':'http://127.0.0.1:8080',
    #          'https':'http://127.0.0.1:8080'}

    while not q.empty():
        url = q.get()
        try:
            res = requests.get(url,allow_redirects=True,verify=False)
            if res.status_code == 200:
                print(f"{color.cyan}[+] Directory Found : {res.url}{color.rst}")
        except :
            print(f"{color.red}[-] Error While requesting page{color.rst}")
        
        q.task_done()

def thrd(no_of_threads):
    for i in range(no_of_threads):
        t = threading.Thread(target=bruto,daemon=True)
        try:
            t.start()
        except KeyboardInterrupt:
            print(f"{color.red}Ended{color.rst}")

if __name__ == "__main__":
    args = take_arguments()
    # print(f"{args.url},{args.threads},{args.wordlists}")
    url = args.url
    wordlist_path = args.path_to_wordlists
    
    if args.threads:
        threads = args.threads
    else:
        threads = 10

    q = queue.Queue()
    add_dir_in_queue(wordlist_path,url)
    clear_term()
    start_time = time.time()
    print(f"{color.bright}{color.green}\t\t\tFinding Directories{color.rst}")
    try:
        thrd(threads)
        q.join()
        
    except KeyboardInterrupt:
        print(f"{color.red}\nProgram Ended Successfully{color.rst}")
    
    print(f"{color.bright}{color.yellow}Time Taken : {time.time()-start_time}{color.rst}")