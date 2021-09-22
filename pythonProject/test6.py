num=1
num1=int(input("请输入密码\n"))
if num == num1 :
    print("准入")
else:
    print("不准入")
i=0
while i<num1 :
    print(f'{i}')
    i+=1
    if i==3 :
        print(f'打印{i}跳出循环')
        break

str="liuxing"
for i in str :
    print(f'{i}')


list1=[10,20,30]
for i in list1:
    print(f'{i}')