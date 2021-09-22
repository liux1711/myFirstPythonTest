
import random
i=random.randint(0,4)
num=0
while num<5:
    i = random.randint(0, 4)
    if i==2:
        print(f"输出次数i={i }")
        break
    num=num+1
    print(f"输出次数{num}")

