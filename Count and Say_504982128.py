class Solution(object):
    def countAndSay(self, n):
        
        def countnumber(self, s):
            count = 0
            num = 0
            string = ""
            
            for i in s:
                if (num == i):
                    count += 1
                elif (num == 0):
                    num = i
                    count = 1
                else:
                    string = string + str(count)
                    string = string + str(num)
                    num = i
                    count = 1
            
            
            string = string + str(count)
            string = string + str(num)
            return (string)                          
            
        
        base = "1"
        count = 0
        i = 1
        while(i < n):
            base = countnumber(self, base)
            i = i+1
        return base
            
        
        
            
        """
        :type n: int
        :rtype: str
        """
        
