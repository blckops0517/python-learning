#Call index position to get string

string="access a string using index value "
print(string[2])
print(string[2:])
print(string[2:5])
print(string[:5])
print(string[-4:]) 

#Modify the string

string1 = " this modify string  "
print(string1.upper())
print(string1.lower())
print(string1.strip())                   # Remove white space front and back     
print(string1.lstrip())  
print(string1.rstrip())                     
print(string1.replace("this","that"))
print(string1.split(","))

#Concatenation a string use + operator

str_1 = "hello"
str_2 = "guys"
str_3 = 78
str_4 = 5
total = str_1+" "+str_2
print(total)

#To add string + variable use f-string method .format is old method
#use f-string do operations, fuction, variables,modify
print(f"hi {str_1} {str_2} ")
print(f"hi {str_1} {str_3}")            #Concatenate str + int
print(f"to add this {str_3+2} value\nto minus {str_4-2} value")

#Escape characters
str_escape1="hello makkale'escape'vanakam"      #\n \t \b \r \f \\
str_escape="hello makkale\"escape\"vanakam"

print(str_escape)
print(str_escape1)

