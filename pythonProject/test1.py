if True :
    print("执行！")

if False :
    print("不执行！")
    print("不执行")

print("不执行")
age=30
if age> 28 :
    print("老大不小了")
else:
    print("还小，还能浪")


age= input("请输入年龄\n")


if int(age)<18 :
    print(f"你年龄在{age},属于未成年不能上网")
elif int(age)>30 and int(age)<60:
    print(f"输入年龄{age}")
elif int(age)>60:
      print("可以啊，还有心情上网")


