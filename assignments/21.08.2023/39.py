class solution:
    def combination(self,li,target):
        result=[]
        def backstrack(index,current_set,target):
            if target==0:
                result.append(list(current_set))
                return
            
            for i in range(index,len(li)):
                if target-li[i]>=0:
                    current_set.append(li[i])
                    backstrack(i,current_set,target - li[i])
                    current_set.pop()

        backstrack(0,[],target)
        return result

s = solution()
k = s.combination([2,2,3],7)
kf = set(map(tuple,k))
print(list(kf))