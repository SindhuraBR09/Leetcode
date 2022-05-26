class Solution(object):
    def evalRPN(self, tokens):
        
        stack = []
        for ele in tokens:
            if (ele == "+"):
                p1 = stack.pop()
                p2 = stack.pop()
                stack.append(p1+p2)
            elif (ele == '-'):
                p1 = stack.pop()
                p2 = stack.pop()
                stack.append(p2-p1)
            elif (ele == '*'):
                p1 = stack.pop()
                p2 = stack.pop()
                stack.append(p1*p2)
            elif (ele == '/'):
                p1 = stack.pop()
                p2 = stack.pop()
                stack.append(int(float(p2)/p1))
            else:
                stack.append(int(ele))
           
        return stack.pop()
            
            
            
            
            
            
        #     if (ele.isdigit()):
        #         stack.append(int(ele))
        #     else:
        #         p1 = stack.pop()
        #         p2 = stack.pop()
        #         print("P1 and P2 {} {} {}".format(p1,p2,ele))
        #         if (ele == "+"):                    
        #             stack.append(p1+p2)
        #         if (ele == '-'):
        #             stack.append(p2-p1)
        #         if (ele == '*'):
        #             stack.append(p1*p2)
        #         if (ele == '/'):
        #             stack.append(int(p2/p1))
        # return stack.pop()
                    
        """
        :type tokens: List[str]
        :rtype: int
        """
        
