from ipwhois import IPWhois
from pprint import pprint

obj = IPWhois('221.2.44.75')

#Pega completo
#results = obj.lookup_rdap(depth=1)

#Pega ip
#results2 = obj.address

#Whois completo
#result3 = obj.lookup_whois()

result4 = obj.lookup_whois()

#Pega pais
pprint(result4["nets"][0]['country'])





