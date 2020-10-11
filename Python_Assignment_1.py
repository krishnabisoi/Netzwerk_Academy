# 1. ASSIGNMENT - SOME OF THE IN BUILT FUNCTIONS 

a = "Hello World!"

#1) index() -> will give you the first occurance of the string
print("Position of first occurance of w: {}".format(a.index("W")))
print("Position of first occurance of ld: {}".format(a.index("ld")))


#2) rindex() - > will give you the last occurance of the string
print("Position of last occurance of 'l': {}".format(a.rindex("l")))
print("Position of last occurance of 'o': {}".format(a.rindex("o")))


#3) replace("oldvalue","newvalue") -> it will replace the old string wiht new string.
print("New string : {}".format(a.replace("World","Krishna")))


#4) isspace() -> it will return TRUE if all the characters are whitespaces in the string
a.isspace()


#5) casefold() -> it will convert the string to lowercase
print(a.casefold())


#6) count() -> it will return the total count of a value present in the string
print("Total occurances of 'l': {}".format(a.count("l")))


#7) spilt("separator") -> it will return a list of string which is separated by the separator provided in function
x = a.split(" ")
print("List : {}".format(x))


#8) swapcase() -> it will swap the cases of the string
print("String with swapped case : {}".format(a.swapcase()))


#9) title() -> it will convert the first character of evry word to upper case
str1 = "hi i am a student of netzwerk academy."
print("Title converted string : {}".format(str1.title()))


#10) zfill() -> it will fill the string with 0 at the begining of the string at specified length
str2 = "12345"
print("String with 0 at the begining : {}".format(str2.zfill(10)))




# 2. ASSIGNMENT - CHECK IF THE "to" IS PRESENT IN "Welcome to Python."

str3 = "Welcome to Python."

#fucntion index()
print("Position of to : {}".format(str3.index("to")))

#OR

#function find()
print("Position of to : {}".format(str3.find("to")))
