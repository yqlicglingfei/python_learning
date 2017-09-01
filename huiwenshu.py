def huiwenshu(n):
    if len(n) == 1:
        return True
    elif len(n) == 2 and n[0] == n[1]:
        return True
    
    if n[0] == n[-1]:
        n = n[1:-2]
        huiwenshu(n)

    return False

if __name__ == "__main__":
    print('please input a digit')
    n = input()
    if huiwenshu(n):
        print('Yes')
    else:
        print('No')
