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
print(float("2.x"))