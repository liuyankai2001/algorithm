def reverse_str(s, left, right):
    i = left
    j = right
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


def reverseStr(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    i = 0
    j = 0
    str = list(s)
    while j < len(str)-1:
        while j - i + 1 < 2 * k and j < len(str)-1:
            j += 1
        if j>=len(str):
            break
        reverse_str(str, i, i + k - 1)
        i = j + 1
        j += 1
    if j-i+1<k:
        reverse_str(str,i,j)
    else:
        reverse_str(str, i, i + k - 1)
    ans = "".join(str)
    return ans

if __name__ == '__main__':
    # s = "abcdefg"
    s = "a"
    k = 2
    print(reverseStr(s, k))