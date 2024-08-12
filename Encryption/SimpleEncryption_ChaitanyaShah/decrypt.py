def decrypt(s):
    
    s=s[::-1]
    s_decrypted=""
    temp=""
    
    for ch in s:
        if ch != "~":
            temp += ch
        else:
            s_decrypted += chr(int(temp,2))
            temp = ""
    
    if temp != "":
        s_decrypted += chr(int(temp))
    
    return s_decrypted