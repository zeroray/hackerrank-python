if __name__ == '__main__':
    a = int(input())
    b = int(input())

    print(a, b, 10^10)
    if a >= 1 and a <= 10**10 and b >= 1 and b <= 10**10:
        print(a+b)
        print(a-b)
        print(a*b)
    else:
        print("Other path")