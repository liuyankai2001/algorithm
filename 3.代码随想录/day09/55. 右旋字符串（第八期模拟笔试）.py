

def reverse_str(str,left,right):
    i = left
    j = right
    while i<j:
        str[i],str[j]=str[j],str[i]
        i+=1
        j-=1

def main():
    k = int(input())
    str = input()
    str = list(str)
    length = len(str)
    reverse_str(str, 0, length-1)
    reverse_str(str,0,k-1)
    reverse_str(str,k,length-1)
    print(''.join(str))

if __name__=="__main__":
    main()