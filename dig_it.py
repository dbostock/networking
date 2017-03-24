import socket
import dns.resolver

path=r"C:\python\list2.txt"
with open(path, 'r') as f:
    for host in f:
        HOSTN = host.rstrip()
	print HOSTN
#resolver.nameservers=[socket.gethostbyname('ns1...')]
	myResolver = dns.resolver.Resolver()
	myResolver.nameservers = ['10.7.40.13', '10.6.1.134'] 
	try:
		myAnswers = myResolver.query(HOSTN, "A")
		for rdata in myAnswers:
			print rdata
	except:
		print "Query failed"
		pass

