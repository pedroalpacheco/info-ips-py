from ipwhois import IPWhois
from pprint import pprint

def verip(ip):
    obj = IPWhois(ip)
    '''Pegando pais'''
    result4 = obj.lookup_whois()
    pprint(result4["nets"][0]['country'])

arquivo = open('arq-limpo3.txt', 'r')

le_arquivo = arquivo.read()

result = le_arquivo.split("\n")

for i in result:
    verip(i)