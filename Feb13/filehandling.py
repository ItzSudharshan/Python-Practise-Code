file = open('text.txt', 'r')
'''
data = file.read()
print(data)
print(data[0])

OUTPUT

Hello from Test File 
Learing File Handling
H

-------------------------------------------
'''
'''
firstLine = file.readline()
print(firstLine)

file.close()

OUTPUT:

Hello from Test File.

-------------------------------------------------

'''

'''
print(file.readlines()) 

#OUTPUT

#['Hello from Test File.\n', 'Learing File Handling \n']

#It returns the sentence as a List 

-------------------------------------------------
'''
'''
file.close()

file1 = open('test2.txt', 'w')
file1.write('Hello From Python\n')
file1.write('Hello From Java')
'''
'''
OUTPUT 

This output will be written in test2.txt 


Hello From Python
Hello From Java

-------------------------------------------
'''
'''
#When u ask python to write the file then previous content is erased

file1 = open('test2.txt', 'w')
file1.write('Hello')
file1.close()

#So output is Hello

-----------------------------------------
'''
'''

#if u want to keep the previous content and add extra content use append 

#txt2.txt will contain Hello From Python  now after executing the following
file1 = open('test2.txt', 'a')
file1.write('\nHello Java\n')
file1.close()

'''
'''
Output:
Hello From Python 

Hello Java

So Previous Content isnt lost 
---------------------------------------------------------
'''
