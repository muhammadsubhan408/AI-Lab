my_string=input("enter the string :")
str_length = len(my_string)  # calc the length of the string
# printing the first character  
print(my_string[0])

#printing the last character 
print(my_string[str_length-1])

#printing the length
print(str_length)

#print twice
print(my_string *2)

#printing length excluding space
print(len(my_string.replace( " ","")))