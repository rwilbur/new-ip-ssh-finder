import nmap
import sys
print('Starting NMAP scan...\n')
nm=nmap.PortScanner()
nm.scan('192.168.1.1-255','22')
nm.command_line()
nm2=nmap.PortScanner()

if sys.version_info[0] < 3:
    raw_input('Please plug device in to the network and wait until it is connected...\nPress Enter to continue')
else:
    input('Please plug device in to the network and wait until it is connected...\nPress Enter to continue')
nm2.scan('192.168.1.1-255', '22')
nm2.command_line()
for host in nm2.all_hosts():
    if not nm.has_host(host):
        print(host)


