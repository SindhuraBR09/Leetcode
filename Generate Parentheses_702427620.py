class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def generate(self, n, s, opened, closed, res):
            
            if len(s) == 2*n:
                res.append(s)
                return res
            else:
                if opened < n:
                    # s=s+'('
                    res = generate(self, n, s+'(', opened+1, closed, res)
                if closed < opened:
                    # s=s+')'
                    res = generate(self, n, s+')', opened, closed+1, res)
            return res
                        
        res = []
        res = generate(self, n, "", 0,0,res)
        return res
                    
                            
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         def createPar(self, s, l, n, opened, closed):
#             if (len(s) == 2*n):
#                 l.append(s)
#                 return l
            
#             else:
#                 if (opened < n):
#                     l = createPar(self, s+'(', l, n, opened+1, closed)
#                 if(closed < opened):
#                     l = createPar(self, s+')', l, n , opened, closed+1)
                    
#             return l
            
        
#         l = []
#         l = createPar(self, "", l, n, 0,0)
#         return l
            
                
        
