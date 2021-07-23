names = ['oliver queen','peter pan','james bond','muhammad khan','david paterson','grey hamilton']
username = []

def uname(names):
    for n in names:
        # Splitting Full Name into two lists
        full_name = n.split()
        # Makes a new list with all the first names
        f_name = full_name[0]
        # Makes a new list with all the last names
        l_name = full_name[1]
        # Concatinating to make a special username.
        uname = f_name + '_' + l_name[0]
        # Appending the list of username with uname
        username.append(uname)

uname(names)
print(username)


import re

string =["www.website.com/ThingIWantHere/blahblahblah","www.website.com/ThingIWantHere2/blahblahblah"]

for i in string:
    w = re.search("^.*/[a-zA-Z]+/.*$",i)
    print(w.group(0))
