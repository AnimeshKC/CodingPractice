def iterativeFibonacchi(n):
    '''returns fibonacci sequence upto a number n using iteration'''
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        arr = [0, 1]
        for i in range(2, n):
            arr.append(arr[i-1] + arr[i - 2])
        return arr

if __name__ == '__main__':
    print(iterativeFibonacchi(5))