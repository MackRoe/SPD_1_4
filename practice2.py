
def f(a, k):
    while k > 0:
        # enumerate(a)  # returns both index and value
        for i, v in enumerate(a):  # replace range(len(a)) with enumerate(a)
            a[i] += (2 * i)
        k -= 1
    return a


a, k = [1, 2, 3, 4, 5], 2
print(f(a, k))

''' Variable Table:
    k: 0
    i: 4
    a[i]: 13
    a: 1, 4, 7, 10, 13
        [1, 6, 11, 16, 21]  << expected output

Time Complexity: O(n^2) aka O(k*n)
    '''
