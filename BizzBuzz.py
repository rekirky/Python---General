# For a range of numbers. 
# If number is divisible by variable A - display Bizz
# If number is divisible by variable B - display Buzz
# If divisible by both variable A & B - display BizzBuzz

A = 2
B = 5
count = 1000

for i in range(1,count+1,1):
    output = ""
    if i%A == 0:
        output += "Bizz"
    
    if i%B == 0:
        output += "Buzz"
    
    if output == "":
        output = i 
    
    print(output)