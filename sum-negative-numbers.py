range = [-1, -2, -3, -2, 0, 1, -2, -3, 0, 0]

# This takes the range and provides a 2D array - count of consecutive values + their sum
def get_list(range):
    count = 0
    sum = 0
    list=[]
    x = 0
    for i in range:
        if i < 0:
            count += 1
            sum+=i
        else:
            list.append([count,sum])
            count = 0
            sum = 0
    return(list)
   



