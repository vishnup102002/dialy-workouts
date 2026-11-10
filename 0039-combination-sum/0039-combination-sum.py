class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        n=len(candidates)
         
        def findcomb(ind:int,targ:int,ds:list[int],ans:list[list[int]]):
            if ind==n or targ<0:
                return          
            if targ == 0:
                ans.append(list(ds)) 
                return    
            if candidates[ind]<=targ:
                ds.append(candidates[ind])
                findcomb(ind,targ-candidates[ind],ds,ans)
                ds.pop()
            findcomb(ind+1,targ,ds,ans)
        res=[]
        dds=[]
        findcomb(0, target, [], res)  
        return res
                
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna