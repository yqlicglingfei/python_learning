def getOnesInNumber(n):
    i = n
    num = 0
    while (i > 0):
        if i % 10 == 1:
            num+=1
        i /= 10
    return num

def getOnes(n):
    sum = 0
    l=[i for i in range(0, int(n))]
    l1=[i for i in l if '1' in str(i)]
    for i in l1:
        sum += getOnesInNumber(i)
    print('has', sum, 'ones')

if __name__ == '__main__':
    print('input a digit')
    n=input()
    getOnes(n)
