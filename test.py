import numpy as np
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        numberArray = [int(x) for x in num]
        numberArray = np.array(numberArray)
        print(numberArray)
        if len(numberArray) == k:
            return "0"
        multiplier = [x for x in range(len(numberArray) , 0 , -1)]
        print(multiplier)
        multiplier = np.array(multiplier)
        multiplied = [[multiplier * numberArray]]
        print(multiplied)
        multiplied.append(numberArray)
        print(multiplied)
        print(multiplied)
num = "1234343"
k = 3
first = Solution()
first.removeKdigits(num , k)