'''s1 = 'Kodnest'
s1.upper()
print(s1)
'''
#String are Immutable(Once Declare the String we cant modify it)
#If we try to modify it , it will create a new String 
#If new String does not have any reference variable then it will be removed 


#id will help us to get the actual adress of object 

#Python Internally uses String Interning 

#String Interning is the Process Of Checking String Intern Pool Before Creating Any new object

#Whenver we want to create a New Object . Python First Will Check Check String Intern Poll Whether the Object already exist or not 

#When the object already exist in the String Intern record then the address of existing object will be reused  
'''
s1 = 'K'
print(s1,id(s1))
'''



s1 = 'Hello'
s2 = 'World'
print(s1, id(s1))
print(s2, id(s2))

print(s1[0])
print(s1[-1])

print('S1 ID of H:',id(s1[0]))
print('S1 ID of O:',id(s1[-1]))


print('S2 ID of W:',id(s2[0]))
print('S2 ID of O:',id(s2[1]))




