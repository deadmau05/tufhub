import sys
import os

def install():
	os.system("apt update")
	os.system("pip install mechanize json whois python-whois requests bs4 requests[socks] urlparse cookielib") 
	os.system("pip install scapy datetime argparse re threading urllib2 modules builtwith smtplib")
	os.system("apt install python-socks")
	os.system("apt install metasploit-framework")
	os.system("apt install setoolkit")
	os.system("apt install wifite")
	os.system("apt install reaver")
	os.system("apt install aircrack-ng")
	os.system("apt install nmap")
	os.system("apt install php")
	os.system("apt install perl")

print "\033[0madding script to path so you can use it anywhere by typing \033[92mtufhub.sh\033[0m"
os.system("sleep 2")
os.system('''
chmod +x /root/tufhub *
mkdir /bin/tufhub
cd /root/tufhub
cp -r /root/tufhub * /bin/tufhub
rm -fr tufhub
echo "python /bin/tufhub/tufhub.py" >> /bin/tufhub/tufhub.sh
chmod +x /bin/tufhub/tufhub.sh
echo "export PATH=/bin/tufhub:$PATH" >> /root/.bashrc
''')


print "are you running on the real kali linux os   [y/n]"
check = raw_input("[y/n]> ")
if check == "y" :
	print "good"
	os.system("sleep 2")
	install()
if check == "n" :
	print "then a decent amount of tools in this script might not work"
	print "do you want to continue installation  [y/n]"
	install = raw_input("[y/n]> ")
	if install == "y" :
		install()
	if install == "n" :
		print "thanks for checking out my script"
		sys.exit
