def main(s):
    str = list(s)
    new_str = []
    for i in str:
        if ord(i)>=ord('0') and ord(i)<=ord('9'):
            new_str.append('number')
        else:
            new_str.append(i)
    print(''.join(new_str))

if __name__=='__main__':
    s = input()
    main(s)