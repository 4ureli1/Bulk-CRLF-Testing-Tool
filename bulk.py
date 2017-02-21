import httplib
import os 

print """
+===================================================================+
||  Test Carriage Return Line Feed Vulnerable Website with Ease !  ||
||		     (HTTP Response Splitting)			   ||	
||    +======================================================+     ||
||	 ___   _   _   _      _  __     ___   ___   _      ___     ||
||	| _ ) | | | | | |    | |/ /    / __| | _ \ | |    | __|    ||
|| 	| _ \ | |_| | | |__  | ' <    | (__  |   / | |__  | _|     ||
||	|___/  \___/  |____| |_|\_\    \___| |_|_\ |____| |_|      ||
||								   ||
||    +======================================================+     ||
||      ~ by Yadnyawalkya Tale (yadnyawalkyatale@gmail.com) ~  	   ||
+===================================================================+
"""

payload = "//www.google.com/%2e%2e"

with open("weblist.txt", "r") as f:
    for domain in f:
        domain = "www." + domain.strip()
	conn = httplib.HTTPConnection(domain)
	conn.request("HEAD","//www.google.com/%2e%2e")
	res = conn.getresponse()
	#print res.status, res.reason
	com = "curl -I --silent {0}{1} | grep -i location".format(domain,payload)
	if res.status == 301:
		print "\x1b[6;30;41m", res.status, res.reason, "** at {0} \x1b[0m".format(domain)
		os.system(com)
	elif res.status > 300 and res.status < 400:
		if res.status != 301 :
	                print "\x1b[6;30;42m", res.status, res.reason , "\x1b[0m", "** at {0}".format(domain)
			os.system(com)
	elif res.status != 301:
                print "\x1b[6;30;44m", res.status, res.reason, "\x1b[0m" "** at {0} ".format(domain)
		os.system(com)

