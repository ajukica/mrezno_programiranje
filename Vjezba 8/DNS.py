import dns.resolver
import dnspython

domena = input('Unesite DNS ime ili IP adresu..')
tip = input ("Unesite tip zapisa")


for qtype in 'A', 'MX', 'PTR':
    result = dns.resolver.resolve(domena,qtype, raise_on_no_answer=False)
    if result.rrset is not None:
        print(result.rrset)
        print('Record checked successfully\n')
