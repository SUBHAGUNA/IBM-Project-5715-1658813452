import random
ip = []
n = int(input("Enter the number of inputs: "))
for i in range(0,n):
    e=int(input())
    ip.append(e)
print(ip)
T=random.choice(ip)
H=random.choice(ip)
print(T,H)
if T>100:
    if H>80:
        print("High temperature and Humidity risk")
    else:
        print("High Temperature!!!")
elif T==100:
    print("Temperature risk!!")
else:
    print("Temperature and humidity are normal..")
