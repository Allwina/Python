s=0
n=input("enter the number")
l=len(n)
for num in (n):
    s=s+(int(num)**l)
print(s)
if(s == int(n)):
    print("Armstrong")
else:
    print("Not")