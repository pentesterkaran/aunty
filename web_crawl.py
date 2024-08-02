import requests,os
from bs4 import BeautifulSoup
import argparse
import queue
import threading,urllib3
from urllib.parse import urljoin
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
    #parser.add_argument('-w','--wordlists',help='Give wordlists for directories',dest='path_to_wordlists',type=str,required=True)

    return parser.parse_args()

def request(url):
    try:
        html = requests.get(url,verify=False,timeout=2)
        return html.content
    except:
        pass
def crawl(domain_name):
    content_list=[]
    while not q.empty():
        url = f"https://{q.get()}"
        html = request(url)
        soup = BeautifulSoup(html,'html.parser')
        for anchor in soup.find_all('a',href=True):
            link = urljoin(url,anchor['href'])
            
            if "#" in link:
                link = link.split('#')[0]

            if link not in content_list and domain_name in link:
                content_list.append(link)
                with open(f'{domain_name}/crawler_output.txt','a') as f:
                    f.write(f'{link}\n')
                print(f"{color.cyan}[+] Found URL : {link}{color.rst}")
        q.task_done()

def add_subd_q(domain_name):
    file_path = os.path.join(domain_name, "subdomains_find.txt")  # Use os.path.join for safe path construction
    try:
        with open(file_path, 'r') as file:
            subd = file.read().splitlines()
            for subdomain in subd:
                q.put(subdomain)
    except FileNotFoundError:
        print(f"{color.red}Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error occurred while reading '{file_path}': {e}{color.rst}")


def thrd(no_of_threads,domain_name):
    for i in range(no_of_threads):
        t = threading.Thread(target=crawl,args=(domain_name,),daemon=True)
        t.start()
    



if __name__ == '__main__':
    args = take_arguments()
    q=queue.Queue()
    domain = args.domain
    if args.threads:
        threads = args.threads
    else:
        threads = 10
    add_subd_q(domain)
    with open(f"{domain}/crawler_output.txt",'w') as file:
        pass

    print(f'{color.bright}{color.green}\t\t\tCrawling to Find links{color.rst}')
    try:
        thrd(threads,domain)
        q.join()
    except KeyboardInterrupt:
        print("\n[-] Programm Ended")