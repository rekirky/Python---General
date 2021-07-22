a = True
b = not a
print(not (a and b))

input_str = "python"
input_list = []
for i in input_str:
    input_list.append(i)

print(input_list)

sentence = "What a lovely day!"
print(sentence[-1])

camel = r"""
Switching on the camera in the camel habitat...
"""

lion = r"""
Switching on the camera in the lion habitat...
"""

deer = r"""
Switching on the camera in the deer habitat...
"""

goose = r"""
Switching on the camera in the goose habitat...
"""

bat = r"""
Switching on the camera in the bat habitat...
"""

rabbit = r"""
Switching on the camera in the rabbit habitat...
"""

def a123():
    habitats = [camel,lion,deer,goose,bat,rabbit]
    value = int(input("Please enter the number of the habitat you would like to view: > "))
    print(habitats[value])
    print("---")
    print("You've reached the end of the program. To check another habitat, please restart the watcher.")

print(49**0.5)

a = True
b = False
c = a and not b

print(a and (not c or b))


i = 0
while i <= 10:
    i = i + 1
    if i > 7:
        i = i + 2
print(i)

print(float(-52))
print(float("52.0"))


print("\\\\")


def mystery_delete():
    mystery_set = [1,2,3]
    # mystery_set has been defined
    string = 2

# delete string from mystery_set
    mystery_set_temp = mystery_set
    for i in mystery_set_temp:
        if string == i:
            mystery_set.remove(i)

    print(mystery_set)
mystery_delete()

numbers1=[1,2,3,4,5]
answers1=[5,4,1,2,1,3]
result1=True
numbers2=[999,1,1001,15,6,7]
answers2=[1,6,7,1,999]
result2=False
numbers3=[3,4,5,7]
answers3=[3,4,5,6,7]
result3=False

def set_check(number,answer):
    if set(number) == set(answer):
        return True
    else:
        return False

print(set_check(numbers3,answers3))