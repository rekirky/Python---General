'''
a1=int(input("Input a1 : "))

b1=int(input("Input b1 : "))

a2=int(input("Input a2 : "))

b2=int(input("Input b2 : "))

a3=int(input("Input a3 : "))

b3=int(input("Input b3 : "))
'''
a1=10
b1=-1
a2=-2
b2=11
a3=0
b3=1

result1= ((((a2 - a1)**2) + ((b2-b1)**2) )**0.5)
result1= round(result1)
result2= ((((a2 - a3)**2) + ((b2-b3)**2) )**0.5)
result2= round(result2)
result3= ((((a1 - a3)**2) + ((b1-b3)**2) )**0.5)
result3= round(result3)

print("distance between",(a1,b1),"and",(a2,b2),"is : ",result1)
print("distance between",(a2,b2),"and",(a3,b3),"is : ",result2)
print("distance between",(a3,b3),"and",(b1,b2),"is : ",result3)

semiperimeter= (((result1)+(result2)+(result3))/2)
print(semiperimeter)

A = round(((semiperimeter*(semiperimeter-result1)*(semiperimeter-result2)*(semiperimeter-result3)) ** 0.5),3)
print(A)