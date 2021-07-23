my_list = ["This","is","a","split","of","words","BREAK","this","is","not","to","be","included"]
string = ""

for words in my_list:
    if words == "BREAK":
        break
    else:
        string += words
print(f"{string} \n")