Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a='bangla'
>>> print (a)
bangla
>>> print('My favorit language is :',a);
My favorit language is : bangla
>>> 
>>> 
>>> #amr chaile akhane string ar jonno alada sign use korte pari
>>> print('what is our Mother Language:%s' %a);
what is our Mother Language:bangla
>>> #%d use hoi --intger type ar jonno
>>> #%f use hoi -- float type number ar jonmn
>>> #%s use hoi -- string type ar jonno
>>> print('what is our Mother Language:%s' a);
SyntaxError: invalid syntax
>>> #number string
>>> number =4563296.3655421
>>> print('number')
number
>>> print(number)
4563296.3655421
>>> print('%.2f'%number)#% ar por . diye joto number dibo doshomic ar por toto ghor nibe.
4563296.37
>>> 
>>> 
>>> 
>>> a=input()
bangla
>>> b=input()
English
>>> print('My favorit language are',a,'and',b)
My favorit language are bangla and English
>>> #uporer program ar a ar b te duti language ar nam  hisheb input nise tarpor akta shundor line print diyese
>>> 
>>> 
>>> 
>>> #same kazta amra string diye o use korte pari
>>> a='Bangla'
>>> a=input()
Python
>>> b=input()
Javascript
>>> print('My favorit language is :%s and %s'(a,b))
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    print('My favorit language is :%s and %s'(a,b))
TypeError: 'str' object is not callable
>>> print('My favorit language is :%s and %s'%(a,b))
My favorit language is :Python and Javascript
>>> 