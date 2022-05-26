class Solution(object):
    def groupAnagrams(self, strs):
        
#         mainlist = []
#         def CheckInMainlist(self, word):
#             # word = list(word)
#             templist = []
#             print("Input word is {}".format(word))
            
#             for list1 in mainlist:
#                 print("list1 is {}".format(list1))
#                 temp=list1[0]
#                 print("first word of list {}".format(temp))
#                 m1 = list(temp)
#                 m2 = list(str(word))
#                 print(m1)
#                 print(m2)
#                 m1.sort()
#                 m2.sort()
#                 print(m1)
#                 print(m2)
#                 if (m1==m2):
#                     list1.append(word)
#                     return
#             templist.append(str(word))
#             mainlist.append(templist)
            
#         for word in strs:
#             CheckInMainlist(self, word)
        
#         return mainlist

        mapper = {}
        ans = []
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in mapper.keys():
                temp = mapper[sorted_word]
                temp.append(word)
            else:
                temp = [word]
                mapper[sorted_word] = temp
                
        for key in mapper.keys():
            ans.append(mapper[key])
            
        return ans
            
            
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
