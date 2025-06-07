# 作者：liuyankai
# 时间：2025年06月07日23时27分53秒
# liuyankai23@mails.ucas.ac.cn
def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for i in tokens:
        if i == '+':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a + b)
        elif i == '-':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a - b)
        elif i == '*':
            b = int(stack.pop())
            a = int(stack.pop())
            stack.append(a * b)
        elif i == '/':
            b = int(stack.pop())
            a = int(stack.pop())
            if a * b < 0:
                res = abs(a)//abs(b)
                stack.append(-res)
            else:
                stack.append(a // b)
        else:
            stack.append(int(i))
    return int(stack[0])

if __name__ == '__main__':
    print(-6 // 4)
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(evalRPN(tokens))