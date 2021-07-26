# Check if all values equal something

a = 1
b = 2
c = 1
d = 1

print(a == b == c == d == 1)
print(all (i == 1 for i in (a,b,c,d)))