#Difference ways of Declaring the String 

#s1 = 'My Name is Sudharshan Nayak'
#s2 = "My Age is 25"
#s3 =  """We are Learning Strings"""
#s4 = '''Python is Dynamically Typed Programming Language'''
#s5 = "I'm Priya"
#s6 = 'My  "age" is 25'

#print(s1)
#print(s2)
#print(s3)
#print(s4)
#print(s5)
#print(s6)

#Multiline comment 
''' ''' #Used for Multiline Comments

print('--------------------------------------------')
print("STRING METHODS IN PYTHON")
print('1.UPPER')
message = 'Python Programming is Intresting'
message_result = message.upper()
print(message_result)
print('--------------------------------------------')
print('2.LOWER')
message1 = 'Python Programming is Intresting'
message_result1 = message1.lower()
print(message_result1)
print('--------------------------------------------')
print('3.STRIP')
message3 = '***Python is a Good Programming language***'
stripped_message = message3.strip("*")
print(stripped_message)
print('--------------------------------------------')
print("4.FIND")
message4 = "Python is an Amazing Programming Langauage"
position = message4.find('Amazing')
print(position)
print('--------------------------------------------')
print("5.CONCAT")
str1 = "Hello"
str2 = "World!"
print(str1 + ' ' + str2)
print('--------------------------------------------')
print('6.LENGTH OF THE STRING')
message5 = 'Sudharshan Nayak'
length = len(message5)
print("The length of the String is", length)
print('--------------------------------------------')
print('7.REPLACE')
message6 = 'I love Programming in java'
updated_message = message6.replace('Java', 'Python')
print(updated_message)
print('--------------------------------------------')
print('8.SPLIT & JOIN')
sentence = 'Python is a Versatile Programming Language'
words_list = sentence.split()
hyphenated_sentence = '-'.join(words_list)
print(words_list)
print(hyphenated_sentence)
print('--------------------------------------------')
