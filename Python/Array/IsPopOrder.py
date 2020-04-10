#The first sequence represents the push order of the stack.
# Please determine whether the second sequence may be the pop order of the stack.
class Solution:
    def IsPopOrder(self, pushV, popV):
        if len(pushV)==1:
            if pushV[0]==popV[0]:
                return True
            else:
                return False
        stack,j,i=[],0,0
        while i<len(pushV):
            for i in range(len(pushV)):
                if pushV[i] != popV[0]:
                    stack.append(pushV[i])
                else:
                    i += 1
                    j += 1
                    break
            if pushV[i]!=popV[j] and not popV[j] in stack:
                while i < len(pushV):
                    if pushV[i] != popV[j]:
                        stack.append(pushV[i])
                        i+=1
                    else:
                        i += 1
                        j += 1
                        break
            elif pushV[i]==popV[j]:
                i+=1
                j+=1
            else:
                return False
        while j <len(popV):
            if popV[j]==stack.pop():
                j+=1
            else:
                return False
        return True

    def IsOrder(self,pushV,popV):
        stack,i,j=[],0,0
        while i<len(pushV):
            if pushV[i]!=popV[j] and not popV[j] in stack:
                stack.append(pushV[i])
                i+=1
            elif pushV[i]==popV[j]:
                i+=1
                j+=1
            elif popV[i]!=pushV[i] and popV[j]==stack[-1]:
                stack.pop()
                j+=1
            else:
                return False
        while j<len(popV):
            if popV[j]==stack.pop():
                j+=1
            else:return False
        return True








push=[1]
pop=[1]
res=Solution()
print(res.IsOrder(push,pop))