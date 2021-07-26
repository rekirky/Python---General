import re
s = "Hello--#$-# --$$12.5 holy mother hehe#@$@$@#%&"
#s="^&*(12"
resultList = re.findall(r"[\-\$\.]+[0-9]+|\s|\w", s)
resultString = "".join(resultList)
resultString = re.sub(r'([^a-z])\1+', r'\1', resultString)
#resultString = "".join(resultList).replace("--","-").replace("$$","$")

print(resultString)