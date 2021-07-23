#n = input()
n = '6623456789'
def orig_code():
    n = input()
    count =0
    if n[0] in '6789' and len(n) == 10 and n.isdigit()== True: # check first digit, length & that it is a digit
        for i in range(0,len(n)):
            print(i)
            for j in range(0,i):
                print(j)
                if i == j:
                    count +=1
                    if count > 7:
                        print('invalid')
                        if n[i] == n[i+1] == n[i+2]== n[i+3] == n[i+4] == n[i+5]:
                            print('invalid')
                        else:
                            print('valid')
    else:
        print('invalid')

def new_code(input):
    count=0
    if input[0] in '6789' and len(input) == 10 and input.isdigit():  #check 1,2
        for i in range(1,len(input)):
            if input[i-1] == input[i]:
                count+=1
        print(count)
           

new_code(n)



'''
This is the question
Accept phone number from user as string.
A valid phone number should satisfy the following constraints.
1. The number should start with 6,7,8 and 9.
2. Length of the number should be 10.
3. Number should not have any digit repeated more then 5 times in consecutive manner.
4. Number should not have any digit more than 7 times...
pl point out the mistakes in my code
'''