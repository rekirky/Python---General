# Convert Roman Numberals into Integer

class Solution:
    def romanToInt(self, s: str) -> int:
        try:
            s=s[::-1] #reverse the string
            
            #put roman numerals and its value into hashmap
            romanHash = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
            prevVal = 0 #contains previous value
            value = 0 #sum of value in loop so far
            
            #if the previous value is bigger than the current value, subtract the current value from the total value
            for char in s:
                hashVal = romanHash[char]
                
                if prevVal > hashVal:
                    value -= hashVal
                else: 
                    value += hashVal
                
                prevVal = hashVal
            return value
        except:
            print("Enter a valid roman numeral")

value = input("Enter Roman Numerals to convert: ")
print(Solution.romanToInt(None,value))