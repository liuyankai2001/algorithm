def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    str_list = s.strip().split(' ')
    str_list.reverse()
    ans = []
    i = 0
    for i in range(len(str_list)):
        if str_list[i] == '':
            continue
        ans.append(str_list[i])

    return ' '.join(ans)

if __name__ == '__main__':
    s = "a good   example"
    print(reverseWords(s))