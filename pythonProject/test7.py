

#切片

#str="abcde";
#print(str[2:5:2])
#print(str[:5])
#print(str[-3:-1])


str1="my name is liuxing , i am a man ,is a loney man"

#print(str1.find("is",11,50))
#print(str1.count("is",11,50))
#print(str1.index("is",11,50))


#print(str1.replace('is', 'im',10))

print(str1.split('is'))


list1=['aa','bb','cc']
str4=('aa','bb','cc')
str2=''
# for i in list1:
#     str2=i.join()
#     print(str2)
print('......'.join(list1))
print('......'.join(str4))