def encrypt(s):
    l=len(s)
    
    s_encrypted=""
    
    for i in range(0,l):
        ch=s[i]
        s_encrypted+=str(bin(ord(ch)))+"~"
    
    s_encrypted=s_encrypted[::-1]
    
    return s_encrypted