str1=input("enter the string:")
char=str1[0]
str1=str1.replace(char,'$')
str1=char+str1[1:]
print("replaced string:",str1)
