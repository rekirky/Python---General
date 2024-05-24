# For a range of numbers. 
# If number is divisible by variable A - display Fizz
# If number is divisible by variable B - display Buzz
# If divisible by both variable A & B - display FizzBuzz

A = 3
B = 5
count = 100

for i in range(1,count+1,1):
    output = ""
    if i%A == 0:
        output += "Fizz"
    
    if i%B == 0:
        output += "Buzz"
    
    if output == "":
        output = i 
    
    print(output)