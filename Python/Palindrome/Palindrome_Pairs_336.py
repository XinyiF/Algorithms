#Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
# so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

class Solution(object):
    def palindromePairs_BF(self, words):
        res=[]
        for i in range(len(words)-1):
            for j in range(i+1,len(words)):
                if (len(words[i])+len(words[j]))%2==0:
                    temp,mid=words[i]+words[j],int((len(words[i])+len(words[j]))/2)
                    if temp[0:mid]==temp[mid:len(words[i]) + len(words[j])][::-1]:
                        pair=[i,j];res.append(pair)
                    temp=words[j]+words[i]
                    if temp[0:mid]==temp[mid:len(words[i]) + len(words[j])][::-1]:
                        pair=[j,i];res.append(pair)
                else:
                    temp, mid = words[i] + words[j], int((len(words[i])+len(words[j]))/2)
                    if len(temp)==1:
                        pair1,pair2=[i,j],[j,i]
                        res.append(pair1);res.append(pair2)
                    else:
                        if temp[0:mid] == temp[mid + 1:len(words[i]) + len(words[j])][::-1]:
                            pair = [i, j];res.append(pair)
                        temp = words[j] + words[i]
                        if temp[0:mid] == temp[mid + 1:len(words[i]) + len(words[j])][::-1]:
                            pair = [j, i];res.append(pair)
        return res


    def palindromePairs(self, words):
        # store words who is palindrome itself, include ''
        palidStr = []
        # reverse words and their index
        rev_words = {}
        # result
        res = []
        for idx, word in enumerate(words):
            rev_words[word[::-1]] = idx
            if word == word[::-1]:
                palidStr.append(idx)
        for idx, word in enumerate(words):
            if word:
                for i in range(len(word)):
                    left, right = word[:i], word[i:]
                    # if we can find word add to its left to make them to a palindrome
                    if left == left[::-1] and right in rev_words and idx != rev_words[right]:
                        res.append([rev_words[right], idx])
                    # add to right
                    if right == right[::-1] and left in rev_words and idx != rev_words[left]:
                        res.append([idx, rev_words[left]])
            else:
                # for ''
                for loc in palidStr:
                    if loc != idx:
                        res.append([idx, loc])
        return res





words=["a","","abc","aba"]
res=Solution()
result=res.palindromePairs(words)
print(result)
