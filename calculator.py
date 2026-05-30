Python 3.13.13 (tags/v3.13.13:01104ce, Apr  7 2026, 19:25:48) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> #simple calculator project
>>> num1=int(input("enter 1st number:"))
enter 1st number:10
>>> num2=int(input("enter 2nd number:"))
enter 2nd number:5
>>> operator=input("enter a opetaror:")
enter a opetaror:*
>>> if operator=="+":
...     print(f"sum of numbers is {num1+num2}")
... elif operator=="-":
...     print(f"subtraction of numbers is {num1-num2}")
... elif operator=="*":
...     print(f"multiplication of numbers is {num1*num2}")
... elif operator=="/":
...     print(f"division of numbers is {num1/num2}")
... else:
...     print("invalid")
... 
...     
multiplication of numbers is 50
