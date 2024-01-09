
def gcdOfStrings(str1, str2):
    """
    :type str1: str
    :type str2: str
    :rtype: str
    """
    str1_len = len(str1)
    str2_len = len(str2) 
    for i in range(min(str1_len, str2_len), 0, -1):
        sub_str = str1[:i]
        sub_str_len = len(sub_str)
        
        if str1_len%sub_str_len or str2_len%sub_str_len:
            pass
        else:
            div1, div2 = str1_len//sub_str_len, str2_len//sub_str_len
            if sub_str * div1 == str1 and sub_str * div2 == str2:
                return sub_str
    return ""
print(gcdOfStrings('ABCABC', 'ABC'))