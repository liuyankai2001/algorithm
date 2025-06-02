# 作者：liuyankai
# 时间：2025年06月02日16时02分03秒
# liuyankai23@mails.ucas.ac.cn
def calculate(n):
    sum = 0
    while n:
        sum += n % 10
        n //= 10
    return sum


def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    hash_map = {}
    while n != 1:
        res = hash_map.get(n, -1)
        if res > 0:
            return False
        hash_map[n] = 1
        n = calculate(n)
    return True

if __name__ == '__main__':
    n = 7
    print(isHappy(n))