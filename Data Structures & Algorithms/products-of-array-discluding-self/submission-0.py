class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = []
        postfix = []

        for i in range(len(nums)):
            if i == 0:
                prefix.append(nums[0])
                postfix.append(nums[-1])
            else:
                prefix.append(prefix[i - 1] * nums[i])
                postfix.insert(0, nums[-1 - i] * postfix[0])
        
        for i in range(len(nums)):
            product = 1
            if i == 0:
                product *= postfix[i + 1]
            else:
                if i != len(nums) - 1:
                    product *= prefix[i - 1] * postfix[i + 1]
                else:
                    product *= prefix[i - 1]
            output.append(product)
            

        return output