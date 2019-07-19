import socket

Host_name = str(input("Enter Host Name : ")) #Enter Host Address i.e www.facebook.com
Host_ipv4 = socket.gethostbyname(Host_name) 
print("Host IPV4 {0}".format(Host_ipv4))

option = True
while option:
    port = int(input("port : ")) #Port To Scan 
    try:
        soc_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        soc_object.connect((Host_name, port))
        print("Port {}: Open".format(port))
        soc_object.close()
    except:
        print("Port {}: Closed".format(port))

print("Port Scanning complete")
