## [WEB-04] String data in Python ##

# Strings as sequences #
iese = 'IESE Business School'
len(iese)
iese[5:]
iese[:4] + ', A way to learn'
'IE' in iese

# Python string functions #
iese.lower()
iese.replace('IESE', 'Iese')
iese.split(' ')
iese.split('i')
iese.split()
iese.find('Business') 
iese.find('Negocios')
iese.count('s')

# Regular expressions #
import re
re.sub('[a-z]', 'x', iese)
re.sub('[a-z]+', 'x', iese)
re.split('\W+', 'IESE: A way to learn, a mark to make')
re.findall('\w+', iese)
re.sub(',.+', '', 'IESE: A way to learn, a mark to make')
re.sub('$20', '$30', 'The price is $20')
re.sub('\$20', '$30', 'The price is $20')
