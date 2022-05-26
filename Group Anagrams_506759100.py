class Solution(object):
    def groupAnagrams(self, strs):
        
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
                
        # for key in mapper.keys():
        #     ans.append(mapper[key])
            
        return mapper.values()

        # d = {}
        # for w in sorted(strs):
        #     key = tuple(sorted(w))
        #     d[key] = d.get(key, []) + [w]
        # return d.values()
            
            
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
