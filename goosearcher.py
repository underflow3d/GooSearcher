import socket
import sys

host_port = ("www.google.com", 80)

query = input("[+] Enter Search Query: ")
level = int(input("[+] Level Of Information To Show: "))
filename = input("[+] Enter Filename to Write HTML: ")

query = query.replace(" ", "%20")

req = f"GET /search?q={query} HTTP/1.1\r\nHost: {host_port[0]}\r\n\r\n"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(host_port)

client.send(bytes(req, encoding="utf-8"))

f = open(filename, "a")

for i in range(1, level):
    f.write(str(client.recv(4096)))

f.close()
client.close()
