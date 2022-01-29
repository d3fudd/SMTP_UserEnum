#!/usr/bin/python

import socket,sys,time,re

if len(sys.argv) !=4:
	print " "
	print " :':':':':':':':':':':':':':':':':':':':':':':':':':':':':':':':':':':' "
	print "                S M T P  -  U S E R   E N U M E R A T O R"
	print " .:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.: "
	print " "
	print " [!] Necessary to inform: Target IP, port SMTP and wordlist "
	print "     Example: python smtp_user_enum.py 192.168.15.9 25 users.txt "
	print " "
	sys.exit(0)

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((sys.argv[1],int(sys.argv[2])))

banner = tcp.recv(1024)
print " "
print " :':':':':':':':':':':':':':':':':':':':':':':':':':':':':':':':':':':' "
print "                S M T P  -  U S E R   E N U M E R A T O R"
print " .:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.: "
print " "
print " [*] Searching for existing users, please wait..."
print " "
print " [+] Banner: "+banner.strip("220 ")
print " :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::: "
print " "

usuarios_file = open(sys.argv[3]).read().split("\n")

for usuario in usuarios_file:
	tcp.send("VRFY "+str(usuario)+"\r\n")
	user = tcp.recv(1024)

	if re.search("252",user):
		print " [+] User found: "+user.strip("252 2.0.0 ")
	time.sleep(2)
