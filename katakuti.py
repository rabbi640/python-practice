Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #amra kono string ar chracter ar jaiga chaile change korte pari ba pori borton korte pari\
>>> #amra akhane replace () function ar
>>> sen='How can a clam cram in a clean cream can'
>>> sen.replace('c','d')
'How dan a dlam dram in a dlean dream dan'
>>> #akhon amra ? sign k e vanish kore dibo
>>> sen='How can a clam cram in a clean cream can?'
>>> sen.replace('?','')
'How can a clam cram in a clean cream can'
>>> #ata amara alada arekta function diyeo korte pari
>>> #sheta holo strip() function
>>> sentace='How can a clam cram in a clean cream can?'
>>> sentace.sprip('?')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sentace.sprip('?')
AttributeError: 'str' object has no attribute 'sprip'
>>> sentace.strip('?')
'How can a clam cram in a clean cream can'
>>> #amra alhon string ar faka jaiga gulor maddhome string ke alada krre felbo i mean tukra rukta kore felbo tar jonno amrader splite string use korte hobe
>>> #tar jonno amra split () funtion use korbo
>>> sentance.split(' ')
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    sentance.split(' ')
NameError: name 'sentance' is not defined
>>> sentance.split('')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    sentance.split('')
NameError: name 'sentance' is not defined
>>> sentace.split('')
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    sentace.split('')
ValueError: empty separator
>>> sentace.split(' ')
['How', 'can', 'a', 'clam', 'cram', 'in', 'a', 'clean', 'cream', 'can?']
>>> 