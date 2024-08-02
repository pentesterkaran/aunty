
   ![aunty_logo](https://github.com/pentesterkaran/aunty/blob/main/asset/aunty.png)

## Host Discovery

### Features

- **Network Scanning**: Discover devices on your local network by using Address Resolution Protocol.

### Requirements

Before you run the script, Install Required Python packages :

```sh 
pip3 install -r requirements.txt
```
### Usage

```sh 
python3 host_discovery.py -n 192.168.1.0/24
```

### Sample Output
```sh
[INFO] Network Scanning in Progress...
[INFO] Scanning network: 192.168.1.0/24

IP Address's                  MAC Address's
192.168.1.1                   00:1A:2B:3C:4D:5E
192.168.1.105                 01:2B:3C:4D:5E:6F
192.168.1.110                 02:3C:4D:5E:6F:70
```

## Port Scan

### Features

- **Multi-Threaded Port Scanning**: Scan multiple ports simultaneously to speed up the process.
- **Port Status**: Identifies whether ports are open or closed.
- **Dynamic IP Resolution**: Resolves domain names to IP addresses.
- **Customizable Scanning Range**: Specify the range of ports to scan.
- **Color-Coded Output**: Easily distinguish open and closed ports with color-coded console output.

### Usage

```sh
python fast_port.py <IP_ADDRESS_OR_DOMAIN> <START_PORT> <END_PORT> <NUMBER_OF_THREADS>
```

```sh
python fast_port.py example.com 20 80 10
```
### Sample Output
```sh
PORT        STATE
20          OPEN
21          CLOSED
22          OPEN
...
```

## Directory Brute Force 


### Features

- **Multi-Threaded Scanning**: Efficiently brute-force directories using multiple threads.
- **Configurable Threads**: Control the number of threads used for scanning.
- **Color-Coded Output**: View results in a clear and visually distinct format.
- **Custom Wordlists**: Use your own wordlists for directory names.

### Usage

```sh 
python directory_bruteforcer.py -u <TARGET_URL> -w <WORDLIST_PATH> [-t <NUMBER_OF_THREADS>]
```

```sh
python directory_bruteforcer.py -u <TARGET_URL> -w <WORDLIST_PATH> [-t <NUMBER_OF_THREADS>]
```

```sh
python directory_bruteforcer.py -u http://example.com -w wordlists/common.txt -t 20
```

### Sample output
```sh
[+] Directory Found : http://example.com/admin
[+] Directory Found : http://example.com/login
[-] Error While requesting page
```
