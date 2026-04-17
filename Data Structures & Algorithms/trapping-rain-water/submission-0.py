class Solution:
    def trap(self, height: List[int]) -> int:
        
        if height is None:
            return False
        
        left=0
        right=len(height)-1

        parallel = [0]  * (len(height))
    
        base_val = height[right]
        while right!=0:
            if height[right-1]>=base_val:
                base_val=height[right-1]
                right-=1
            else:
                parallel[right-1] = base_val - height[right-1]
                right-=1
        print(parallel)
        
        parallel2=[0]*len(height)
        base_val=height[0]
        while left!= (len(height)-1):
            if height[left+1]>=base_val:
                base_val=height[left+1]
                left+=1
            else:
                parallel2[left+1] = base_val - height[left+1]
                left+=1
        print(parallel2)

        sums=[0]*len(height)

        for i in range(len(parallel)):
            sums[i]=min(parallel[i],parallel2[i])
        
        return sum(sums)
            
            



            