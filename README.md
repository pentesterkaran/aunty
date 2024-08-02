
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

### Output
```sh
[INFO] Network Scanning in Progress...
[INFO] Scanning network: 192.168.1.0/24

IP Address's                  MAC Address's
192.168.1.1                   00:1A:2B:3C:4D:5E
192.168.1.105                 01:2B:3C:4D:5E:6F
192.168.1.110                 02:3C:4D:5E:6F:70
```


