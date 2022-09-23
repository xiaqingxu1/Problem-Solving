class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        
        if '.' in queryIP:
            ip = queryIP.split('.')
            if len(ip) == 4:
                IPv4 = True
                for i in ip:
                    if IPv4:  
                        if i.isdigit() and (i == '0' or (0 <= int(i) <= 255 and i[0] != '0')):
                            continue
                        else:
                            IPv4 = False
                
                if IPv4:
                    return 'IPv4'
        
        if ':' in queryIP:
            ip6 = queryIP.split(':')
            if len(ip6) == 8:
                IPv6 = True
                
                for i in ip6:
                    if IPv6:
                        ip = list(i)
                        if not i or len(i) > 4:
                            IPv6 = False
                        for char in ip:
                            if char not in "0123456789abcdefABCDEF":
                                IPv6 = False
                        
                if IPv6:
                    return 'IPv6'
        
        return 'Neither'
        
                            
                        
            
            
            
                        
                     
                        
        