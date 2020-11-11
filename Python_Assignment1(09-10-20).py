# 1. ASSIGNMENT - SOME OF THE IN BUILT FUNCTIONS 

a = "Hello World!"

#1) index() -> will give you the first occurance of the string
print("Position of first occurance of w: {}".format(a.index("W")))
print("Position of first occurance of ld: {}".format(a.index("ld")))
'''
OUTPUT:
Position of first occurance of w: 6
Position of first occurance of ld: 9
'''


#2) rindex() - > will give you the last occurance of the string
print("Position of last occurance of 'l': {}".format(a.rindex("l")))
print("Position of last occurance of 'o': {}".format(a.rindex("o")))
'''
OUTPUT:
Position of last occurance of 'l': 9
Position of last occurance of 'o': 7
'''


#3) replace("oldvalue","newvalue") -> it will replace the old string wiht new string.
print("New string : {}".format(a.replace("World","Krishna")))
'''
OUTPUT:
New string : Hello Krishna!
'''


#4) isspace() -> it will return TRUE if all the characters are whitespaces in the string
a.isspace()
'''
OUTPUT:
False
'''


#5) casefold() -> it will convert the string to lowercase
print(a.casefold())
'''
OUTPUT:
hello world!
'''


#6) count() -> it will return the total count of a value present in the string
print("Total occurances of 'l': {}".format(a.count("l")))
'''
OUTPUT:
Total occurances of 'l': 3
'''


#7) spilt("separator") -> it will return a list of string which is separated by the separator provided in function
x = a.split(" ")
print("List : {}".format(x))
'''
OUTPUT:
List : ['Hello', 'World!']
'''


#8) swapcase() -> it will swap the cases of the string
print("String with swapped case : {}".format(a.swapcase()))
'''
OUTPUT:
String with swapped case : hELLO wORLD!
'''


#9) title() -> it will convert the first character of evry word to upper case
str1 = "hi i am a student of netzwerk academy."
print("Title converted string : {}".format(str1.title()))
'''
OUTPUT:
Title converted string : Hi I Am A Student Of Netzwerk Academy.
'''


#10) zfill() -> it will fill the string with 0 at the begining of the string at specified length
str2 = "12345"
print("String with 0 at the begining : {}".format(str2.zfill(10)))
'''
OUTPUT:
String with 0 at the begining : 0000012345
'''




# 2. ASSIGNMENT - CHECK IF THE "to" IS PRESENT IN "Welcome to Python."

str3 = "Welcome to Python."

#fucntion index()
print("Position of to : {}".format(str3.index("to")))
'''
OUTPUT:
Position of to : 8
'''

#OR


#function find()
print("Position of to : {}".format(str3.find("to")))
'''
OUTPUT:
Position of to : 8
'''
