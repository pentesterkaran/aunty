import requests
import argparse
import os
import queue
import threading
import urllib3
from colorama import Fore,Back,Style

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class color:
    red = Fore.RED
    blue = Fore.BLUE
    cyan = Fore.CYAN
    green = Fore.GREEN
    yellow = Fore.YELLOW
    rst = Style.RESET_ALL
    bright = Style.BRIGHT

def take_arguments():
    parser = argparse.ArgumentParser(description="Level 1 Subdomain Finder")
    parser.add_argument('-d','--domain',help='Provide target domain',dest='domain',type=str,required=True)
    parser.add_argument('-t','--threads',help='Provide Threads(Default = 10)',dest='threads',type=int)
    parser.add_argument('-w','--wordlists',help='Give wordlists for directories',dest='path_to_wordlists',type=str,required=True)

    return parser.parse_args()

def make_file(domain_name):
    if not os.path.exists(f"{domain_name}"):
        os.mkdir(domain_name)
        with open(f'{domain_name}/subdomains_find.txt','w') as f:
            f.write(f"{domain_name}\n")
    else:
        with open(f'{domain_name}/subdomains_find.txt','a') as f:
            f.write(f"{domain_name}\n")
            


def add_subd_in_q(path,domain_name):
    with open(path,'r',encoding='utf-8',errors='ignore') as subd_list:
        for subd in subd_list.read().splitlines():
            url = f"https://{subd}.{domain_name}"
            q.put(url)

def brute_subd(domain_name):
   
        # proxy = {'http':'http://127.0.0.1:8080',
        #         'https':'http://127.0.0.1:8080'}
        while not q.empty():
            l1subd = q.get()
            
            try:
                res = requests.get(url=l1subd,verify=False,timeout=2)
                if res.status_code == 200:
                    subd = res.url.split('/')[2]
                    print(f"{color.cyan}[+] Subdomain Find : {subd}{color.rst}")
                    with open(f"{domain_name}/subdomains_find.txt",'a') as file:

                        file.write(subd+'\n')
                
            except:
                pass
            q.task_done()
        


def thrd(no_of_threads,domain_name):
    for i in range(no_of_threads):
        t = threading.Thread(target=brute_subd,args=(domain_name,),daemon=True)
        t.start()

def clear_term():
    os.system('cls' if os.system == 'nt' else 'clear')



if __name__=='__main__':
    args = take_arguments()
    domain = args.domain
    wpath = args.path_to_wordlists
    if args.threads:
        threads = args.threads
    else:
        threads = 10

    clear_term()
    q=queue.Queue()
    add_subd_in_q(wpath,domain)
    make_file(domain)
    print(f"{color.bright}{color.green}\t\tFinding Subdomains{color.rst}")
    try:
        thrd(threads,domain)
        q.join()
    except KeyboardInterrupt:
        print(f'{color.red}\n[-] Program Ended{color.rst}')
    
   
    
    
