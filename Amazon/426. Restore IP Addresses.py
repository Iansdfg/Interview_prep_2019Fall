class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        # write your code here
        result = []
        self.dfs(s, [], result)
        return result
        
    def dfs(self, s, path, result):
        if len(path) == 4 and not s:
            result.append('.'.join(path[:]))
            return
        if len(path) == 4 and s:
            return
        
        for i in [1, 2, 3]:
            if not self.is_valid(i, s):
                continue
            
            ip_num = s[:i]
            path.append(ip_num)
            self.dfs(s[i:], path, result)
            path.pop()
            
            
    def is_valid(self, i, s):
        if i > len(s):
            return False
        ip = s[:i]
        if int(ip) > 255:
            return False
        if len(ip) > 1 and ip[0] == '0':
            return False 
        return True
            
