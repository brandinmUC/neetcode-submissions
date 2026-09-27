class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        for i in range(len(nums)):
            # prefixes
            product = 1
            if i == 0:
                output.append(product)
            else:
                output.append(product * output[i - 1] * nums[i - 1])
        
        print(output)
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            # suffixes            
            output[i] *= suffix
            suffix *= nums[i]
            
        return output