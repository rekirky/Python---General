def count_ones(num):
    count = 0
    input = bin(num)[2:]
    
    for i in input:
        if int(i) == 1:
        print(i)
        count +=1
    return count


print(count_ones(4))