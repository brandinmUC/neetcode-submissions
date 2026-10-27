class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        n1_l, n2_l = len(num1), len(num2)
        num1, num2 = self.convertToInt(num1, n1_l), self.convertToInt(num2, n2_l)
        # print(num1, num2)

        return str(num1 * num2)

    
    def convertToInt(self, num, l):
        num_conv = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}

        res = 0
        for i in range(1, l + 1):
            # print(i, 10**(l - i),  num_conv[num[i - 1]])
            place = 10**(l - i) * num_conv[num[i - 1]]
            res += place
        return res
