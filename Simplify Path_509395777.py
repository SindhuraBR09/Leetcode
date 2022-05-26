class Solution(object):
    import re
    
    def simplifyPath(self, path):
        
        res = ['/']
        if (path[0] == '/'):
            path = path[1:]
        
        path = re.sub('//','/',path)
        l = path.split('/')
        
        print("l is {}".format(l))
        char = ''
        for char in l:
            if (char == '..'):
                if(len(res) > 1):
                    res.pop()
                    res.pop()
            elif (char == '.'):
                continue
            elif (char == ''):
                continue
            else:
                res.append(char)
                res.append('/')
                
        if (res[-1] == '/' and len(res) > 1):
            res.pop()
        return ''.join(res)
                    
        
        """
        :type path: str
        :rtype: str
        """
        
