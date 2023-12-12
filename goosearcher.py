##########################===
#  Author: Pwn3r Security   #
#  Date: 27/May/2023        #
##########################===

# Importing Modules
import socket
import sys

# Host and Port Tuple
host_port = ("www.google.com", 80)

# Taking Some Inputs
query = input("[+] Enter Search Query: ")
level = int(input("[+] Level Of Information To Show: "))
filename = input("[+] Enter Filename to Write HTML: ")

# Filtering Query
query = query.replace(" ", "%20")

# Creating A Request To Send To Server
req = f"GET /search?q={query} HTTP/1.1\r\nHost: {host_port[0]}\r\n\r\n"

# Creating A Client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting To Server
client.connect(host_port)

# Sending The Request
client.send(bytes(req, encoding="utf-8"))

# Opening A File To Write HTML
f = open(filename, "a")

# For Every Level Get HTML Response (The Higher, The More HTML It GETS)
for i in range(1, level):
    f.write(str(client.recv(4096)))

# Closing The File and TCP Client
f.close()
client.close()
