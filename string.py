str1="this is a String.\nWe are creating it in python"
print(str1)
#concretenation
str1="Almas"
len1=len(str1)
print(len1)
str2="Sayem"
str3="AS"
stgg="{} {},{}!".format(str1,str2,str3)
print(stgg)
len2=len(str2)
print(len2)
Final_str=str1+" "+str2
print(Final_str)
print(len(Final_str))
#indexing
str="Almas Sayem"
print(str[0])
print(str[1])
print(str[2])

#slicing
# str[starting_index:ending_index]

str="Almas Sayem"
print(str[1:4])
print(str[0:len(str)])
print(str[:5])
print(str[6:])
print(str[-3:-1]) 


str="I am a coder"
print(str.endswith("oder"))#True
print(str.endswith("Hi"))#False
#Capitalize 1st character
str1="hi Sayem"
str1=str1.capitalize()
print(str1)
#Replace
print(str.replace("coder","Doctor"))
#find
print(str.find("coder"))
#count
print(str.count("a"))
#index
print(str.index('c'))
#splits
print(str.split(" "))
#rpartition
print(str.rpartition(" a "))

stg="Simplilearn"
print(stg.upper())
print(stg.lower())
for i in stg:
    print(i,end="")



