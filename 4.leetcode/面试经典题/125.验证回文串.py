

def condition(i):
    if ord(i)>=48 and ord(i)<=57:
        return True
    elif ord(i)<=90 and ord(i)>=65:
        return True
    elif ord(i)<=122 and ord(i)>=97:
        return True
    else:
        return False

def isPalindrome(s: str) -> bool:
    res = ""
    for i in s:
        if condition(i):
            res+=i
    if len(res)==0:
        return True
    res = res.lower()
    j = len(res)-1
    k = 0
    while k<j:
        if res[k]!=res[j]:
            return False
        k+=1
        j-=1
    return True

if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))