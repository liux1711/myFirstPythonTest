
print("hello word")
name ='刘星'
stu_id=1
stu_id2=1000
age=31
weight=55.5
print(f"姓名:{name},年龄:{age},体重:{weight}")
print("体重:%.3f" %weight)
print("姓名:%s" %name)
print("学号:%03d" %stu_id)
print("学号:%03d" %stu_id2)
print("姓名:%s,年龄:%d,体重:%.2f" %(name,age+1,weight))

"""
1:input("请输入密码")
2:
"""

password=input("\t请输入密码\n")
print("您输入的密码是%s" %password)

print(type(int(password)))
print(type(float(password)))
print(type(str(password)))
list1=[10,20,30]
print(tuple(list1))
t1=(100,200,300)
print(list(t1))



