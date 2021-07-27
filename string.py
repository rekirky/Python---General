string = "Birds are sometimes best stored in the fins"
a = string[0]
b = string[1]
c = string[-2]
d = string[-1]

print(f"The treasure is in the {a}{b}{c}{d}!")

print(f"The treasure is in the {string[:2]}{string[-2:]}!")


secret = input("Secret phrase? ")
a = secret[0]
b = secret[1]
c = secret[-2]
d = secret[-1]
print("The treasure is in the " + a + b +c + d + "!")



print('abcdefcdghcd'.split('cd'))

def func(num):
    num += 1
    return num

a = 10
a = func(a)
print(func(a))
